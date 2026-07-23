"""exit_simulation 的单元测试：验证 IRR/MOIC 计算与降级二分法。"""
import math

import pytest

import exit_simulation as es


def test_simple_doubling_irr():
    # 投 1000，2 年后翻倍(溢价 100%)，无期间现金流 → IRR ≈ 41.4%
    r = es.simulate(1000, 1.0, 2)
    assert r["moic"] == 2.0
    assert r["irr"] == pytest.approx(0.4142, abs=1e-3)
    assert r["annualized_return"] == pytest.approx(0.4142, abs=1e-3)


def test_one_year_premium_equals_irr():
    # 持有 1 年、溢价 50% → IRR 恰为 50%
    r = es.simulate(1000, 0.5, 1)
    assert r["irr"] == pytest.approx(0.5, abs=1e-4)
    assert r["moic"] == 1.5


def test_interim_cashflows_raise_moic():
    no_interim = es.simulate(1000, 1.0, 5)
    with_interim = es.simulate(1000, 1.0, 5, interim_cashflows=[100, 100, 100, 100])
    assert with_interim["moic"] > no_interim["moic"]


def test_bisect_matches_analytic():
    # 直接测二分法兜底：现金流 [-1000, 1500]，IRR 应为 0.5
    r = es._irr_bisect([-1000, 1500])
    assert r == pytest.approx(0.5, abs=1e-5)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        es.simulate(0, 1.0, 3)
    with pytest.raises(ValueError):
        es.simulate(1000, 1.0, 0)


def test_npv_zero_at_irr():
    flows = [-1000, 200, 200, 1200]
    r = es.irr(flows)
    assert es._npv(r, flows) == pytest.approx(0.0, abs=1e-2)
