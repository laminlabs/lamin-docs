# Pipelines

Pipelines (sometimes also called workflows) in bioinformatics encompass structured sequences of computational tools that manipulate, visualize, and potentially interpret biological data, orchestrating a coherent analytical framework.
Their significance lies in automating intricate data processing procedures, ensuring rigorous standardization, reproducibility, and scalability in bioinformatics, thereby expediting scientific discovery.
Prominent workflow managers such as Snakemake, Nextflow, and Redun offer advanced tools for orchestrating, executing, and overseeing the execution of these pipelines, addressing challenges related to version control, collaborative research efforts, and efficient resource utilization.
Lamin enables tracking of pipeline execution including metadata such as name or version.
Moreover, it tracks data lineage as it flows through pipelines and validates output against biological registries and ontologies.

The following notebooks entail example runs of various workflow managers and their interaction with Lamin.

```{toctree}
:maxdepth: 1

../redun
../nextflow
```
