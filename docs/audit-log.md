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

Events are read-only and their visibility is governed by a users access permissions to the database.
