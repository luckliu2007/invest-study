"""
资本预算工具 v2026.1
功能：企业项目投资评估——NPV、IRR、回收期、折现回收期、情景分析、敏感性分析。
依赖：仅标准库。
用法：python scripts/capital_budgeting.py
输出：reports/capital_budgeting.csv（情景与敏感性结果）

约定：现金流按年末发生，cashflows[0] 为第 0 年（通常为负的初始投资）。
"""
import csv
import os
import sys

# Windows 控制台默认非 UTF-8，中文输出会 UnicodeEncodeError
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = "reports/capital_budgeting.csv"


def npv(rate, cashflows):
    """按年末折现的净现值。"""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def sign_changes(cashflows):
    signs = [cf > 0 for cf in cashflows if cf != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def irr(cashflows, lo=-0.99, hi=10.0, tol=1e-9, max_iter=500):
    """二分法求 IRR。现金流没有正负变化时不存在 IRR，返回 None。

    现金流正负变化超过一次时可能存在多个 IRR，此时返回区间内找到的一个，
    并应以 NPV 为准做决策（见 evaluate 中的 multiple_irr_risk）。
    """
    if sign_changes(cashflows) == 0:
        return None
    f_lo, f_hi = npv(lo, cashflows), npv(hi, cashflows)
    if f_lo * f_hi > 0:
        return None
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def _payback(flows):
    cum = 0.0
    for t, cf in enumerate(flows):
        prev = cum
        cum += cf
        if t > 0 and prev < 0 <= cum:
            return t - 1 + (-prev / cf)   # 在当年内线性插值
    return None


def payback(cashflows):
    """静态回收期（年）；始终收不回投资返回 None。"""
    return _payback(cashflows)


def discounted_payback(rate, cashflows):
    """折现回收期（年）。"""
    return _payback([cf / (1 + rate) ** t for t, cf in enumerate(cashflows)])


def evaluate(cashflows, rate):
    return {
        "npv": npv(rate, cashflows),
        "irr": irr(cashflows),
        "payback_years": payback(cashflows),
        "discounted_payback_years": discounted_payback(rate, cashflows),
        "multiple_irr_risk": sign_changes(cashflows) > 1,
    }


def project_cashflows(capex=1000.0, working_capital=150.0, years=5, units=300.0, unit_growth=0.05,
                      price=6.0, margin=0.22, tax_rate=0.25, salvage=50.0):
    """示例项目：新产品线（单位：万元）。

    自由现金流 = EBIT×(1−税率) + 折旧 − 资本开支 − 营运资金变动；
    第 0 年投入设备和营运资金，期末收回营运资金和残值（残值按税后计）。
    margin 为折旧前经营利润率（EBITDA / 收入）。
    """
    dep = (capex - salvage) / years
    flows = [-(capex + working_capital)]
    for y in range(1, years + 1):
        revenue = units * (1 + unit_growth) ** (y - 1) * price
        ebitda = revenue * margin
        ebit = ebitda - dep
        fcf = ebit * (1 - tax_rate) + dep
        if y == years:
            fcf += working_capital + salvage
        flows.append(fcf)
    return flows


SCENARIOS = {
    "悲观": {"units": 230.0, "margin": 0.18},
    "基准": {},
    "乐观": {"units": 360.0, "margin": 0.25},
}
# 本模型中价格与销量对收入的影响相同，只保留销量
SENSITIVITY_PARAMS = ["units", "margin", "capex", "unit_growth"]


def sensitivity(rate, delta=0.10, base=None):
    """各参数分别上下浮动 delta，其他不变，返回 NPV 变化（用于画龙卷风图）。"""
    base = base or {}
    base_npv = npv(rate, project_cashflows(**base))
    defaults = project_cashflows.__defaults__
    names = project_cashflows.__code__.co_varnames[:project_cashflows.__code__.co_argcount]
    default_map = dict(zip(names, defaults))
    rows = []
    for p in SENSITIVITY_PARAMS:
        v = base.get(p, default_map[p])
        low = npv(rate, project_cashflows(**{**base, p: v * (1 - delta)}))
        high = npv(rate, project_cashflows(**{**base, p: v * (1 + delta)}))
        rows.append({"param": p, "npv_low": low, "npv_high": high, "swing": abs(high - low), "base_npv": base_npv})
    return sorted(rows, key=lambda r: r["swing"], reverse=True)


def main(rate=0.10):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    rows = []
    print(f"折现率（WACC）：{rate:.0%}")
    for name, params in SCENARIOS.items():
        r = evaluate(project_cashflows(**params), rate)
        irr_txt = f"{r['irr']:.2%}" if r["irr"] is not None else "无"
        pb = f"{r['payback_years']:.2f}" if r["payback_years"] is not None else "未回收"
        print(f"  {name}：NPV {r['npv']:8.1f} 万元  IRR {irr_txt:>7}  回收期 {pb} 年")
        rows.append({"type": "scenario", "name": name, **r})
    print("敏感性（各参数 ±10%，按 NPV 摆动幅度排序）：")
    for s in sensitivity(rate):
        print(f"  {s['param']:<8} NPV {s['npv_low']:8.1f} ~ {s['npv_high']:8.1f}")
        rows.append({"type": "sensitivity", "name": s["param"], "npv": s["base_npv"],
                     "npv_low": s["npv_low"], "npv_high": s["npv_high"]})
    keys = sorted({k for r in rows for k in r})
    with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    print(f"已生成 {OUT}")


if __name__ == "__main__":
    main()
