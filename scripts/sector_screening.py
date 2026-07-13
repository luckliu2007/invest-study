"""
行业/赛道筛选脚本 v2026.1
功能：拉取 A 股列表，按行业过滤，计算 ROE/PE 等因子，输出候选池。
数据源：akshare（需 pip install akshare）
兼容：无网络/无 akshare/接口字段变化时自动降级为内置示例数据，保证流程可跑通。
输出：reports/sector_screening.csv
"""
import os
import sys

# Windows 控制台默认非 UTF-8，中文输出会 UnicodeEncodeError
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    import akshare as ak
    HAVE_AK = True
except Exception:
    HAVE_AK = False

import pandas as pd

INDUSTRY_KEYWORD = "新能源车"  # 可改为 "半导体"/"人工智能"/"医药" 等
ROE_MIN = 0.15
PE_MAX = 20
OUT = "reports/sector_screening.csv"

# 缺少任一必需字段就降级为示例数据，避免接口字段变化导致 KeyError
REQUIRED_COLS = {"ticker", "name", "industry"}


def sample_universe():
    return pd.DataFrame({
        "ticker": ["600519", "000858", "300750", "002594", "600036"],
        "name": ["贵州茅台", "五粮液", "宁德时代", "比亚迪", "招商银行"],
        "industry": ["白酒", "白酒", "新能源车", "新能源车", "银行"],
        "close": [1700, 150, 220, 260, 40],
        "roe": [0.30, 0.25, 0.18, 0.16, 0.17],
        "pe": [35, 25, 28, 18, 7],
    })


def load_universe():
    if HAVE_AK:
        try:
            df = ak.stock_zh_a_spot()
            df = df.rename(columns={"代码": "ticker", "名称": "name", "行业": "industry",
                                   "最新价": "close", "市盈率": "pe"})
            missing = REQUIRED_COLS - set(df.columns)
            if missing:
                print(f"[warn] akshare 返回缺少字段 {sorted(missing)}（接口字段可能已变化），使用示例数据")
                return sample_universe()
            return df
        except Exception as e:
            print(f"[warn] akshare 拉取失败，使用示例数据: {e}")
    return sample_universe()


def screen(industry=INDUSTRY_KEYWORD, roe_min=ROE_MIN, pe_max=PE_MAX):
    df = load_universe()
    target = df[df["industry"].astype(str).str.contains(industry, na=False)]
    if "roe" in target.columns and "pe" in target.columns:
        cands = target[(target["roe"] > roe_min) & (target["pe"] < pe_max)]
    else:
        print("[warn] 缺少 roe/pe 字段，仅按行业过滤，不做因子筛选")
        cands = target
    return cands


if __name__ == "__main__":
    cands = screen()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cands.to_csv(OUT, index=False, encoding="utf-8-sig")
    print(f"候选池（行业含'{INDUSTRY_KEYWORD}' 且 ROE>{ROE_MIN} PE<{PE_MAX}）：")
    print(cands.to_string(index=False))
    print(f"已生成 {OUT}")
