from pathlib import Path

import pytest
from pydantic import ValidationError

from hpc_ai.settings import Settings


def test_environment_overrides_dotenv(monkeypatch):
    Path(".env").write_text("HPC_AI_PORT=8100\nHPC_AI_LOG_LEVEL=debug\n", encoding="utf-8")
    monkeypatch.setenv("HPC_AI_PORT", "8200")

    settings = Settings()

    assert settings.port == 8200
    assert settings.log_level == "debug"
    assert settings.host == "127.0.0.1"


@pytest.mark.parametrize("port", ["0", "65536", "not-a-number"])
def test_invalid_server_port_is_rejected(monkeypatch, port):
    monkeypatch.setenv("HPC_AI_PORT", port)

    with pytest.raises(ValidationError):
        Settings()
