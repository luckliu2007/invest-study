"""backtest_stats 的单元测试：用 Bailey & López de Prado (2014) 论文中的数值例子校验。"""
import math
import random

import backtest_stats as bs


def test_paper_example_dsr_090():
    # 论文：100 次试验后，DSR≈0.90（只有 90% 的把握真实夏普大于 0），投资人拒绝
    r = bs.paper_example()
    assert math.isclose(r["dsr"], 0.9004, abs_tol=5e-4)
    assert r["dsr"] < 0.95


def test_paper_example_46_trials_passes():
    # 论文：如果只做了 46 次试验，DSR 为 0.9505，刚好超过 95%
    r = bs.paper_example(n_trials=46)
    assert math.isclose(r["dsr"], 0.9505, abs_tol=5e-4)


def test_paper_example_normal_returns_88_trials():
    # 论文：收益服从正态分布时，88 次试验后 DSR 才降到 0.95 左右
    r = bs.paper_example(n_trials=88, skew=0.0, kurt=3.0)
    assert math.isclose(r["dsr"], 0.9505, abs_tol=5e-4)


def test_expected_max_grows_with_trials():
    vals = [bs.expected_max_sharpe(n, 0.01) for n in (2, 10, 100, 1000)]
    assert vals == sorted(vals)
    assert bs.expected_max_sharpe(1, 0.01) == 0.0


def test_expected_max_close_to_simulation():
    rng = random.Random(7)
    n, sd, iters = 50, 0.1, 4000
    sim = sum(max(rng.gauss(0, sd) for _ in range(n)) for _ in range(iters)) / iters
    assert math.isclose(bs.expected_max_sharpe(n, sd ** 2), sim, rel_tol=0.03)


def test_psr_half_at_benchmark_and_fat_tails_hurt():
    assert math.isclose(bs.probabilistic_sharpe_ratio(0.1, 0.1, 500), 0.5)
    normal = bs.probabilistic_sharpe_ratio(0.1, 0.0, 500)
    fat = bs.probabilistic_sharpe_ratio(0.1, 0.0, 500, skew=-2, kurt=9)
    assert fat < normal


def test_sharpe_and_moments():
    rets = [0.01, -0.02, 0.03, 0.0, 0.015, -0.005]
    m = sum(rets) / len(rets)
    sd = math.sqrt(sum((r - m) ** 2 for r in rets) / (len(rets) - 1))
    assert math.isclose(bs.sharpe(rets), m / sd)
    s, k = bs.skew_kurt([-1.0, 0.0, 1.0])
    assert math.isclose(s, 0.0, abs_tol=1e-12) and math.isclose(k, 1.5)


def test_main_writes_csv(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bs.main()
    text = (tmp_path / bs.OUT).read_text(encoding="utf-8-sig")
    assert text.startswith("n_trials,") and len(text.strip().splitlines()) == 11
