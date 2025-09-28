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
