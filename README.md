# HPC AI

현대차 Pleos 프로젝트의 선택적 내부 AI 서비스입니다. 현재는 개발 환경과
`GET /health`만 제공합니다. 모델, 프롬프트, 추론 API, 외부 AI 호출은 아직 없습니다.
BE/FE 개발을 위해 이 서버를 항상 실행할 필요는 없습니다.

## 개발 환경

- Python 3.12 (`.python-version`, `pyproject.toml`)
- uv 0.11.26
- FastAPI, Uvicorn, Pydantic Settings
- Ruff, pytest, HTTPX2 (Starlette TestClient)

직접 의존성은 `pyproject.toml`, 전이 의존성과 배포 파일 해시는 `uv.lock`에 고정합니다.
Python 3.12의 패치 버전은 보안 업데이트를 받을 수 있도록 고정하지 않습니다.

## 시작

아래 명령은 모두 이 저장소 루트에서 실행합니다.

```console
uv sync --locked
uv run --locked hpc-ai
```

기본 주소는 `http://127.0.0.1:8000`입니다.

- `GET /health`: `{"status":"ok","service":"hpc-ai"}`
- `/docs`: 개발용 OpenAPI UI

health는 프로세스 생존 여부만 나타냅니다. 모델 준비 여부를 보장하지 않습니다.
외부 API 키나 DB가 없어도 서버와 테스트가 실행됩니다.

선택적으로 `.env.example`을 `.env`로 복사하고 `HPC_AI_HOST`, `HPC_AI_PORT`,
`HPC_AI_LOG_LEVEL`을 변경합니다. Pydantic Settings가 실행 디렉터리의 `.env`를
읽으며, 같은 이름의 프로세스 환경 변수가 `.env`보다 우선합니다. `.env`는 커밋하지 않습니다.

## 검증

```console
uv lock --check
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
```

포맷 수정은 `uv run --locked ruff format .`로 실행합니다.
CI의 `verify` 작업도 위 검사들을 실행하며, 모델 다운로드나 외부 AI 호출은 하지 않습니다.

## 컨테이너

```console
docker build -t hpc-ai:local .
docker run --rm -p 127.0.0.1:8000:8000 hpc-ai:local
```

컨테이너 내부에서는 `0.0.0.0:8000`에서 수신하고 일반 사용자로 실행합니다.
`.env`와 모델 파일은 이미지에 포함하지 않습니다.
통합 실행과 선택적 AI 프로필은 `HPC-workspace`가 관리합니다.

## 작업 규칙

협업·Git Flow·커밋·PR 규칙은 `CONTRIBUTING.md`, AI 작업 지침은 `AGENTS.md`를 따릅니다.
AI 내부 API와 실행 환경은 이 저장소가 소유하며, 사용자 인증·업무 데이터·공개 API는
BE가 담당합니다. 실제 모델이나 외부 제공자 연결은 별도 기능 작업에서 결정합니다.
