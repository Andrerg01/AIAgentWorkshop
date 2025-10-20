"""
my_mcp_functions.py
-------------------

Utility module for interacting with an MCP (Michelin Cloud Platform) server
through LangChain MCP Adapters.

This module provides helper functions to:
  • List available MCP tools for a given token.
  • Call (invoke) a specific MCP tool asynchronously.

It includes network configuration workarounds required inside the Michelin
corporate network environment, ensuring trusted certificate usage and
compatibility with internal HTTPS endpoints.
"""

import os
import truststore
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools


# === STEP 1: NETWORK CONFIGURATION ===
# Some corporate environments (like Michelin’s) define SSL-related environment
# variables that can interfere with custom certificate handling.
# We remove them here so `truststore` can properly inject the system CA bundle.
for k in ("SSL_CERT_FILE", "SSL_CERT_DIR", "REQUESTS_CA_BUNDLE"):
    os.environ.pop(k, None)

# Inject the OS trust store (corporate root CAs, etc.) into Python’s SSL context.
truststore.inject_into_ssl()


# === STEP 2: MCP CONNECTION CONFIGURATION ===
# These constants define the MCP endpoint and access credentials.
# Replace TOKEN with a valid bearer token for your environment when deploying.
MCP_URL = "https://dev.d0s.michelin.com/projects/goaats_mcp/v1/mcp"
TOKEN = "dev-token-change-me"


# === STEP 3: ASYNC HELPER FUNCTIONS ===

async def list_tools():
    """
    Retrieve all tools available on the configured MCP server.

    This function:
      • Establishes a client connection to the MCP server.
      • Creates a session using the active token.
      • Loads and returns all discoverable tools for that connection.

    Returns:
        list[Tool]: A list of `Tool` objects, each describing a callable MCP tool.
    """
    # Create an MCP client with one logical connection named "server"
    client = MultiServerMCPClient(
        connections={
            "server": {
                "url": MCP_URL,
                "transport": "streamable_http",  # Enables SSE-like streaming responses
                "headers": {"Authorization": f"Bearer {TOKEN}"},
            }
        }
    )

    # Open a session context for the MCP server
    async with client.session("server") as session:
        # Load all tools registered with this connection
        tools = await load_mcp_tools(session)
        return tools


async def call_tool(name: str, arguments: dict):
    """
    Invoke a specific MCP tool by name with the given arguments.

    Args:
        name (str): The name of the MCP tool to call (must match a tool’s `name`).
        arguments (dict): Parameters to pass to the tool.

    Returns:
        Any: The tool’s response, or an error string if the tool is not found.
    """
    # Initialize client connection (same configuration as list_tools)
    client = MultiServerMCPClient(
        connections={
            "server": {
                "url": MCP_URL,
                "transport": "streamable_http",
                "headers": {"Authorization": f"Bearer {TOKEN}"},
            }
        }
    )

    # Open a session with the MCP server
    async with client.session("server") as session:
        # Fetch the available tools for this session
        tools = await load_mcp_tools(session)

        # Attempt to find the requested tool by name
        tool = next((t for t in tools if t.name == name), None)

        if not tool:
            # Return an error message listing available tool names for convenience
            available = [t.name for t in tools]
            return f"Tool {name!r} not found. Available tools: {available}"

        # Execute the selected tool asynchronously and return the result
        return await tool.ainvoke(arguments)
