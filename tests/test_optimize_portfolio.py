"""optimize_portfolio 的单元测试：覆盖示例价格生成与优化/降级输出。"""
import os

import pandas as pd

import optimize_portfolio as op


def test_load_prices_generates_sample_when_no_file(tmp_path, monkeypatch):
    # 指向一个不存在的价格文件，触发示例数据生成
    monkeypatch.setattr(op, "PRICE_CSV", str(tmp_path / "nope.csv"))
    prices = op.load_prices()
    assert isinstance(prices, pd.DataFrame)
    assert prices.shape == (250, 3)
    assert list(prices.columns) == ["A", "B", "C"]
    # 随机种子固定，结果应可复现
    prices2 = op.load_prices()
    assert prices.iloc[-1].equals(prices2.iloc[-1])


def test_load_prices_reads_existing_file(tmp_path, monkeypatch):
    csv = tmp_path / "price_history.csv"
    df = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=3, freq="D"),
        "X": [1.0, 1.1, 1.2],
        "Y": [2.0, 1.9, 2.1],
    })
    df.to_csv(csv, index=False)
    monkeypatch.setattr(op, "PRICE_CSV", str(csv))
    prices = op.load_prices()
    assert list(prices.columns) == ["X", "Y"]
    assert len(prices) == 3


def test_optimize_writes_output(tmp_path, monkeypatch):
    out = tmp_path / "reports" / "weights.csv"
    monkeypatch.setattr(op, "OUT", str(out))
    monkeypatch.setattr(op, "PRICE_CSV", str(tmp_path / "nope.csv"))
    op.optimize()
    assert out.exists()
    result = pd.read_csv(out, index_col=0)
    # 无论走 pyportfolioopt 还是等权降级，输出都应非空
    assert len(result) > 0
