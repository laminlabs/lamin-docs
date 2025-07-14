The Python & R packages `lamindb` & `laminr` share _almost_ the same API (`.` → `$`).

**Manage data & metadata with a unified API (“lakehouse”).**

- Use a built-in SQLite/Postgres database to organize files, folders & arrays across any number of storage locations
- Query & search across data & metadata: {class}`~lamindb.models.SQLRecord.filter`, {class}`~lamindb.models.SQLRecord.search`
- Model entities via registries based on the Django {term}`ORM`: {class}`~lamindb.models.SQLRecord`
- Model files and folders as datasets & models: {class}`~lamindb.Artifact`
- Slice large array stores: {class}`~lamindb.Artifact.open` → [guide](cellxgene)
- Cache & load artifacts: {class}`~lamindb.Artifact.cache`, {class}`~lamindb.Artifact.load`
- Manage features & labels: {class}`~lamindb.Feature`, {class}`~lamindb.Schema`, {class}`~lamindb.ULabel`, {class}`~bionty.Gene`, {class}`~bionty.Protein`, {class}`~bionty.CellType`, {class}`~bionty.CellLine`, ...
- Use array formats in memory & storage: DataFrame, [AnnData](/arrays), [MuData](multimodal), [tiledbsoma](cellxgene), ... backed by parquet, [zarr](/arrays), [tiledb](cellxgene), [HDF5](/arrays), [h5ad](/arrays), [DuckDB](rxrx), ...
- Create iterable & queryable collections of artifacts with data loaders: {class}`~lamindb.Collection`
- Version artifacts, collections & transforms: {class}`~lamindb.models.IsVersioned`

**Track data lineage across notebooks, scripts, pipelines & UI.**

- Track scripts & notebooks with a simple method call: {meth}`~lamindb.track`
- Track functions with a decorator: {meth}`~lamindb.tracked`
- A unified registry for all your notebooks, scripts & pipelines: {class}`~lamindb.Transform`
- A unified registry for all data transformation runs: {class}`~lamindb.Run`
- Manage execution reports, source code and Python environments for [notebooks & scripts](/track)
- Integrate with workflow managers: [redun](redun), [nextflow](nextflow), [snakemake](snakemake)

**Manage registries for experimental metadata & in-house ontologies, import public ontologies.**

- Use >20 public ontologies with module {mod}`bionty`: {class}`~bionty.Gene`, {class}`~bionty.Protein`, {class}`~bionty.CellMarker`, {class}`~bionty.ExperimentalFactor`, {class}`~bionty.CellType`, {class}`~bionty.CellLine`, {class}`~bionty.Tissue`, ...
- Use a canonical wetlab database schema module {mod}`wetlab`
- Safeguards against typos & duplications
- Version ontologies and manage their life cycle

**Validate, standardize & annotate.**

- Validate & standardize metadata: {class}`~lamindb.models.CanCurate.validate`, {class}`~lamindb.models.CanCurate.standardize`.
- High-level curation flow including annotation: {class}`~lamindb.Curator`
- Inspect validation failures: {class}`~lamindb.models.CanCurate.inspect`

**Organize and share data across a mesh of LaminDB instances.**

- Create & connect to instances with the same ease as git repos: `lamin init` & `lamin connect`
- Zero-copy [transfer](/transfer) data across instances

**Integrate with analytics tools.**

- Vitessce: {class}`~lamindb.integrations.save_vitessce_config`

**Zero lock-in, scalable, auditable.**

- Zero lock-in: LaminDB runs on generic backends server-side and is _not_ a client for "Lamin Cloud"
  - Flexible storage backends (local, S3, GCP, https, HF, R2, anything [fsspec](https://github.com/fsspec) supports)
  - Two SQL backends for managing metadata: SQLite & Postgres
- Scalable: metadata registries support 100s of millions of entries, storage is as scalable as S3
- Plug-in custom [schema modules](/setup.ipynb#manage-schema-modules) & manage database schema migrations
- Auditable: data & metadata records are hashed, timestamped, and attributed to users (full audit log to come)
- [Secure](access): embedded in your infrastructure
- Tested, typed, [idempotent](faq/idempotency) & [ACID](faq/acid)
