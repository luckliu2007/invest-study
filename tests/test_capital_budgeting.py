"""capital_budgeting 的单元测试：核心公式用手算可验证的现金流检验。"""
import math

import capital_budgeting as cb


def test_npv_and_irr_simple():
    flows = [-100, 110]
    assert math.isclose(cb.npv(0.10, flows), 0.0, abs_tol=1e-9)
    assert math.isclose(cb.irr(flows), 0.10, abs_tol=1e-6)


def test_irr_matches_npv_zero_for_annuity():
    flows = [-1000] + [300] * 5
    r = cb.irr(flows)
    assert r is not None
    assert math.isclose(cb.npv(r, flows), 0.0, abs_tol=1e-4)


def test_irr_none_without_sign_change():
    assert cb.irr([100, 50, 20]) is None
    assert cb.irr([-100, -50]) is None


def test_payback_interpolates():
    # 累计：-100, -60, -20, +20 → 第 2 年末还差 20，第 3 年流入 40，回收期 2.5 年
    assert math.isclose(cb.payback([-100, 40, 40, 40]), 2.5)


def test_payback_never_recovered():
    assert cb.payback([-100, 10, 10]) is None


def test_discounted_payback_longer_than_simple():
    flows = [-100, 40, 40, 40, 40]
    assert cb.discounted_payback(0.10, flows) > cb.payback(flows)


def test_multiple_irr_risk_flag():
    # 正负号变化两次（投资 → 流入 → 期末大额拆除费用）
    r = cb.evaluate([-100, 230, -132], 0.10)
    assert r["multiple_irr_risk"] is True


def test_example_project_scenarios_ordered():
    npvs = {name: cb.npv(0.10, cb.project_cashflows(**p)) for name, p in cb.SCENARIOS.items()}
    assert npvs["悲观"] < npvs["基准"] < npvs["乐观"]


def test_higher_rate_lowers_npv():
    flows = cb.project_cashflows()
    assert cb.npv(0.12, flows) < cb.npv(0.08, flows)


def test_sensitivity_sorted_and_directional():
    rows = cb.sensitivity(0.10)
    swings = [r["swing"] for r in rows]
    assert swings == sorted(swings, reverse=True)
    capex = next(r for r in rows if r["param"] == "capex")
    assert capex["npv_high"] < capex["npv_low"]   # 投资额越高，NPV 越低
    margin = next(r for r in rows if r["param"] == "margin")
    assert margin["npv_high"] > margin["npv_low"]


def test_example_project_is_a_real_decision():
    """示例项目应体现“结论取决于判断”：基准情景值得做，悲观情景不值得做。"""
    assert cb.npv(0.10, cb.project_cashflows()) > 0
    assert cb.npv(0.10, cb.project_cashflows(**cb.SCENARIOS["悲观"])) < 0
