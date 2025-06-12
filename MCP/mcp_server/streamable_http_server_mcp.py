#!/usr/bin/env python3
"""
MCP Server - streamable-http transport 예제 (간소화 버전)
공식 MCP Python SDK를 사용한 간단한 streamable-http 기반 MCP 서버 (권장 방식)
"""

from mcp.server.fastmcp import FastMCP

# FastMCP 서버 생성 (stateless HTTP 모드)
mcp = FastMCP("streamable-http-simple-server", stateless_http=True)


@mcp.tool()
def echo(text: str) -> str:
    """입력된 텍스트를 그대로 반환합니다"""
    return f"Streamable HTTP Echo: {text}"


if __name__ == "__main__":
    print("🚀 Streamable HTTP MCP 서버 시작 중...")
    print("📡 MCP endpoint: http://localhost:3000/mcp")
    print("❤️  Health check: http://localhost:3000/health")
    print("🎯 권장 transport 방식입니다!")
    
    # streamable-http transport로 서버 실행
    mcp.run(transport="streamable-http", port=3000) 