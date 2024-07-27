**Manage data & metadata with a unified Python API (“lakehouse”).**

Manage storage (files, folders, arrays) and a SQL database (SQLite, Postgres) backend.

- Query & search across artifacts ({class}`~lamindb.Artifact`) & metadata records ({class}`~lamindb.core.Record`): {class}`~lamindb.core.Record.filter`, {class}`~lamindb.core.Record.search`
- Query large array stores like CellXGene Census: {class}`~lamindb.Artifact.open` → [guide](/query-census)
- Cache artifacts on disk & load them into memory: {class}`~lamindb.Artifact.cache`, {class}`~lamindb.Artifact.load`
- Manage machine learning entities: {class}`~lamindb.Feature`, {class}`~lamindb.FeatureSet`, {class}`~lamindb.ULabel`
- Plug-in custom [schemas](/schemas) & manage schema migrations on an equal footing with the LaminDB core entities
- Use array formats in memory & storage: [DataFrame](/tutorial), [AnnData](/arrays), [MuData](multimodal), [SOMA](cellxgene), ... backed by [parquet](/tutorial), [zarr](/arrays), [TileDB](cellxgene), [HDF5](/arrays), [h5ad](/arrays), [DuckDB](rxrx), ...
- Create iterable collections of artifacts & data loaders: {class}`~lamindb.Collection` {meth}`~lamindb.Collection.mapped`
- Version artifacts, collections & transforms: {class}`~lamindb.core.IsVersioned`

**Track data lineage across notebooks, pipelines & UI: {meth}`~lamindb.track`, {class}`~lamindb.Transform` & {class}`~lamindb.Run`.**

- Execution reports, source code and Python environments for [notebooks & scripts](/track)
- Integrate with workflow managers: [redun](redun), [nextflow](nextflow), [snakemake](snakemake)

**Manage registries for experimental metadata & in-house ontologies, import public ontologies.**

- Use >20 public ontologies with plug-in {mod}`bionty`
- {class}`~bionty.Gene`, {class}`~bionty.Protein`, {class}`~bionty.CellMarker`, {class}`~bionty.ExperimentalFactor`, {class}`~bionty.CellType`, {class}`~bionty.CellLine`, {class}`~bionty.Tissue`, ...
- Safeguards against typos & duplications
- Ontology versioning

**Validate, standardize & annotate based on registries: {class}`~lamindb.core.CanValidate.validate` & {class}`~lamindb.core.CanValidate.standardize`.**

- Use a high-level curation flow: {class}`~lamindb.Curate`
- Inspect validation failures: {class}`~lamindb.core.CanValidate.inspect`
- Annotate with features & labels: {class}`~lamindb.core.FeatureManager`
- Save data & metadata ACID: {class}`~lamindb.Artifact.save`

**Organize and share data across a mesh of LaminDB instances.**

- Create & load database instances like git repos: `lamin init` & `lamin load`
- Zero-copy [transfer](/transfer) data across instances

**Integrate with analytics tools.**

- Vitessce: {class}`~lamindb.integrations.save_vitessce_config`

**Zero lock-in, scalable, auditable, access management, and more.**

- Zero lock-in: LaminDB runs on generic backends server-side and is _not_ a client for "Lamin Cloud"
  - Flexible storage backends (local, S3, GCP, anything [fsspec](https://github.com/fsspec) supports)
  - Two SQL backends for managing metadata: SQLite & Postgres
- Scalable: metadata registries support 100s of millions of entries, storage is as scalable as S3
- Auditable: data & metadata records are hashed, timestamped, and attributed to users (full audit log to come)
- [Access](access) management:
  - High-level access management through Lamin's collaborator roles
  - Fine-grained access management via storage & SQL roles
- [Secure](access): embedded in your infrastructure (Lamin has no access to your data & metadata)
- Tested, typed, [idempotent](faq/idempotency) & [ACID](faq/acid)
