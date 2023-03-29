# Architecture

- Lamin's high-level API is currently Python only but might include other languages in the future.
- On a lower level, data is stored in SQL databases and otherwise language-independent storage formats.

## LaminDB

[LaminDB](https://lamin.ai/docs) provides the core API.

## Standalone modules

Two data modules can be used standalone.

[nbproject](https://lamin.ai/docs/nbproject): Manage Jupyter notebooks. Open-source ELN for the drylab.

- Manage notebooks with metadata, dependency, and integrity tracking.
- Sketch pipelines and share reproducible notebooks with context.
- Track data flow in and out of notebooks.

[Bionty](https://lamin.ai/docs/bionty): Manage biological entities.

- Lookup & curate metadata based on scientific standards.
- Access biological knowledge without the timeouts of many existing REST endpoints.

## Open-sourced data modules

Below follow Python packages behind [LaminDB](https://lamin.ai/docs).

[Reach out](https://lamin.ai/contact) for non-listed closed-source extensions and maintenance of an enterprise data platform.
