"""
投资组合优化脚本 v2026
功能：给定价格序列，计算最小波动率 / 最大夏普权重。
依赖：pyportfolioopt, pandas, numpy
降级：无价格文件时生成示例相关矩阵。
"""
import os
import numpy as np
import pandas as pd

PRICE_CSV = "data/price_history.csv"


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
        print("最小波动率权重：", w_min)
        print("最大夏普权重：", w_sharpe)
    except Exception as e:
        print(f"[warn] pyportfolioopt 不可用，输出等权基准: {e}")
        print(prices.pct_change().mean())


if __name__ == "__main__":
    optimize()
