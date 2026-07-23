"""sector_screening 的单元测试：重点覆盖无网络/无 akshare 时的降级路径。"""
import pandas as pd
import pytest

import sector_screening as ss


def test_sample_universe_has_required_columns():
    df = ss.sample_universe()
    assert ss.REQUIRED_COLS <= set(df.columns)
    assert len(df) > 0
    # roe/pe 用于因子筛选，示例数据必须带上
    assert {"roe", "pe"} <= set(df.columns)


def test_screen_filters_by_industry_and_factors():
    # 使用内置示例数据（无 akshare 时的默认路径）
    cands = ss.screen(industry="新能源车", roe_min=0.15, pe_max=20)
    assert isinstance(cands, pd.DataFrame)
    # 示例数据里比亚迪 roe=0.16 pe=18 满足；宁德 pe=28 不满足
    assert (cands["industry"].str.contains("新能源车")).all()
    if not cands.empty:
        assert (cands["roe"] > 0.15).all()
        assert (cands["pe"] < 20).all()


def test_screen_empty_when_industry_absent():
    cands = ss.screen(industry="不存在的行业xyz")
    assert cands.empty


def test_load_universe_falls_back_without_akshare(monkeypatch):
    # 强制走无 akshare 分支
    monkeypatch.setattr(ss, "HAVE_AK", False)
    df = ss.load_universe()
    assert ss.REQUIRED_COLS <= set(df.columns)


def test_screen_without_factor_columns():
    """行业列存在但缺 roe/pe 时应仅按行业过滤，不报错。"""
    fake = pd.DataFrame({
        "ticker": ["000001", "000002"],
        "name": ["A", "B"],
        "industry": ["新能源车", "银行"],
    })
    # 通过 monkeypatch 让 load_universe 返回无因子列的数据
    import pytest as _pytest  # noqa
    orig = ss.load_universe
    ss.load_universe = lambda: fake  # type: ignore
    try:
        cands = ss.screen(industry="新能源车")
        assert len(cands) == 1
        assert cands.iloc[0]["industry"] == "新能源车"
    finally:
        ss.load_universe = orig  # type: ignore
