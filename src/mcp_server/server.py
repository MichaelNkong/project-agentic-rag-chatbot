"""
MCP Server implementation for Customer Support Chatbot.
Exposes tools for order status, refunds, and tracking.
"""

from fastapi import FastAPI, Request
from pydantic import BaseModel
from enum import Enum
import json
from typing import Any, Dict, List, Optional

from src.mcp_server.tools.rag_query_tool import rag_query_tool


# ============= Tool Schemas =============

class Tool(BaseModel):
    """MCP Tool definition."""
    name: str
    description: str
    input_schema: Dict[str, Any]


class ToolRequest(BaseModel):
    """Request to execute a tool."""
    tool_name: str
    arguments: Dict[str, Any]


class ToolResponse(BaseModel):
    """Response from tool execution."""
    tool_name: str
    status: str
    result: Any
    error: Optional[str] = None


# ============= MCP Server =============

class MCPServer:
    """Model Context Protocol Server for  Internet Search Agent."""

    def __init__(self):
        self.tools: Dict[str, callable] = {}
        self.tool_definitions: Dict[str, Tool] = {}
        self._register_tools()

    def _register_tools(self):
        """Register all available tools."""

        self.register_tool(
            name="rag_query_tool",
            func=rag_query_tool,
            description=(
                "Retrieve information from an internal knowledge base using semantic search. "
                "Returns a JSON object with fields: has_context (boolean), answer (string), and sources (list). "
                "If has_context is false, no relevant information was found."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "User question or search query for the knowledge base"
                    }
                },
                "required": ["query"]
            }
        )


    def register_tool(
        self,
        name: str,
        func: callable,
        description: str,
        input_schema: Dict[str, Any]
    ):
        """Register a tool with the MCP server."""
        self.tools[name] = func
        self.tool_definitions[name] = Tool(
            name=name,
            description=description,
            input_schema=input_schema
        )
        print(f"✓ Registered tool: {name}")

    def get_tools(self) -> List[Dict[str, Any]]:
        """Return list of available tools."""
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema
            }
            for tool in self.tool_definitions.values()
        ]

    def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool and return result."""
        if tool_name not in self.tools:
            return {
                "status": "error",
                "error": f"Tool '{tool_name}' not found"
            }

        try:
            func = self.tools[tool_name]
            result = func(**arguments)
            return {
                "status": "success",
                "result": result
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }


# ============= FastAPI App =============

app = FastAPI(title="MCP Server - Customer Support Chatbot")
mcp_server = MCPServer()


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "server": "MCP Server running"}


@app.get("/tools")
async def list_tools():
    """List all available tools."""
    return {
        "tools": mcp_server.get_tools(),
        "count": len(mcp_server.tools)
    }


@app.post("/execute")
async def execute_tool(request: ToolRequest) -> ToolResponse:
    """Execute a tool with given arguments."""
    result = mcp_server.execute_tool(request.tool_name, request.arguments)
    return ToolResponse(
        tool_name=request.tool_name,
        status=result.get("status", "error"),
        result=result.get("result"),
        error=result.get("error")
    )


@app.post("/tools/{tool_name}")
async def execute_tool_direct(tool_name: str, req: ToolRequest):
    """Direct tool execution endpoint (legacy support)."""
    result = mcp_server.execute_tool(tool_name, req.arguments)
    return {
        "tool": tool_name,
        "status": result.get("status"),
        "result": result.get("result"),
        "error": result.get("error")
    }


# ============= Startup =============

if __name__ == "__main__":
    import uvicorn

    print("=" * 60)
    print("🚀 Starting MCP Server for Question Answering Chatbot")
    print("=" * 60)
    print(f"📋 Registered Tools: {len(mcp_server.tools)}")
    for tool_name in mcp_server.tools.keys():
        print(f"   • {tool_name}")
    print("=" * 60)
    print("API Documentation: http://localhost:5001/docs")
    print("=" * 60)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5001,
        log_level="info"
    )