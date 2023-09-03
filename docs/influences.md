# Influences

Here, we'll try to explain how Lamin was influenced by other projects & tools.

This page is, for now, just a stub.

## Workflow managers: redun

Lamin complements workflow managers with its focus on interactive analyses, biological entities & provenance beyond deterministic workflows (app uploads & notebooks). We encourage using a workflow manager to manage scheduling, execution, error & parameter handling of workflows and integrating successful executions into LaminDB for full provenance tracking.

Despite Lamin's different scope, the workflow manager [redun](https://github.com/insitro/redun) greatly influenced LaminDB. In particular, naming choices in LaminDB's `File` class (`.hash`, `.stage()`) & hashing strategies for sets are inspired by redun's File class.

Similar to redun, Lamin tries to achieve idempotency but for different use cases & using largely differing designs.

Like redun & git, LaminDB is a distributed system in which any LaminDB instance can exchange & share data with any other LaminDB instance. (Currently, this feature is built into the design, but not yet fully implemented.)

LaminDB hasn't knowingly been influenced by other workflow managers.

## Meta-ontologies & knowledge graphs: BioLink & Biocypher

Biological ontologies are structured frameworks that define and categorize biological entities along with the relationships that connect them.

In LaminDB, ontologies are used to standardize & validate metadata based on plug-in {mod}`lnschema_bionty`. The implementation is a wrapper around the common public ontologies, their data deposits & REST APIs, caching assets for robust availability on Lamin-managed S3.

There are numerous efforts to leverage ontologies in the field with different scopes:

- [BioLink](https://biolink.github.io/biolink-model/) is a standardized data model designed to facilitate the integration and query of biological data from various sources in knowledge graphs. It provides a structured way to represent biological entities, their attributes, and the relationships between them, enhancing interoperability in bioinformatics.
  It is primarly a schema in YAML syntax that can be translated into various formats. [BioLink](https://biolink.github.io/biolink-model/) does not provide tooling to access knowledge graphs generated.
- [Biocypher](https://biocypher.org/) is a Python package that simplifies the creation of knowledge graphs.
  Built upon a modular framework, it empowers users to manipulate and harmonize ontologies. Unlike LaminDB, it does not focus on data curation or SQL entities and is primarily for developers interested in building their own knowledge graphs.