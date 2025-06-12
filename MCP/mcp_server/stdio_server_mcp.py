#!/usr/bin/env python3
"""
MCP Server - stdio transport 예제 (간소화 버전)
공식 MCP Python SDK를 사용한 간단한 stdio 기반 MCP 서버
"""

from mcp.server.fastmcp import FastMCP

# FastMCP 서버 생성
mcp = FastMCP("stdio-simple-server")


@mcp.tool()
def echo(text: str) -> str:
    """입력된 텍스트를 그대로 반환합니다"""
    return f"Echo: {text}"


if __name__ == "__main__":
    print("📡 stdio MCP 서버 시작...")
    print("💡 사용법: JSON-RPC 메시지를 stdin으로 입력하세요")
    
    # stdio transport로 서버 실행
    mcp.run(transport="stdio") 