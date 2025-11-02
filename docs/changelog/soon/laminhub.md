## 2025-10-31 (0.40.0)

New Features

- Features & Datasets
  - Composite feature sets can now expand inline to reveal all features without leaving the page.

Changes

- Features & Datasets
  - Feature set links are derived more robustly from their type and safely fall back to the features index when unknown, and non‑string feature values are rendered clearly.
  - Related-label badges and filters use the correct display field from the feature type for accurate names and filtering.
- Access Management
  - Adding spaces, instances, or teams uses a unified search picker that filters out invalid or duplicate entries and excludes the default team, with consistent name sorting across lists and tables.
  - Logging out now also ends the server session to avoid lingering authentication state.
- Access & Security
  - Reading link tables enforces access based on the related records for more consistent, least‑privilege behavior.

Bug fixes

- Features & Datasets
  - Prevent errors when rendering feature sets with invalid type strings by handling unsupported types gracefully and indicating them in the UI.
  - Search and selection menus no longer show entries with empty names, avoiding selection glitches.

## 2025-10-29 (0.39.0)

Changes

- Database & Migrations
  - Database migrations are more robust by ensuring required admin permissions for constraint visibility and automatically cleaning up legacy tables that could otherwise interfere with installing security policies.

## 2025-10-29 (0.38.0)

Changes

- Platform & Observability
  - Error reporting environments are now consistent between server and client and tracing covers additional enterprise domains, improving the accuracy of diagnostics across deployments.

## 2025-10-29 (0.37.0)

New Features

- Storage & Buckets
  - S3 bucket permission setup and instance creation now associate buckets with your organization, record the creator, and accept optional bucket settings when creating or linking a bucket.
- Debug & Ops
  - A new debug endpoint is available to inspect the active database engine cache for troubleshooting.

Changes

- Access & Error Handling
  - API errors are standardized with consistent HTTP status codes and clearer messages across resources, including 400 for invalid queries, 403 for permission denials, 404 for missing or inaccessible records, and 409 for uniqueness conflicts.
  - Unauthorized responses return a generic message in production while remaining descriptive in non-production to avoid leaking details.
- Tables & UI
  - Artifact table feature chips use schema-defined display fields for linked registries, improving label text and link targets.

Bug fixes

- Tables & UI
  - The artifact feature panel now shows a clear inline error when it fails, preventing broken cells in the table.

## 2025-10-28 (0.36.0)

Changes

- Access & Security
  - Organization admins can manage domains, and platform superadmins can manage all domains.
  - Instance administrators can view selected system data that was previously hidden.
- Navigation & UI
  - The lineage label on detail pages is shortened from “Data lineage” to “Lineage”.
  - In run lists, the “Parameters” column is renamed to “Features”.

Bug fixes

- Teams & Collaborators
  - Team member and space collaborator lists filter out accounts or teams that are no longer part of the organization to avoid empty rows and sorting errors.
- Sheets
  - The “No type” view shows existing records when available instead of rendering an empty table.
- Query & Filters
  - Filters based on the number of related items handle zero correctly and apply greater/less-than comparisons consistently.

## 2025-10-27 (0.35.0)

New Features

- Workflows & Launch
  - You can now add or edit a sheet row directly within the “Select or add row” dialog when choosing run metadata, without leaving the launch flow.

Changes

- Workflows & Launch
  - Numeric parameters in Nextflow launch forms are automatically treated as numbers in the JSON view for more accurate parameter typing.
- Sheets Editor
  - Row selection tables hide internal ID columns by default for a cleaner, more focused view.
- Performance & Stability
  - Caching reachability checks are memoized to reduce overhead and improve stability.

Bug fixes

- Sheets Editor
  - Prevent an error when rendering row selectors if a row lacks record metadata.

## 2025-10-26 (0.34.0)

New Features

- Records & Search
  - You can search across related fields (e.g., transform or label attributes) in tables and value pickers, with results ordered by relevance.
