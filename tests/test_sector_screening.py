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
    cands = ss.screen(industry="汽车整车", roe_min=0.15, pe_max=20)
    # 示例数据里比亚迪（汽车整车）roe=0.16 pe=18 满足
    assert list(cands["ticker"]) == ["002594"]
    # 宁德时代（电池）pe=28 不满足
    assert ss.screen(industry="电池", roe_min=0.15, pe_max=20).empty


def test_default_industry_is_in_sample_data():
    """默认板块名必须能命中示例数据，否则离线默认运行永远输出空表。"""
    assert ss.INDUSTRY_KEYWORD in set(ss.sample_universe()["industry"])


def test_screen_empty_when_industry_absent():
    cands = ss.screen(industry="不存在的行业xyz")
    assert cands.empty


def test_load_universe_falls_back_without_akshare(monkeypatch):
    # 强制走无 akshare 分支
    monkeypatch.setattr(ss, "HAVE_AK", False)
    df = ss.load_universe()
    assert ss.REQUIRED_COLS <= set(df.columns)


def test_screen_without_factor_columns(monkeypatch):
    """行业列存在但缺 roe/pe 时应仅按行业过滤，不报错。"""
    fake = pd.DataFrame({
        "ticker": ["000001", "000002"],
        "name": ["A", "B"],
        "industry": ["新能源车", "银行"],
    })
    monkeypatch.setattr(ss, "load_universe", lambda *_: fake)
    cands = ss.screen(industry="新能源车")
    assert len(cands) == 1
    assert cands.iloc[0]["industry"] == "新能源车"


class _FakeAk:
    """模拟东方财富行业成分股接口的返回字段（该接口不含 ROE）。"""

    @staticmethod
    def stock_board_industry_cons_em(symbol):
        return pd.DataFrame({
            "序号": [1, 2, 3],
            "代码": ["002594", "601127", "600104"],
            "名称": ["比亚迪", "赛力斯", "上汽集团"],
            "最新价": [260.0, 90.0, 15.0],
            "市盈率-动态": [18.5, "-", 9.2],  # "-" 代表亏损/无数据
        })


def test_load_universe_live_path_maps_eastmoney_columns(monkeypatch):
    monkeypatch.setattr(ss, "HAVE_AK", True)
    monkeypatch.setattr(ss, "ak", _FakeAk, raising=False)
    monkeypatch.delenv("INVEST_OFFLINE", raising=False)
    df = ss.load_universe("汽车整车")
    assert ss.REQUIRED_COLS <= set(df.columns)
    assert (df["industry"] == "汽车整车").all()
    assert pd.isna(df.loc[df["ticker"] == "601127", "pe"]).all()


def test_screen_live_path_filters_by_pe_only(monkeypatch):
    monkeypatch.setattr(ss, "HAVE_AK", True)
    monkeypatch.setattr(ss, "ak", _FakeAk, raising=False)
    monkeypatch.delenv("INVEST_OFFLINE", raising=False)
    cands = ss.screen(industry="汽车整车", pe_max=20)
    # 无 ROE 列时只按 PE 过滤；PE 缺失的赛力斯被剔除
    assert set(cands["ticker"]) == {"002594", "600104"}


def test_offline_env_skips_network(monkeypatch):
    class _Boom:
        @staticmethod
        def stock_board_industry_cons_em(symbol):
            raise AssertionError("INVEST_OFFLINE 时不应联网")

    monkeypatch.setattr(ss, "HAVE_AK", True)
    monkeypatch.setattr(ss, "ak", _Boom, raising=False)
    monkeypatch.setenv("INVEST_OFFLINE", "1")
    assert ss.REQUIRED_COLS <= set(ss.load_universe().columns)
