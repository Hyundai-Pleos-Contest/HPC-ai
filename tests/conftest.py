import os

import pytest


@pytest.fixture(autouse=True)
def isolate_settings(monkeypatch: pytest.MonkeyPatch, tmp_path):
    """Do not let a developer's local .env or environment change the test result."""
    monkeypatch.chdir(tmp_path)
    for key in os.environ:
        if key.upper().startswith("HPC_AI_"):
            monkeypatch.delenv(key)
