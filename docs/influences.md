# Influences

```{note}

This page is, for now, just a stub.

```

Lamin was influenced by many projects. Here we will attempt to attribute them.

## Workflow managers

Lamin complements workflow managers with its focus on interactive analyses, biological entities & provenance beyond deterministic workflows (app uploads & notebooks).

We encourage using a workflow manager to manage scheduling, execution, error & parameter handling of workflows, and tracking successful executions with LaminDB for full provenance tracking. For a great recent perspective, see [AracadiaScience23](https://research.arcadiascience.com/pub/perspective-reproducible-workflows/release/3).

:::{dropdown} How can I integrate workflow manager outputs?

See:

- {doc}`/redun`
- {doc}`/nextflow`
- {doc}`/snakemake`

:::

### redun

Despite Lamin's different scope, the workflow manager [redun](https://github.com/insitro/redun) greatly influenced LaminDB. In particular, naming choices in LaminDB's `File` class (`.hash`, `.stage()`) & hashing strategies for sets are inspired by redun's File class.

Similar to redun, Lamin tries to achieve idempotency but for different use cases & using largely differing designs.

Like redun & git, LaminDB is a distributed system in which any LaminDB instance can exchange & share data with any other LaminDB instance: see {doc}`/transfer`.

LaminDB hasn't consciously been influenced by other workflow managers.

## Biological entities

In LaminDB, ontologies are used to standardize & validate metadata based on plug-in {mod}`lnschema_bionty`. It wraps common public ontologies for which Lamin caches curated assets on S3 for robust availability.

We're not aware of another tool that focuses on leveraging ontologies for curation & validation, but there exist several tools that extend & harmonize ontologies for building knowledge graphs. We list two of them below.

LaminDB does not attempt to create a knowledge graph but assumes that associations between entities are mainly found through experimentation, statistics & machine learning.

Also within LaminDB, connections between entities can be mapped through the pathway entity and by using enrichment tools or by defining relations between biological entities in custom schema. Some relations might be added to `lnschema_bionty` in the future.

### BioLink

[BioLink](https://biolink.github.io/biolink-model/) is a data model to integrate data from various sources in knowledge graphs. It provides a structured way to represent biological entities, their attributes, and the relationships between them.

It is primarily a schema in YAML syntax that can be translated into various formats. It does not provide tooling to access generated knowledge graphs.

### Biocypher

[Biocypher](https://biocypher.org/) is a Python package that simplifies the creation of knowledge graphs.

Built upon a modular framework, it enables users to manipulate and harmonize ontologies.

### bioregistry

[bioregistry](https://bioregistry.io/) is an open-source registry that provides access to curated ontologies with standardized metadata. Bionty uses bioregistry-standardized prefixes as the key for reference sources.

### gget

[gget](https://github.com/pachterlab/gget) provides a simple, intuitive API to query existing web servers of genomic databases.

With [bionty](https://lamin.ai/docs/bionty), Lamin provides a similar tool with three important differences:

- Bionty focuses on leveraging public ontologies for data management (validation, standardization, annotation) rather than queries. In comparison to gget, Bionty's queries are more limited.
- To enable robust & performant access for usage in data pipelines that bulk-validate, -standardize, or -annotate, Lamin hosts versioned ontologies on AWS S3 instead of relying on the sometimes flaky availability of existing public web servers.
- Bionty can be plugged into LaminDB to easily import records from public ontologies into biological registries, managed in a simple database.
