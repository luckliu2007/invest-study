"""让 tests 能直接 import scripts/ 下的模块。"""
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import pytest


@pytest.fixture(autouse=True)
def _offline(monkeypatch):
    """测试默认离线：本机装了 akshare 时也不联网，结果可复现。需要联网路径的用例自行 delenv。"""
    monkeypatch.setenv("INVEST_OFFLINE", "1")
