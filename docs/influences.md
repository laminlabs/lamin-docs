# Influences

```{note}

This page is, for now, just a stub.

```

Lamin was inspired by many projects.
Here, we will attempt to acknowledge those influences and compare our solutions to them.

## Workflow managers

Lamin complements workflow managers with its focus on interactive analyses, biological entities & provenance beyond deterministic workflows (app uploads & notebooks).

We encourage using a workflow manager to manage scheduling, execution, error & parameter handling of workflows, and tracking successful executions with LaminDB for full provenance tracking.
For a great recent perspective, see [AracadiaScience23](https://research.arcadiascience.com/pub/perspective-reproducible-workflows/release/3).

:::{dropdown} How can I integrate workflow manager outputs?

See:

- {doc}`/redun`
- {doc}`/nextflow`
- {doc}`/snakemake`

:::

### redun

Despite Lamin's different scope, the workflow manager [redun](https://github.com/insitro/redun) greatly influenced LaminDB.
In particular, concepts in LaminDB's :class:`Artifact` class (`.hash`, `.cache()` in lamindb ~ `.stage()` in redun) & hashing strategies for sets are inspired by redun's `File` class.
Similar to redun, Lamin tries to achieve idempotency but for different use cases & using largely differing designs.
Like redun & git, LaminDB is a distributed system in which any LaminDB instance can exchange & share data with any other LaminDB instance: see {doc}`/transfer`.

LaminDB hasn't consciously been influenced by other workflow managers.

## Biological entities

Biological ontologies categorize entities such as genes or proteins and their relationships, forming the basis of knowledge graphs that interconnect these entities.
In LaminDB, ontologies are used to standardize and validate metadata through the {mod}`bionty` plug-in, which wraps common public ontologies and caches curated assets on S3 for robust availability.
While we’re unaware of another tool focused on ontology-based curation and validation, several models and tools exist that extend and harmonize ontologies for building knowledge graphs.

LaminDB does not attempt to create a knowledge graph but assumes that associations between entities are mainly found through experimentation, statistics & machine learning.
Also within LaminDB, connections between entities can be mapped through the :class:`~bionty.Pathway` entity or by defining relations between biological entities in a custom schema.

### BioLink

[BioLink](https://biolink.github.io/biolink-model/) is a data model for knowledge graphs which provides a structured way to represent biological entities, their attributes, and the relationships between them.
It is primarily a schema in YAML syntax that can be translated into various formats.
Biolink does not provide tooling to access or manipulate generated knowledge graphs.

### Biocypher

[Biocypher](https://biocypher.org/) is a modular Python framework that simplifies the creation of knowledge graphs using schemas such as BioLink.
It further enables users to manipulate and harmonize ontologies.
The package does not focus on data curation or modeling entities using SQL and is primarily for developers interested in building knowledge graphs.

### bioregistry

[bioregistry](https://bioregistry.io/) is an open-source registry that provides access to curated ontologies with standardized metadata.
Bionty uses bioregistry-standardized prefixes as the key for reference sources.

### gget

[gget](https://github.com/pachterlab/gget) provides a simple, intuitive API to query existing web servers of genomic databases.

With {mod}`bionty`, Lamin provides a similar tool with three important differences:

- Bionty focuses on leveraging public ontologies for data management (validation, standardization, annotation) rather than queries.
  In comparison to gget, Bionty's queries are more limited.
- To enable robust & performant access for usage in data pipelines that bulk-validate, -standardize, or -annotate, Lamin hosts versioned ontologies on AWS S3 instead of relying on the sometimes flaky availability of existing public web servers.
- Bionty can be plugged into LaminDB to easily import records from public ontologies into biological registries, managed in a simple database.
