"""
投资组合优化脚本 v2026.1
功能：给定价格序列，计算最小波动率 / 最大夏普权重。
依赖：pyportfolioopt, pandas, numpy
降级：无价格文件时生成示例价格序列；无 pyportfolioopt 时输出等权基准。
输出：reports/portfolio_weights.csv
"""
import os
import sys

import numpy as np
import pandas as pd

# Windows 控制台默认非 UTF-8，中文输出会 UnicodeEncodeError
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PRICE_CSV = "data/price_history.csv"
OUT = "reports/portfolio_weights.csv"


def load_prices():
    if os.path.exists(PRICE_CSV):
        return pd.read_csv(PRICE_CSV, parse_dates=["date"], index_col="date")
    # 示例：3 只标的 250 日随机游走（可复现）
    np.random.seed(42)
    dates = pd.date_range("2025-01-01", periods=250, freq="B")
    cols = ["A", "B", "C"]
    paths = np.cumprod(1 + np.random.normal(0.0005, 0.02, (250, 3)), axis=0)
    return pd.DataFrame(paths, index=dates, columns=cols)


def optimize():
    prices = load_prices()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    try:
        from pypfopt import EfficientFrontier, risk_models, expected_returns
        mu = expected_returns.mean_historical_return(prices)
        S = risk_models.sample_cov(prices)
        ef = EfficientFrontier(mu, S)
        ef.min_volatility()
        w_min = ef.clean_weights()
        ef2 = EfficientFrontier(mu, S)
        ef2.max_sharpe()
        w_sharpe = ef2.clean_weights()
        pd.DataFrame({"min_volatility": w_min, "max_sharpe": w_sharpe}).to_csv(OUT, encoding="utf-8-sig")
        print("最小波动率权重：", w_min)
        print("最大夏普权重：", w_sharpe)
    except Exception as e:
        print(f"[warn] pyportfolioopt 不可用，输出等权基准: {e}")
        n = len(prices.columns)
        equal = pd.Series(1 / n, index=prices.columns, name="equal_weight")
        equal.to_csv(OUT, encoding="utf-8-sig")
        print(equal)
    print(f"已生成 {OUT}")


if __name__ == "__main__":
    optimize()
