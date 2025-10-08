
## 2025-09-29

New Features

- Runs
  - Run list is now filterable by user: click a user in “Ran by” to apply a created_by.handle filter; a “Filtered by …” badge appears with a one‑click clear action. List and Grid views are available, with “Show all runs/Show less” controls and a hint for “newer runs available.” The table shows UID (copyable), Parameters, Status, Input/Output counts, Duration, and Started (time + user), and highlights the latest run.
- Transforms
  - Added an inline type toggle above the run table to quickly scope to All, Notebooks, Pipelines, Functions, or Scripts. The selection syncs with filters and prevents conflicting multi‑selections.
- Analytics & Group‑By
  - Dashboard group‑by gained time‑series binning (Day/Week/Month), a “Show values” toggle for labels on bars, better Y‑axis formatting (e.g., 1.2K), and automatic X‑axis label rotation/margins for long categories. Measure selection respects relations (e.g., counts through back‑relations) and keeps charts responsive as you change fields.
- Identity & Access
  - New identity view exposes user email/handle and SSO domain mapping within your organization, scoped to org admins.
  - Access auditability: the system now records who grants access and who creates teams, and ensures users are admins of their own organization by default.
  - Organization members have read‑only access out of the box; managers and members see organization tabs by role.
- Performance & Caching
  - Instance caching backed by Valkey/Redis speeds up instance lookups. Cache keys are per‑instance and expire automatically (default 1h). Admins can GET current cache content or DELETE to invalidate via `/cache/instances/{instance_id}`.
- Storage
  - Adding an external S3 bucket now includes the API URL and supports temporary session tokens, improving success across different deployments.

Changes

- Navigation & Layout
  - Unified top navigation with an overflow “More” menu; consistent layout across registries. The active main tab stays highlighted while you hover its submenu, and submenu hover behavior is smooth and predictable.
  - Lineage graph styling refined for clearer visuals.
  - Language selector on the landing page keeps a stable width.
  - Removed the in‑UI code link to Lamin docs from source view to reduce clutter.
- Transform & Runs Browsing
  - Transform list gains first‑class filters (projects, ULabels, type, created_by) with a dedicated filter bar and 100‑row paging tuned for browsing.
- API & Routing
  - Routes no longer require `schema_id` in instance endpoints; permissions were simplified behind the scenes with no change to user workflows.
  - DB server identifier updated to `db_server_name` (no action needed from users).
- Ownership & Governance
  - An internal trigger keeps instance ownership and admin access in sync when ownership changes.
- Platform
  - UI upgraded to Svelte 5, bringing snappier interactions and a more consistent component model.

Bug fixes

- Lineage no longer shows artifacts as children under collections; parent/child runs render correctly around artifacts.
- Transform detail loads reliably without getting stuck; “Transform → Pipelines” linkage opens the correct context.
- Migrations/lineage graphs render without errors.
- Main nav button remains active while its submenu is open; submenu no longer collapses when moving the pointer between a tab and its flyout.
- Schema view scrolling works smoothly for long lists.
- Advanced filtering no longer crashes when a search starts with a dot; default filters behave consistently.
- Version parsing is robust to non‑decimal formats.
- Queries disambiguate newly added `created_by` fields to avoid collisions.
- Transfer‑ownership flow works end‑to‑end and reflects immediately in the UI.
- On‑prem documentation links point to the correct destination.
- Artifact detailed view correctly handles Record‑typed fields.
- Stale data issues reduced in lists; views update more consistently.
- Adding a new S3 bucket includes the API URL so bucket permissions apply correctly.

## 2025-09-15

New Features

- Sheets:
  - Use your own preprogrammed transform function templates to generate records and import into the current Sheet via a guided form to streamline data loading.
  - Sheets can now be selected as an input for Lamin Workflows
  - Record imports now auto‑create missing related entities
- Pipeline Launch:
  - Launch parameters tied to a sheet schema now surface an inline sheet editor so you can create fresh sheets or tweak existing ones
  - Storage locations now show a loading indicator while data loads.
- Buckets/Storage: Add a managed S3 bucket using a temporary session token (backend + UI).
- Access & Roles: New “Organization Guest” role for view‑only collaborators.

Changes

- Backend upgraded to lamindb 1.11 with unified soft‑delete semantics for safer deletion.
- Default filters no longer bloat the URL.
- Workflows
  - The run_name field is more prominent to reduce confusion.
  - Clearer error message if fetching a workflow schema fails.
- Access Management UI: Cleaner layout and alphabetical sorting for easier scanning.
- Consistent sidebar and a unified name dropdown across registries.
- RLS functions set search_path explicitly for more reliable permission enforcement.
- Internal trigger keeps access_instance data in sync, improving access lists.
- Stability: Central client logic refactored; legacy collaborator routers and obsolete auth‑context removed.
- Removed `schema_id` parameter from API routers

Bug fixes

- fix: Small tables show exact, stable counts in Instance statistics
- fix: List‑typed fields parse, render, and filter correctly in tables and forms.
- fix: Transform sidebar behaves correctly on direct vs. external navigation; no unexpected sidebar on reload/back.
- fix: Bulk row edits save reliably; batch updates no longer fail due to unsupported SQL RETURNING.
- fix: Linked features display even when a dataset has none of its own; no empty/blank panel.
- fix: Show workflow table controls when collapsed.
- fix: Transform pages load without a sidebar flicker.
- fix: API key creation and usage enforce the correct length; valid keys work consistently.
- fix: Deleting links between records works more reliably and reflects immediately in the UI.
- Saving sheet schema settings no longer resets the configuration panel, and option descriptions stay narrow enough that sheet names remain readable.
- Moving the pointer between registry tabs and their flyout menus no longer collapses the submenu.
- Validation badges call out specific rows and features with issues, and CSV imports respect required fields.
