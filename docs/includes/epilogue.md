## Design

### World model

1. Teams need to have enough freedom to initiate work independently but enough structure to easily integrate datasets later on
2. Batched datasets ({class}`~lamindb.Artifact`) from physical instruments are transformed ({class}`~lamindb.Transform`) into useful representations
3. Learning needs features ({class}`~lamindb.Feature`, {class}`~bionty.CellMarker`, ...) and labels ({class}`~lamindb.ULabel`, {class}`~bionty.CellLine`, ...)
4. Insights connect dataset representations with experimental metadata and knowledge (ontologies)

### Architecture

LaminDB is a distributed system like git that can be run or hosted anywhere. As infrastructure, you merely need a database (SQLite/Postgres) and a storage location (file system, S3, GCP, HuggingFace, ...).

You can easily create your new local instance:

::::{tab-set}
:::{tab-item} Shell

```bash
lamin init --storage ./my-data-folder
```

:::
:::{tab-item} Python

```python
import lamindb as ln
ln.setup.init(storage="./my-data-folder")
```

:::
::::

Or you can let collaborators connect to a cloud-hosted instance:

::::{tab-set}
:::{tab-item} Shell

```bash
lamin connect account-handle/instance-name
```

:::
:::{tab-item} Python

```python
import lamindb as ln
ln.connect("account-handle/instance-name")
```

:::
:::{tab-item} R

```R
library(laminr)
ln <- connect("account-handle/instance-name")
```

:::
::::

For learning more about how to create & host LaminDB instances on distributed infrastructure, see {doc}`setup`. LaminDB instances work standalone but can optionally be managed by LaminHub. For an architecture diagram of LaminHub, [reach out](https://lamin.ai/contact)!

### Database schema & API

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/XoTQFCmmj2uU4d2xyj9u.png" width="350px" style="background: transparent" align="right">

LaminDB provides a SQL schema for common metadata entities: {class}`~lamindb.Artifact`, {class}`~lamindb.Collection`, {class}`~lamindb.Transform`, {class}`~lamindb.Feature`, {class}`~lamindb.ULabel` etc. - see the [API reference](/api) or the [source code](https://github.com/laminlabs/lnschema-core/blob/main/lnschema_core/models.py).

The core metadata schema is extendable through modules (see green vs. red entities in **graphic**), e.g., with basic biological ({class}`~bionty.Gene`, {class}`~bionty.Protein`, {class}`~bionty.CellLine`, etc.) & operational entities (`Biosample`, `Techsample`, `Treatment`, etc.).

```{dropdown} What is the metadata schema language?

Data models are defined in Python using the Django ORM. Django translates them to SQL tables.
[Django](https://github.com/django/django) is one of the most-used & highly-starred projects on GitHub (~1M dependents, ~73k stars) and has been robustly maintained for 15 years.

```

On top of the metadata schema, LaminDB is a Python API that models datasets as artifacts, abstracts over storage & database access, data transformations, and (biological) ontologies.

Note that the schemas of datasets (e.g., `.parquet` files, `.h5ad` arrays, etc.) are modeled through the `Feature` registry and do not require migrations to be updated.

### Custom registries

LaminDB can be extended with registry modules building on the [Django](https://github.com/django/django) ecosystem. Examples are:

- [bionty](./bionty): Registries for basic biological entities, coupled to public ontologies.
- [wetlab](https://github.com/laminlabs/wetlab): Registries for samples, treatments, etc.

If you'd like to create your own module:

1. Create a git repository with registries similar to [wetlab](https://github.com/laminlabs/wetlab)
2. Create & deploy migrations via `lamin migrate create` and `lamin migrate deploy`

### Repositories

LaminDB and its plugins consist in open-source Python libraries & publicly hosted metadata assets:

- [lamindb](https://github.com/laminlabs/lamindb): Core package.
- [bionty](https://github.com/laminlabs/bionty): Registries for basic biological entities, coupled to public ontologies.
- [wetlab](https://github.com/laminlabs/wetlab): Registries for samples, treatments, etc.
- [usecases](https://github.com/laminlabs/lamin-usecases): Use cases as visible on the docs.

All immediate dependencies are available as git submodules [here](https://github.com/laminlabs/lamindb/tree/main/sub), for instance,

- [lamindb-setup](https://github.com/laminlabs/lamindb-setup): Setup & configure LaminDB.
- [lamin-cli](https://github.com/laminlabs/lamin-cli): CLI for `lamindb` and `lamindb-setup`.

For a comprehensive list of open-sourced software, browse our [GitHub account](https://github.com/laminlabs).

- [lamin-utils](https://github.com/laminlabs/lamin-utils): Generic utilities, e.g., a logger.
- [readfcs](https://github.com/laminlabs/readfcs): FCS artifact reader.
- [nbproject](https://github.com/laminlabs/readfcs): Light-weight Jupyter notebook tracker.
- [bionty-assets](https://github.com/laminlabs/bionty-assets): Assets for public biological ontologies.

LaminHub is not open-sourced.

### Influences

LaminDB was influenced by many other projects, see {doc}`docs:influences`.
