# Audit log

The audit log provides a history of database write events, similar to a git commit history.
It complements data lineage by answering what was changed, by whom, and when, at a fine-grained level.

To browse the audit log, open a database in the UI and select **Changes → Database writes**.
The newest events are shown first and grouped by date. You can:

- filter by space, branch, event type, table, user, or date range
- sort events
- group consecutive events that affect the same record
- open the affected record when a link is available

<div align="center">
<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/Afygpvnvlkyc1ezM0000.png" style="margin: 1%;"/>
</div>

Events are read-only and their visibility is governed by a user's access permissions to the database.

## Additional logs (Preview)

Database administrators can open **Logs** to review:

- **Permissions:** database, space, and team access changes associated with the instance.
- **REST:** REST API requests associated with the instance.
- **MCP:** MCP tool calls associated with the instance.
- **Storage:** S3 object activity where audit collection is configured.

REST and MCP logs do not include direct SQL reads. Storage auditing covers configured S3 buckets, not Google Cloud Storage or local files. Authentication events are logged internally but are not yet available as customer sign-in history.

REST, MCP, and storage views update daily. **Logs received on (UTC)** selects the day logs were received, which can differ from the event date. Recent activity may not appear yet.

Database administrators can retrieve REST, MCP, and storage events through the API; see {doc}`rest`. For review exports or retention requirements, contact [security@lamin.ai](mailto:security@lamin.ai). Available history depends on the log source and deployment.
