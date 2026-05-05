"""
MCP Client for testing the MCP Server.
Provides examples of calling each tool.
"""
import requests
import json
from typing import Dict, Any
from enum import Enum
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

class APIEndpoint(str, Enum):
    """API endpoints."""
  
    HEALTH =  os.getenv("BASE_URL", "http://localhost:8000")+"/health"
    TOOLS_LIST = os.getenv("BASE_URL", "http://localhost:8000")+"/tools"
    EXECUTE = os.getenv("BASE_URL", "http://localhost:8000")+"/execute"

 

class MCPClient:
    """Client for interacting with MCP Server."""

    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv("BASE_URL", "http://localhost:5001")
        self.session = requests.Session()

    def health_check(self) -> Dict[str, Any]:
        """Check if MCP server is running."""
        try:
            resp = self.session.get(f"{self.base_url}/health", timeout=5)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"status": "error", "message": f"Server unreachable: {str(e)}"}

    def list_tools(self) -> Dict[str, Any]:
        """Get list of available tools."""
        try:
            resp = self.session.get(f"{self.base_url}/tools", timeout=5)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

    from typing import Dict, Any

    def query_knowledge_base(self, query: str) -> Dict[str, Any]:
        """Retrieve information from the internal knowledge base via MCP."""
        return self._execute_tool("rag_query_tool", {"query": query})



    def _execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool on the MCP server."""
        try:
            payload = {
                "tool_name": tool_name,
                "arguments": arguments
            }
            resp = self.session.post(f"{self.base_url}/execute", json=payload, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.ConnectionError:
            return {
                "status": "error",
                "error": "Cannot connect to MCP server. Is it running on port 5001?"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}


def print_response(title: str, response: Dict[str, Any]):
    """Pretty print a response."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")
    print(json.dumps(response, indent=2, default=str))


def main():
    """Run demo tests against MCP server."""
    print("\n" + "=" * 70)
    print("  🔌 MCP Client - Customer Support Chatbot")
    print("=" * 70)

    client = MCPClient()

    # 1. Health check
    print("\n[1/5] Checking server health...")
    health = client.health_check()
    if health.get("status") == "healthy":
        print("✓ Server is running!")
    else:
        print("✗ Server is not responding. Start it first:")
        print("  python -m mcp_server.server")
        return

    # 2. List tools
    print("\n[2/5] Fetching available tools...")
    tools = client.list_tools()
    print_response("Available Tools", tools)


    print("\n" + "=" * 70)
    print("  ✓ All tests completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
