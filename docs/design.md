# Design & architecture

LaminDB is a distributed system like git that can be run or hosted anywhere. It only needs a SQLite or Postgres database and a storage location (file system, S3, GCP, HuggingFace, ...).

You can easily create your new local instance:

::::{tab-set}
:::{tab-item} Shell

```bash
lamin init --storage ./mydir
```

:::
:::{tab-item} Py
:sync: python

```python
import lamindb as ln
ln.setup.init(storage="./mydir")
```

:::
:::{tab-item} R
:sync: r

```R
library(laminr)
lamin_init(storage="./mydir")
```

:::
::::

Or you can let collaborators connect to a cloud-hosted instance:

::::{tab-set}
:::{tab-item} Shell

```bash
lamin connect account/instance
```

:::
:::{tab-item} Py
:sync: python

```python
import lamindb as ln
ln.connect("account/instance")
```

:::
:::{tab-item} R
:sync: r

```R
library(laminr)
ln <- import_module("lamindb")
ln <- ln$connect("account/instance")
```

:::
::::

For learning more about how to create & host LaminDB instances, see {doc}`setup`. LaminDB instances work standalone but can optionally be managed by LaminHub. For an architecture diagram of LaminHub, [reach out](https://lamin.ai/contact)!

## Database schema & API

LaminDB provides a SQL schema for common metadata entities: {class}`~lamindb.Artifact`, {class}`~lamindb.Collection`, {class}`~lamindb.Transform`, {class}`~lamindb.Feature`, {class}`~lamindb.ULabel` etc. - see the [API reference](/api) or the [source code](https://github.com/laminlabs/lamindb/tree/main/lamindb/models).

The core metadata schema is extendable through modules, e.g., with basic biological ({class}`~bionty.Gene`, {class}`~bionty.Protein`, {class}`~bionty.CellLine`, etc.) & operational entities (`Biosample`, `Techsample`, `Treatment`, etc.).

Data models are defined in Python using the Django ORM. Django translates them to SQL tables.
[Django](https://github.com/django/django) is one of the most-used & highly-starred projects on GitHub (~1M dependents, ~73k stars) and has been robustly maintained for 15 years.
While the SQLAlchemy ORM has some advantages, Django is the most popular choice for building metadata management systems in the life sciences.

On top of the metadata schema, LaminDB is a Python API that models datasets as artifacts, abstracts storage & database access, data transformations, and ontologies.

## Modules

LaminDB can be extended with modules building on the [Django](https://github.com/django/django) ecosystem. Examples are:

- [bionty](./bionty): Registries for basic biological entities, coupled to public ontologies.
- [wetlab](https://github.com/laminlabs/wetlab): Registries for samples, treatments, etc.

If you'd like to create your own module:

1. Create a git repository with registries similar to [wetlab](https://github.com/laminlabs/wetlab)
2. Create & deploy migrations via `lamin migrate create` and `lamin migrate deploy`

For more information, see {doc}`setup`.

## Repositories

LaminDB and its plugins consist in open-source Python libraries & publicly hosted metadata assets:

- [lamindb](https://github.com/laminlabs/lamindb): Core package.
- [bionty](https://github.com/laminlabs/bionty): Registries for basic biological entities, coupled to public ontologies.
- [wetlab](https://github.com/laminlabs/wetlab): Registries for samples, treatments, etc.
- [usecases](https://github.com/laminlabs/lamin-usecases): Use cases as visible on the docs.

All immediate dependencies and modules are available as git submodules [here](https://github.com/laminlabs/lamindb/tree/main/sub), for instance,

- [lamindb-setup](https://github.com/laminlabs/lamindb-setup): Setup & configure LaminDB.
- [lamin-cli](https://github.com/laminlabs/lamin-cli): CLI for `lamindb` and `lamindb-setup`.

For a comprehensive list of open-sourced software, browse our [GitHub account](https://github.com/laminlabs).

- [lamin-utils](https://github.com/laminlabs/lamin-utils): Generic utilities, e.g., a logger.
- [readfcs](https://github.com/laminlabs/readfcs): FCS artifact reader.
- [nbproject](https://github.com/laminlabs/readfcs): Light-weight Jupyter notebook tracker.
- [bionty-assets](https://github.com/laminlabs/bionty-assets): Assets for public biological ontologies.

LaminHub is not open-sourced.
