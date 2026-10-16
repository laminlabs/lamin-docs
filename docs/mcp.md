# MCP

This page documents the Model Context Protocol (MCP) server for LaminHub.

MCP connects AI applications to LaminHub so they can retrieve and manage data
in a LaminDB instance on behalf of the authenticated user.

:::{warning}
MCP support is experimental. Tools and behavior may change before a stable
release.
:::


## Connect

Configure your MCP client with the hosted HTTP endpoint and a Lamin JWT. For
example:

```json
{
  "mcpServers": {
    "laminhub": {
      "type": "http",
      "url": "https://lamin.ai/api/mcp",
      "headers": {
        "Authorization": "Bearer <lamin-jwt>"
      }
    }
  }
}
```

Replace `<lamin-jwt>` with a JWT obtained from your Lamin API key. 
See {doc}`Authentication <hub/authentication>` for how to obtain a JWT.

Because Lamin JWTs expire, obtain a new one from your API key when needed.

### Connect Codex

In Codex, select **Plugins → MCP → Add → Add Custom MCP Server**. Give the
server a name, such as `laminhub`, enter
`https://lamin.ai/api/mcp`, and select **No Authentication**.

Then add the MCP server for your LaminHub deployment to
`~/.codex/config.toml`:

```toml
[mcp_servers.laminhub]
url = "https://lamin.ai/api/mcp"
bearer_token_env_var = "LAMIN_ACCESS_TOKEN"
```

Set `LAMIN_ACCESS_TOKEN` to your Lamin JWT, then restart Codex from the
same shell so it inherits the environment variable. For example, on macOS:

```bash
export LAMIN_ACCESS_TOKEN="<lamin-jwt>"
open -a Codex
```

### Connect GitHub Copilot

In GitHub Copilot, select **Customize → MCP → + Add Server**. Enter
`https://lamin.ai/api/mcp`.
Select **HTTP** as the transport, then add the header:

```text
Authorization: Bearer <lamin-jwt>
```

Replace `<lamin-jwt>` with your Lamin JWT.

