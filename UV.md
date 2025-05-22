# UV를 이용한 파이썬 개발환경 구축 및 관리

- 작성자 : [Jinu Cho](https://github.com/jinucho)
- 작성일자 : 2025-05-22
- UV version : 0.7.6(2025-05-19)

## Description : 
- UV 특징 : pip보다 빠르고 더 안정적인 의존성 관리를 제공
- 이 문서는 UV를 사용하여 파이썬 개발환경을 구축하고 관리하는 방법을 설명 합니다.
- 작성일자 : 2025-05-22

## Table of Contents
- [UV 설치](#uv-설치)
- [UV 초기화](#uv-초기화)
- [커널 생성](#커널-생성)
- [주요 명령어](#주요-명령어)
- [참고 글](#참고-글)

## UV 설치

UV는 Rust로 작성되어 있으며, 다양한 방법으로 설치할 수 있습니다.

### macOS에서 설치
```bash
brew install uv
```

### 다른 OS에서 설치
```bash
pip install uv
```

또는 공식 GitHub 저장소의 지침을 따를 수 있습니다:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


## UV 초기화
```bash
uv init <디렉토리 명>
```

혹은 프로젝트를 시작할 디렉토리에서
```bash
uv init
```

초기화 시 생성되는 파일들
- 1. pyproject.toml
    - 프로젝트의 메타데이터와 설정을 저장하는 파일
    ```
    [project]
    name = "my-project"
    version = "0.1.0"
    description = ""
    authors = []
    dependencies = []
    requires-python = ">=3.8"

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [tool.uv]
    # UV 관련 설정
    ```

- 2. .python-version
    - 프로젝트에서 사용할 Python 버전을 지정하는 파일
    ```
    3.11
    ```

- 3. requirements.txt (0.7.6 ver 기준 생성되지 않음)
    - 프로젝트의 의존성 목록
    - 초기에는 비어있음
    - ```uv export --format requirements-txt > requirements.txt``` 로 현재 의존성을 업데이트 함
    - ```uv pip freeze > requirements.txt``` 로 현재 의존성을 업데이트 함(단, uv add --dev 로 설치한 개발용 라이브러리도 저장 됨)

- 4. requirements-dev.txt (0.7.6 ver 기준 생성되지 않음)
    - 개발 환경에서만 필요한 의존성 목록을 저장하는 파일
    - 초기에는 비어있음
    - ```uv export --format requirements-txt --dev > requirements-dev.txt``` 로 업데이트 함

- 5. .venv/ 디렉토리 (0.7.6 ver 기준 생성되지 않음)
    - 가상환경이 생성되는 디렉토리
    - Python 인터프리터와 설치된 패키지들이 저장 됨
    - 주요 하위 디렉토리:
        - bin/ (Unix) 또는 Scripts/ (Window): 실행 파일들이 위치
        - lib/ : 설치된 패키지들이 위치
        - include/ : C확장 모듈 헤더 파일들이 위치

- 6. uv.lock (0.7.6 ver 기준 생성되지 않음)
    - 의존성의 정확한 버전을 잠그는 파일
    - ```uv lock``` 명령으로 생성/업데이트 됨
    - 예시:
        ```
        [package]
        requests = "2.31.0"
        numpy = "1.24.0"
        ```

## 커널 생성
주피터 노트북을 위한 커널 생성
```bash
uv add --dev ipykernel
```

## 주요 명령어

| 명령어 | 설명 |
|--------|------|
| `uv init` | 새 프로젝트 초기화 (pyproject.toml 생성) |
| `uv venv` | 새 가상환경 생성 |
| `uv pip install <패키지명>` | 패키지 설치 |
| `uv pip install -r requirements.txt` | requirements.txt에서 패키지 설치 |
| `uv pip list` | 설치된 패키지 목록 확인 |
| `uv pip uninstall <패키지명>` | 패키지 제거 |
| `uv add <패키지명>` | 프로젝트에 의존성 추가 |
| `uv add --dev <패키지명>` | 개발용 의존성 추가 |
| `uv remove <패키지명>` | 프로젝트에서 의존성 제거 |
| `uv sync` | pyproject.toml 기반으로 의존성 설치 |
| `uv lock` | 의존성 락 파일 생성 |
| `uv show` | 프로젝트 의존성 구조 표시 |
| `uv tree` | 의존성 트리 확인 |

- uv add 사용이 권장되는 경우:
    - 프로젝트의 의존성을 체계적으로 관리할 때
    - 개발 의존성과 프로덕션 의존성을 구분해야 할 때
    - 의존성 버전을 명시적으로 관리해야 할 때
    - 팀 프로젝트에서 의존성을 공유해야 할 때
- uv pip install 사용이 권장되는 경우:
    - 일회성 패키지 설치가 필요할 때
    - 임시로 패키지를 테스트할 때
    - pip 명령어와의 호환성이 필요할 때
    - 의존성 목록 관리가 필요 없을 때


## 참고 글
- [DEVOCEAN KIDO](https://devocean.sk.com/blog/techBoardDetail.do?ID=167420&boardType=techBlog)

- [Medium Sigrid Jin](https://sigridjin.medium.com/파이썬-개발자라면-uv-를-사용합시다-546d523f7178)