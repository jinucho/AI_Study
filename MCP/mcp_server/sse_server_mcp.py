#!/usr/bin/env python3
"""
MCP Server - SSE transport 예제 (간소화 버전)
공식 MCP Python SDK를 사용한 간단한 SSE 기반 MCP 서버
⚠️ 주의: SSE transport는 deprecated되었으며 참고용으로만 사용하세요
"""

from mcp.server.fastmcp import FastMCP

# FastMCP 서버 생성
mcp = FastMCP("sse-simple-server")


@mcp.tool()
def echo(text: str) -> str:
    """입력된 텍스트를 그대로 반환합니다"""
    return f"SSE Echo: {text}"


if __name__ == "__main__":
    print("⚠️  SSE MCP 서버 시작 중...")
    print("⚠️  주의: SSE transport는 deprecated되었습니다")
    print("🌐 서버 URL: http://localhost:8080")
    
    # SSE transport로 서버 실행
    mcp.run(transport="sse", port=8080) 