- Workflows & Launch
  - Launch forms respect hidden parameters defined in Nextflow schemas and provide a toggle to reveal hidden sections when needed.
- Administration
  - Administrators can trigger instance migrations via the API to apply database and hub updates.

Changes

- Navigation & UI
  - The footer now shows the Hub version and deployment date derived from the latest tag for clearer release identification.
- Feature Labels & DTypes
  - Dtype parsing supports hyphenated registry subtype names and labels render more consistently (including list types) with refined spacing and clearer messages.
- Records & Search
  - When a search query is used, sorting is suppressed so results are shown by relevance.
- Transforms
  - The transform list defaults to newest-first and seeds sensible defaults even when URL syncing is disabled.
- Detail Views
  - Structured feature values render as formatted JSON on detail pages for readability.
- Access & Teams
  - Space and Team rows display member counts when available, with visibility aligned to admin and manager roles.

Bug fixes

- Records & Search
  - Relation searches apply the correct joins for many-to-many paths and deduplicate matches, and filtering by relation counts works as expected.
- Storage & Artifacts
  - Large directory uploads are more reliable in serverless environments by reducing concurrency to avoid out-of-memory errors.
- Access & Governance
  - Transferring instance ownership now also grants the new individual owner admin access to the instance.
- Sheets
  - Numeric entries for float/number features are preserved as numbers instead of being coerced to strings.


## 2025-10-22

New Features

- Workflows & Launch
  - Launch forms can reveal hidden parameters when needed, a simplified launch view is available, and Nextflow schema JSON is respected end‑to‑end. Run metadata originating from Sheets is captured for better traceability.
- Transforms & Pipelines
  - Pipeline repository information is automatically derived from transform source code to improve provenance and linking.
  - Branch parameter is supported when resolving repository details for transforms.
- Analytics & Group‑By
  - Group‑by charts support sorting for clearer comparisons.
- Access & Security
  - Record‑level locking via RLS for individual records and Block models.
- Storage
  - Default bucket lookup by instance ID is available; deletion of storage resources is supported; and Lambda now returns IDs for newly created artifacts and storages.

Changes

- Runs & Reports
  - Run logs render ANSI colors for readability; version tags no longer auto‑prepend “v”; run counters increment per transform (not per version) for clearer numbering.
- Navigation & UI
  - Registries nav reordered; sub‑navigation expanded for Artifacts and Features; Sheets show feature descriptions on hover; hide internal “n” in schema tables; assorted copy/title refinements.
  - Team page copy/typos corrected; vocabulary renamed “linked features” → “external features”.
- Workflows & Pipelines
  - Only main‑branch schemas appear in pipeline configuration; configuration files are hidden by default; `input`/`outdir` receive no special treatment so the Nextflow schema is the single source of truth.
  - Parameters show a loading state during launch configuration.
- Performance & Stability
  - Instance caching optimized with a robust fallback.
- Platform & Observability
  - LaminDB upgraded to 1.12 with follow‑up bumps; database resource metadata expanded (host/port/proxy) and schema SQL functions marked STABLE.
- Permissions & Governance
  - Expanded permissions for org admins/managers; more consistent JWT/DB user mapping for org members.

Bug fixes

- Sheets
  - Normalize floats on submission; restore Save after manual import; hide non‑schema self‑referential features; correct feature‑card dtype display and field‑search scope; fix sheet creation button in schema.
- Pipelines & Transforms
  - Resolve transform load errors; pipeline configuration shows only main‑branch schemas; use the correct `name_field`; full‑screen run report no longer flashes.
- Storage & Artifacts
  - Include file extension when uploading artifacts; improve reliability of instance DB transfer.
- Navigation & Tables
  - Fix nav flicker and active‑page highlight; correct org‑page navbar links; table selector uses fuzzy search; access table command bars use the correct accessor keys; remove description column from ULabel tables; fix artifacts page reactivity issues.
- Database & Query
  - Fix collaborator‑access RLS and JWT DB‑user retrieval for org members.

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
