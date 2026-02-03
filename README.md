# ProjectSight-mcp

MCP server generated from OpenAPI. Exposes selected endpoints as tools, plus resources and prompts.

## Install

```bash
uv sync
# or: pip install -e .
```

## Configure

Copy `.env.example` to `.env` and set:

- `API_ACCESS_TOKEN`
- `OPENAPI_BASE_URL`

## Run

**Streamable HTTP** (default):

```bash
uv run python main.py
```

Server runs at `http://127.0.0.1:8000/mcp`. Works behind ngrok or other tunnels.

**Stdio** (e.g. Cursor):

```bash
uv run python main.py stdio
```

## Tools, resources, prompts

- **Tools**: One tool per selected API endpoint (see OpenAPI spec).
- **Resources**: `api-spec://openapi`, `endpoint-list://selected`.
- **Prompts**: Static templates for list projects, create change order, show assignments.
