from fastapi.testclient import TestClient

from hpc_ai.app import create_app


def test_service_starts_without_provider_credentials(monkeypatch):
    for name in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "HUGGING_FACE_HUB_TOKEN"):
        monkeypatch.delenv(name, raising=False)

    with TestClient(create_app()) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "hpc-ai"}
