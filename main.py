"""MCP server entrypoint: FastMCP, streamable-http."""

import sys

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    "ProjectSight-mcp",
    json_response=True,
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

# Register generated tools
from tools.api_tools import register_tools
register_tools(mcp)

@mcp.resource("api-spec://openapi")
def api_spec_resource() -> str:
    import json
    from core import mcp_scaffold_state
    return json.dumps(mcp_scaffold_state.get_spec(), indent=2)

@mcp.resource("endpoint-list://selected")
def endpoint_list_resource() -> str:
    import json
    from core import mcp_scaffold_state
    return json.dumps(mcp_scaffold_state.get_selected_endpoints(), indent=2)


@mcp.prompt()
def list_projects() -> str:
    return "List all projects the user has access to."

@mcp.prompt()
def create_change_order() -> str:
    return "Help the user create a change order."

@mcp.prompt()
def show_open_assignments() -> str:
    return "Show open assignments."


def main() -> None:
    transport = "stdio" if "stdio" in sys.argv else "streamable-http"
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
