Any LaminDB instance comes with an underlying SQL metadata database to organize files, folders, and arrays across any number of storage locations.

The following detailed specs are for the Python package `lamindb`. For the analogous R package `laminr`, see the [R docs](https://laminr.lamin.ai).

**Manage data & metadata with a unified API (“lakehouse”).**

- Query & search across data & metadata: {class}`~lamindb.core.Record.filter`, {class}`~lamindb.core.Record.search`
- Model important entities as an {term}`ORM` which their own metadata registry: {class}`~lamindb.core.Record`
- Model files and folders as datasets & models via one class: {class}`~lamindb.Artifact`
- Slice large array stores: {class}`~lamindb.Artifact.open` → [guide](cellxgene)
- Cache & load artifacts: {class}`~lamindb.Artifact.cache`, {class}`~lamindb.Artifact.load`
- Manage features & labels: {class}`~lamindb.Feature`, {class}`~lamindb.FeatureSet`, {class}`~lamindb.ULabel`
- Plug-in custom [schemas](/schemas) & manage schema migrations
- Use array formats in memory & storage: [DataFrame](/tutorial), [AnnData](/arrays), [MuData](multimodal), [SOMA](cellxgene), ... backed by [parquet](/tutorial), [zarr](/arrays), [TileDB](cellxgene), [HDF5](/arrays), [h5ad](/arrays), [DuckDB](rxrx), ...
- Create iterable collections of artifacts with data loaders: {class}`~lamindb.Collection`
- Version artifacts, collections & transforms: {class}`~lamindb.core.IsVersioned`

**Track data lineage across notebooks, scripts, pipelines & UI.**

- Track run context with a simple method call: {meth}`~lamindb.core.Context.track`
- A unified registry for all your notebooks, scripts & pipelines: {class}`~lamindb.Transform`
- A unified registry for all data transformation runs: {class}`~lamindb.Run`
- Manage execution reports, source code and Python environments for [notebooks & scripts](/track)
- Integrate with workflow managers: [redun](redun), [nextflow](nextflow), [snakemake](snakemake)

**Manage registries for experimental metadata & in-house ontologies, import public ontologies.**

- Use >20 public ontologies with plug-in {mod}`bionty`: {class}`~bionty.Gene`, {class}`~bionty.Protein`, {class}`~bionty.CellMarker`, {class}`~bionty.ExperimentalFactor`, {class}`~bionty.CellType`, {class}`~bionty.CellLine`, {class}`~bionty.Tissue`, ...
- Safeguards against typos & duplications
- Version ontology

**Validate, standardize & annotate.**

- Validate & standardize metadata: {class}`~lamindb.core.CanCurate.validate`, {class}`~lamindb.core.CanCurate.standardize`.
- High-level curation flow including annotation: {class}`~lamindb.Curator`
- Inspect validation failures: {class}`~lamindb.core.CanCurate.inspect`

**Organize and share data across a mesh of LaminDB instances.**

- Create & load instances like git repos: `lamin init` & `lamin load`
- Zero-copy [transfer](/transfer) data across instances

**Integrate with analytics tools.**

- Vitessce: {class}`~lamindb.integrations.save_vitessce_config`

**Zero lock-in, scalable, auditable.**

- Zero lock-in: LaminDB runs on generic backends server-side and is _not_ a client for "Lamin Cloud"
  - Flexible storage backends (local, S3, GCP, anything [fsspec](https://github.com/fsspec) supports)
  - Two SQL backends for managing metadata: SQLite & Postgres
- Scalable: metadata registries support 100s of millions of entries, storage is as scalable as S3
- Auditable: data & metadata records are hashed, timestamped, and attributed to users (full audit log to come)
- [Secure](access): embedded in your infrastructure (Lamin has no access to your data & metadata)
- Tested, typed, [idempotent](faq/idempotency) & [ACID](faq/acid)
