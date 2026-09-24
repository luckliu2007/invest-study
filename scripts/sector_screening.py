"""
行业/赛道筛选脚本 v2026.1
功能：按行业板块拉取 A 股成分股，按 ROE/PE 等因子过滤，输出候选池。
数据源：akshare 东方财富行业板块接口（需 pip install akshare，国内网络）
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

INDUSTRY_KEYWORD = "汽车整车"  # 东方财富行业板块名，如 "半导体"/"电池"/"银行"/"酿酒行业"
ROE_MIN = 0.15
PE_MAX = 20
OUT = "reports/sector_screening.csv"

# 缺少任一必需字段就降级为示例数据，避免接口字段变化导致 KeyError
REQUIRED_COLS = {"ticker", "name", "industry"}

# 东方财富行业成分股接口的字段映射（该接口不含 ROE，实盘仅按 PE 过滤）
EM_COLUMNS = {"代码": "ticker", "名称": "name", "最新价": "close", "市盈率-动态": "pe"}


def sample_universe():
    return pd.DataFrame({
        "ticker": ["600519", "000858", "300750", "002594", "600036"],
        "name": ["贵州茅台", "五粮液", "宁德时代", "比亚迪", "招商银行"],
        "industry": ["酿酒行业", "酿酒行业", "电池", "汽车整车", "银行"],
        "close": [1700, 150, 220, 260, 40],
        "roe": [0.30, 0.25, 0.18, 0.16, 0.17],
        "pe": [35, 25, 28, 18, 7],
    })


def load_universe(industry=INDUSTRY_KEYWORD):
    """按行业板块拉取成分股。

    旧版用 ak.stock_zh_a_spot()，但它不返回“行业”“市盈率”字段，实盘路径永远走不通。
    改用东方财富行业板块成分股接口；该接口通常仅在国内网络可访问，海外（含 GitHub Actions）
    会连接失败并降级为示例数据。设置环境变量 INVEST_OFFLINE=1 可跳过联网直接用示例数据。
    """
    if HAVE_AK and not os.environ.get("INVEST_OFFLINE"):
        try:
            df = ak.stock_board_industry_cons_em(symbol=industry)
            df = df.rename(columns=EM_COLUMNS)
            df["industry"] = industry
            missing = REQUIRED_COLS - set(df.columns)
            if missing:
                print(f"[warn] akshare 返回缺少字段 {sorted(missing)}（接口字段可能已变化），使用示例数据")
                return sample_universe()
            if "pe" in df.columns:
                df["pe"] = pd.to_numeric(df["pe"], errors="coerce")
            return df
        except Exception as e:
            print(f"[warn] akshare 拉取行业“{industry}”失败，使用示例数据: {e}")
    return sample_universe()


def screen(industry=INDUSTRY_KEYWORD, roe_min=ROE_MIN, pe_max=PE_MAX):
    df = load_universe(industry)
    cands = df[df["industry"].astype(str).str.contains(industry, na=False)]
    # 有哪个因子列就用哪个过滤；亏损股 PE 为负或缺失，一并剔除
    if "roe" in cands.columns:
        cands = cands[cands["roe"] > roe_min]
    if "pe" in cands.columns:
        cands = cands[(cands["pe"] > 0) & (cands["pe"] < pe_max)]
    if not {"roe", "pe"} & set(cands.columns):
        print("[warn] 缺少 roe/pe 字段，仅按行业过滤，不做因子筛选")
    return cands


if __name__ == "__main__":
    # 用法：python scripts/sector_screening.py [东方财富行业板块名]
    industry = sys.argv[1] if len(sys.argv) > 1 else INDUSTRY_KEYWORD
    cands = screen(industry)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cands.to_csv(OUT, index=False, encoding="utf-8-sig")
    print(f"候选池（行业含'{industry}' 且 ROE>{ROE_MIN} PE<{PE_MAX}）：")
    print(cands.to_string(index=False))
    print(f"已生成 {OUT}")
