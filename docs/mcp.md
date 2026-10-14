# MCP

This page documents the Model Context Protocol (MCP) server for LaminHub.

MCP connects AI applications to LaminHub so they can retrieve and manage data
in a LaminDB instance on behalf of the authenticated user.

:::{warning}
MCP support is experimental. Tools and behavior may change before a stable
release.
:::

## Available tools

The server currently provides the following tools. Tool availability and the
data returned depend on the authenticated user's permissions.

| Tool | Description |
| --- | --- |
| `attach_label` | Attach a label to a record. |
| `batch_delete_records` | Delete multiple records. |
| `create_artifact` | Register an artifact from an existing storage path. |
| `create_records` | Create records. |
| `create_transform` | Create a transform in an instance. |
| `delete_record` | Delete a record. |
| `detach_label` | Remove a label from a record. |
| `execute_function` | Run a registered function for a transform. |
| `export_record` | Export a record and its related records. |
| `get_artifact_by_path` | Retrieve artifact metadata for a storage path. |
| `get_caller_account` | Retrieve the authenticated user's account. |
| `get_record` | Retrieve a record by ID or UID. |
| `get_records` | Query records from a model. |
| `get_relation_counts` | Return relation counts for a record. |
| `get_relations` | List models related to a schema model. |
| `get_relatives` | Query hierarchical relatives of records. |
| `get_schema` | Discover instance models or inspect a model's schema. |
| `get_values` | Query values for a model field. |
| `group_by` | Aggregate records by selected dimensions. |
| `list_instance_spaces` | List spaces attached to an instance. |
| `list_instances` | List instances available to the authenticated user. |
| `merge_branch` | Merge one branch into another. |
| `query_features` | Query features linked to records. |
| `register_form` | Register a form on an instance. |
| `update_records` | Update existing records. |

## Connect

Configure your MCP client with the hosted HTTP endpoint and a Lamin JWT. For
example:

```json
{
  "mcpServers": {
    "laminhub": {
      "type": "http",
      "url": "https://<laminhub-domain>/api/mcp",
      "headers": {
        "Authorization": "Bearer <lamin-jwt>"
      }
    }
  }
}
```

Replace `<laminhub-domain>` with the domain for your deployment and
`<lamin-jwt>` with a JWT obtained from your Lamin API key. See
{doc}`Authentication <hub/authentication>` for how to obtain a JWT.

Because Lamin JWTs expire, obtain a new one from your API key when needed.

### Connect Codex

In Codex, select **Plugins → MCP → Add → Add Custom MCP Server**. Give the
server a name, such as `laminhub`, enter
`https://<laminhub-domain>/api/mcp`, and select **No Authentication**.

Then add the MCP server for your LaminHub deployment to
`~/.codex/config.toml`:

```toml
[mcp_servers.laminhub]
url = "https://<laminhub-domain>/api/mcp"
bearer_token_env_var = "LAMIN_ACCESS_TOKEN"
```

Replace `<laminhub-domain>` with the domain for your deployment, as described
above. Set `LAMIN_ACCESS_TOKEN` to your Lamin JWT, then restart Codex from the
same shell so it inherits the environment variable. For example, on macOS:

```bash
export LAMIN_ACCESS_TOKEN="<lamin-jwt>"
open -a Codex
```

### Connect GitHub Copilot

In GitHub Copilot, select **Customize → MCP → + Add Server**. Enter
`https://<laminhub-domain>/api/mcp`, replacing `<laminhub-domain>` with the
domain for your deployment. Select **HTTP** as the transport, then add this
header:

```text
Authorization: Bearer <lamin-jwt>
```

Replace `<lamin-jwt>` with your Lamin JWT.
