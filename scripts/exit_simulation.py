"""
退出机制模拟器 v2026.1
功能：并购/退出溢价的 IRR 模拟。
  给定初始投资估值、退出时的溢价比例、持有年限（及可选的期间现金流），
  计算内部收益率(IRR)、MOIC(资本回报倍数)与年化收益。
依赖：仅标准库 + numpy（numpy 不可用时用二分法自实现 IRR，保证可运行）。
输出：reports/exit_simulation.csv
"""
import os
import sys

# Windows 控制台默认非 UTF-8，中文输出会 UnicodeEncodeError
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = "reports/exit_simulation.csv"


def irr(cashflows, guess=0.1):
    """计算一组现金流的 IRR。

    cashflows[0] 通常为负(投资流出)，之后为流入。
    优先用 numpy 的多项式求根；不可用时退化为二分法。
    """
    try:
        import numpy as np

        # IRR 是 NPV(rate)=0 的根；用多项式求根取实数、合理区间内的解
        coeffs = cashflows[::-1]
        roots = np.roots(coeffs)
        real = [r.real for r in roots if abs(r.imag) < 1e-6 and r.real > 0]
        rates = [1.0 / r - 1.0 for r in real if r > 0]
        # 取最接近 guess 且落在 (-0.99, 10) 的解
        valid = [x for x in rates if -0.99 < x < 10]
        if valid:
            return min(valid, key=lambda x: abs(x - guess))
    except Exception:
        pass
    return _irr_bisect(cashflows)


def _npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def _irr_bisect(cashflows, low=-0.99, high=10.0, tol=1e-7, max_iter=200):
    """二分法求 IRR，作为无 numpy 时的兜底。"""
    f_low = _npv(low, cashflows)
    f_high = _npv(high, cashflows)
    if f_low * f_high > 0:
        return float("nan")  # 区间内无符号变化，IRR 不存在
    for _ in range(max_iter):
        mid = (low + high) / 2
        f_mid = _npv(mid, cashflows)
        if abs(f_mid) < tol:
            return mid
        if f_low * f_mid < 0:
            high = mid
        else:
            low, f_low = mid, f_mid
    return (low + high) / 2


def simulate(entry_valuation, premium_pct, hold_years, interim_cashflows=None):
    """模拟一次退出。

    entry_valuation: 进入时的投资额(正数)
    premium_pct: 退出相对进入的溢价，如 0.8 表示退出估值 = 进入 * 1.8
    hold_years: 持有年限
    interim_cashflows: 每年期间现金流(如分红)列表，长度应为 hold_years-1 或 None
    返回 dict: irr / moic / annualized
    """
    if entry_valuation <= 0:
        raise ValueError("entry_valuation 必须为正")
    if hold_years < 1:
        raise ValueError("hold_years 必须 >= 1")

    exit_value = entry_valuation * (1 + premium_pct)
    interim = list(interim_cashflows or [])

    # 现金流序列：第 0 年投出，第 1..hold_years-1 年为期间现金流，第 hold_years 年退出。
    flows = [-entry_valuation]
    for year in range(1, hold_years):
        flows.append(interim[year - 1] if year - 1 < len(interim) else 0.0)
    flows.append(exit_value)

    interim_total = sum(interim[:max(0, hold_years - 1)])
    total_in = exit_value + interim_total
    moic = total_in / entry_valuation
    computed_irr = irr(flows)
    annualized = moic ** (1 / hold_years) - 1
    return {
        "entry_valuation": entry_valuation,
        "premium_pct": premium_pct,
        "exit_value": exit_value,
        "hold_years": hold_years,
        "moic": round(moic, 3),
        "irr": round(computed_irr, 4) if computed_irr == computed_irr else None,
        "annualized_return": round(annualized, 4),
    }


def main():
    scenarios = [
        simulate(1000, 0.5, 3),
        simulate(1000, 1.0, 5),
        simulate(1000, 2.0, 7, interim_cashflows=[50, 50, 50, 50, 50, 50]),
    ]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    import csv

    with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(scenarios[0].keys()))
        writer.writeheader()
        writer.writerows(scenarios)
    print("退出情景模拟：")
    for s in scenarios:
        print(f"  投资{s['entry_valuation']} 溢价{s['premium_pct']:.0%} 持有{s['hold_years']}年"
              f" → MOIC {s['moic']}x, IRR {s['irr']}, 年化 {s['annualized_return']:.2%}")
    print(f"已生成 {OUT}")


if __name__ == "__main__":
    main()
