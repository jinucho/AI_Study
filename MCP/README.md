# MCP (Model Context Protocol) 학습 가이드

이 디렉토리는 **MCP(Model Context Protocol)**의 다양한 transport 방식을 이해하고 실습할 수 있는 종합 가이드입니다.

## 📁 디렉토리 구조

```
MCP/
├── README.md
└── mcp_server/                  # transport 별 예제 코드 디렉토리
    ├── stdio_server_mcp.py      # stdio transport 예제
    ├── sse_server_mcp.py        # SSE transport 예제 (Deprecated)
    └── streamable_http_server_mcp.py # streamable-http transport 예제 (권장)
```

## 📖 1. MCP Transport 방식 이론

### 1.1 stdio (기본)
- **개요**: 로컬 프로세스 간 `stdin/stdout`을 통해 통신
- **장점**: 간단하고 설정이 쉬움, 별도 네트워크 통신 불필요
- **단점**: 로컬에서만 사용 가능, 원격 클라이언트와의 통신 불가
- **사용 사례**: 로컬 개발, 데스크톱 애플리케이션

### 1.2 sse (Deprecated)
- **개요**: HTTP 기반 SSE(Server‑Sent Events)를 이용한 실시간 데이터 스트리밍
- **장점**: 서버에서 실시간 메시지 푸쉬 가능, 설정이 비교적 단순
- **단점**: 단방향(서버 → 클라이언트) 통신만 가능, 확장성 문제
- **상태**: ⚠️ **Deprecated** - 새 프로젝트에서 사용 금지

### 1.3 streamable-http (신규 권장)
- **개요**: HTTP 기반 단일 endpoint를 통해 POST 요청과 SSE 스트리밍을 동시에 지원
- **동작 방식**: `/mcp` endpoint를 통해 POST 요청 수신, 필요 시 SSE로 응답 스트리밍
- **장점**: 완전한 양방향 통신, Stateless 서버 구현 가능, 단일 endpoint 구조
- **사용 사례**: 웹 서비스, 클라우드 환경, 원격 서버

### 1.4 비교표

| Transport | 통신 방식 | Endpoint 수 | 양방향 통신 | 상태 관리 | 스트리밍 지원 | 현재 권장 |
|-----------|-----------|-------------|-------------|-----------|---------------|-----------|
| **stdio** | stdio | 1 | ✅ (로컬) | 로컬 프로세스 | ❌ | ○ |
| **sse** | HTTP POST + SSE | 2 | ❌ | Stateful 필요 | ✅ | ⚠ Deprecated |
| **streamable-http** | HTTP POST + optional SSE | 1 | ✅ | Stateless 가능 | ✅ | ✅ 권장 |

---

## 🎯 2. 핵심 포인트

### 2.1 Transport 선택 기준

| 상황 | 권장 Transport | 이유 |
|------|---------------|------|
| 로컬 개발/테스트 | stdio | 설정 간단, 네트워크 불필요 |
| 웹 서비스 | streamable-http | 양방향 통신, 확장성 |
| 레거시 시스템 | sse | 기존 코드 호환성 (단, 마이그레이션 권장) |

### 2.2 구현 특징

- **stdio**: JSON-RPC 메시지를 stdin/stdout으로 직접 교환
- **sse**: HTTP POST로 요청, SSE로 응답 스트리밍
- **streamable-http**: 단일 endpoint에서 POST 요청과 선택적 SSE 응답

### 2.3 보안 고려사항

- **stdio**: 로컬 환경에서만 사용, 프로세스 격리 중요
- **streamable-http**: CORS 설정, HTTPS 바인딩, Origin 검증 필요
- **공통**: 입력 검증, 에러 처리, 로깅

---

## 📚 3. 참고 자료

### 공식 문서
- [MCP 공식 문서](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP 가이드](https://modelcontextprotocol.io/quickstart)

### 추가 학습
- [JSON-RPC 2.0 스펙](https://www.jsonrpc.org/specification)
- [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)