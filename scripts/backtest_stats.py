"""
回测可信度工具 v2026.1
功能：给“试了很多次才挑出来的”回测结果打折——概率夏普比率（PSR）、多次试验下的期望最大夏普、
      折减夏普比率（Deflated Sharpe Ratio, DSR）。
依赖：仅标准库。
用法：python scripts/backtest_stats.py
输出：reports/backtest_stats.csv（论文数值例子在不同试验次数下的 DSR）

方法出处：Bailey & López de Prado (2014), "The Deflated Sharpe Ratio: Correcting for Selection Bias,
Backtest Overfitting and Non-Normality", Journal of Portfolio Management 40(5)。
约定：所有夏普比率都是**单期**（例如日度）口径，不年化；峰度用非超额峰度（正态分布为 3）。
"""
import csv
import math
import os
import statistics
import sys

# Windows 控制台默认非 UTF-8，中文输出会 UnicodeEncodeError
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = "reports/backtest_stats.csv"
EULER_GAMMA = 0.5772156649015329
_N = statistics.NormalDist()

# 论文中的数值例子：日度数据 5 年（T=1250），年化夏普 2.5，做了 100 次独立试验，
# 各次试验年化夏普的方差为 0.5，收益偏度 -3、峰度 10。论文结论：DSR≈0.90，达不到 95% 置信水平。
PAPER_EXAMPLE = {"annual_sr": 2.5, "annual_sr_var": 0.5, "n_obs": 1250, "n_trials": 100,
                 "skew": -3.0, "kurt": 10.0, "periods_per_year": 250}


def sharpe(returns):
    """单期夏普比率（无风险利率按 0，或传入超额收益）。"""
    return statistics.mean(returns) / statistics.stdev(returns)


def skew_kurt(returns):
    """样本偏度与非超额峰度（总体矩口径，正态分布约为 0 和 3）。"""
    n = len(returns)
    m = sum(returns) / n
    m2 = sum((r - m) ** 2 for r in returns) / n
    m3 = sum((r - m) ** 3 for r in returns) / n
    m4 = sum((r - m) ** 4 for r in returns) / n
    return m3 / m2 ** 1.5, m4 / m2 ** 2


def expected_max_sharpe(n_trials, sr_var, sr_mean=0.0):
    """N 次独立试验中，“最好的那个”夏普比率的期望值（论文式 1）。

    即使每次试验都毫无真实收益（sr_mean=0），试得越多，挑出来的最大值也越高。
    """
    if n_trials <= 1:
        return sr_mean
    z = ((1 - EULER_GAMMA) * _N.inv_cdf(1 - 1 / n_trials)
         + EULER_GAMMA * _N.inv_cdf(1 - 1 / (n_trials * math.e)))
    return sr_mean + math.sqrt(sr_var) * z


def probabilistic_sharpe_ratio(sr, sr_benchmark, n_obs, skew=0.0, kurt=3.0):
    """真实夏普比率高于 sr_benchmark 的概率，考虑样本长度、偏度和峰度。"""
    denom = 1 - skew * sr + (kurt - 1) / 4 * sr ** 2
    if denom <= 0:
        raise ValueError("偏度/峰度与夏普比率组合无效：方差项必须为正")
    return _N.cdf((sr - sr_benchmark) * math.sqrt(n_obs - 1) / math.sqrt(denom))


def deflated_sharpe_ratio(sr, n_trials, sr_var, n_obs, skew=0.0, kurt=3.0):
    """把“期望最大夏普”作为门槛的 PSR。习惯上 DSR ≥ 0.95 才算显著。"""
    return probabilistic_sharpe_ratio(sr, expected_max_sharpe(n_trials, sr_var), n_obs, skew, kurt)


def paper_example(n_trials=None, skew=None, kurt=None):
    """按论文数值例子计算，可改试验次数或分布形状，返回单期口径的结果。"""
    p = PAPER_EXAMPLE
    k = p["periods_per_year"]
    sr = p["annual_sr"] / math.sqrt(k)
    sr_var = p["annual_sr_var"] / k
    n = p["n_trials"] if n_trials is None else n_trials
    s = p["skew"] if skew is None else skew
    ku = p["kurt"] if kurt is None else kurt
    sr0 = expected_max_sharpe(n, sr_var)
    return {"n_trials": n, "skew": s, "kurt": ku,
            "sr_annual": p["annual_sr"], "sr0_annual": sr0 * math.sqrt(k),
            "dsr": deflated_sharpe_ratio(sr, n, sr_var, p["n_obs"], s, ku)}


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    print("论文例子：年化夏普 2.5、5 年日度数据、收益偏度 -3、峰度 10")
    rows = []
    for n in (1, 10, 46, 100, 1000):
        for s, ku in ((PAPER_EXAMPLE["skew"], PAPER_EXAMPLE["kurt"]), (0.0, 3.0)):
            r = paper_example(n, s, ku)
            rows.append(r)
            tag = "正态" if s == 0 else "厚尾负偏"
            ok = "显著" if r["dsr"] >= 0.95 else "不显著"
            print(f"  试验 {n:>4} 次（{tag}）：门槛（年化）{r['sr0_annual']:.2f}  DSR {r['dsr']:.4f}  {ok}")
    with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"已生成 {OUT}")


if __name__ == "__main__":
    main()
