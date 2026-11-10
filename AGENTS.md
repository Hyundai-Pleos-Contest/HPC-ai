# HPC-ai 작업 지침

## 범위

- Python 3.12와 uv를 사용하는 선택적 내부 AI 서비스다.
- 현재 구현은 서버 실행 설정과 `/health`뿐이다. 모델, 프롬프트, 추론 API는 미정이다.
- API 키, 네트워크 AI 서비스, 모델 다운로드 없이 로컬 실행과 테스트가 가능해야 한다.
- 사용자 인증·업무 데이터·공개 API는 HPC-be, 통합 Compose는 HPC-workspace가 소유한다.

## 협업

- 브랜치·커밋·PR 작업 전 `CONTRIBUTING.md`를 읽는다.
- `AGENTS.md`가 공통 AI 지침 원본이다. `CLAUDE.md`에 내용을 복제하지 않는다.
- 다른 저장소의 계약을 바꾸면 관련 PR과 호환성 영향을 함께 기록한다.
- 작업 범위에 없는 모델·데이터셋·추론 기능을 초기 설정에 추가하지 않는다.

## 명령

저장소 루트에서 실행한다.

- 설치: `uv sync --locked`
- 서버: `uv run --locked hpc-ai` (기본 `127.0.0.1:8000`)
- 의존성 일치: `uv lock --check`
- 린트: `uv run --locked ruff check .`
- 포맷 검사: `uv run --locked ruff format --check .`
- 테스트: `uv run --locked pytest`
- 이미지 빌드: `docker build -t hpc-ai:local .`

## 구현 규칙

- 패키지는 `src/hpc_ai`, 테스트는 `tests`에 둔다.
- 의존성은 uv로 관리하고 `pyproject.toml`과 `uv.lock`을 함께 갱신한다.
- `.env`, 제공자 키, 원본 사용자 데이터, 모델 가중치를 Git에 넣지 않는다.
- `/health`는 생존 상태만 의미한다. 모델 준비 여부와 혼동하지 않는다.
- 외부 AI 연동을 추가할 때는 CI에서 실제 제공자를 호출하지 않도록 테스트 대체물을 둔다.
- 실행하지 않은 검증을 통과했다고 기록하지 않는다.
