# Audit log

The audit log provides a history of write events similar to the commit history in git.
They complement data lineage in answering what was changed by whom when on a fine-grained level.

Open a database in the UI and select **Changes → Database writes**.

The newest events are shown first and grouped by date. You can:

- filter by space, branch, event type, table, user, or date range
- sort events
- group consecutive events that affect the same record
- open the affected record when a link is available

<div align="center">
<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/Afygpvnvlkyc1ezM0000.png" style="margin: 1%;"/>
</div>

Events are read-only and their visibility follows is governed by the database {doc}`permissions`.
