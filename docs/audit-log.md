# Audit log

Audit logs provide a time-ordered history of database writes in LaminDB. They
help answer what changed, who changed it, and when.

## What is recorded

Each audit event identifies:

- the type of change (`INSERT`, `UPDATE`, or `DELETE`)
- the affected table and record
- the time of the change
- the acting user when the write has an authenticated Lamin user context
- the associated space, branch, and run, when applicable

For updates, the audit entry stores the previous values of the fields that
changed. For deletes, it stores the previous record data.

## View the audit log

Open an instance in LaminHub and select **Changes → Database writes**.

The newest events are shown first and grouped by date. You can:

- filter by space, branch, event type, table, user, or date range
- sort events
- group consecutive events that affect the same record
- open the affected record when a link is available

<div align="center">
<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/Afygpvnvlkyc1ezM0000.png" style="margin: 1%;"/>
</div>

## Access control

Audit records are read-only and their visibility follows the instance's {doc}`permissions`. A collaborator can only read events for spaces and records they are allowed to access.
