**Access data & metadata across storage (files, arrays) & database (SQL) backends.**

- Query & search: {class}`~lamindb.core.Registry.filter`, {class}`~lamindb.core.Registry.search`
- Cache, load & stream artifacts: {class}`~lamindb.Artifact.cache`, {class}`~lamindb.Artifact.load`, {class}`~lamindb.Artifact.backed`
- Manage {class}`~lamindb.Feature`, {class}`~lamindb.FeatureSet`, {class}`~lamindb.ULabel`
- Plug-in custom [schemas](/schemas) & manage schema migrations
- Use array formats in memory & storage: [DataFrame](/tutorial), [AnnData](/data), [MuData](multimodal), [SOMA](cellxgene), ... backed by [parquet](/tutorial), [zarr](/data), [TileDB](cellxgene), [HDF5](/data), [h5ad](/data), [DuckDB](rxrx), ...
- Create iterable collections of artifacts: {class}`~lamindb.Artifact`, {class}`~lamindb.Collection`
- Use PyTorch data loaders: {meth}`~lamindb.Collection.mapped`
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

- Use a high-level annotation & validation flow: {class}`~lamindb.Annotate`
- Inspect validation failures: {class}`~lamindb.core.CanValidate.inspect`
- Annotate with features & labels: {class}`~lamindb.core.FeatureManager`
- Save data & metadata ACID: {class}`~lamindb.Artifact.save`

**Organize and share data across a mesh of LaminDB instances.**

- Create & load instances like git repos: `lamin init` & `lamin load`
- Zero-copy [transfer](/transfer) data across instances

**Integrate with analytics tools.**

- Vitessce: {class}`~lamindb.integrations.save_vitessce_config`

**Zero lock-in, scalable, auditable, access management, and more.**

- Zero lock-in: LaminDB runs on generic backends server-side and is not a client for "Lamin Cloud"
  - Flexible storage backends (local, S3, GCP, anything [fsspec](https://github.com/fsspec) supports)
  - Two SQL backends for managing metadata: SQLite & Postgres
- Scalable: registries support 100s of millions of entries
- Auditable: data & metadata records are hashed, timestamped, and attributed to users (full audit log to come)
- [Access](access) management:
  - High-level access management through Lamin's collaborator roles
  - Fine-grained access management via storage & SQL roles
- [Secure](access): embedded in your infrastructure (Lamin has no access to your data & metadata)
- Tested & typed (up to Django Model fields)
- [Idempotent](faq/idempotency) & [ACID](faq/acid)
