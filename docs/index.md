# Overview

Start [here](/guide/index)!

For more background, read up on the key [problems](problems) we work towards resolving or browse Lamin's [data modules](modules).

**Basic components**

- **[LaminDB](guide/index)**. Core Python API that manages storage and SQL databases. Contains `SQLModel`-based [schema](lamindb.schema) for tracking generic data (`DObject`, `DFolder`, `Pipeline`, `Notebook`, `Run`, `User`, `Storage`, etc.).
- **[Lamin CLI](setup/index)**. CLI for setting up LaminDB instances.
- **[lnschema-bionty](https://lamin.ai/docs/lnschema-bionty)**. `SQLModel`-based schema defining basic biological entities (`Gene`, `Protein`, `Tissue`, etc.).
- **[nbproject](https://lamin.ai/docs/nbproject)**. Python API for managing Jupyter notebooks.
- **[Bionty](https://lamin.ai/docs/bionty)**. Python API for defining biological entities based on knowledge.

```{toctree}
:maxdepth: 1
:hidden:

guide/index
api
setup/index
faq/index
modules
glossary
problems
changelog
```
