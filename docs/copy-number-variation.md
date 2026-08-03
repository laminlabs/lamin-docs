# Copy-number variation

Agentic variant analysis of the [1000 Genomes Project](https://www.internationalgenome.org/) — VCF → Parquet curation under a schema contract, then Polars / DuckDB / PyArrow queries and agent-tracked genomic-band analyses.

Write-up: [Agentic variant analysis of the 1000 Genomes Project](https://blog.lamin.ai/1000genomes)

**Instance:** [laminlabs/1000genomes](https://lamin.ai/laminlabs/1000genomes) · **Projects:** [Lakehouse benchmarks](https://lamin.ai/laminlabs/1000genomes/project/huN5V4kDfDQT) · [Agentic workflows](https://lamin.ai/laminlabs/1000genomes/project/xSomr73bTHWK)

## Datasets

| #   | Collection                                                                                                  | Variants             | Files | Ingest                                                                        | Schema                                                                   |
| --- | ----------------------------------------------------------------------------------------------------------- | -------------------- | ----- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 1   | [DRAGEN CNVs (per individual)](https://lamin.ai/laminlabs/1000genomes/collection/Lh6IsCOGIl5TOjAj0000)      | 4.86M CNVs           | 3,201 | [notebook](https://lamin.ai/laminlabs/1000genomes/transform/dqmJBREmxYSV0003) | [schema](https://lamin.ai/laminlabs/1000genomes/schema/sDIFphiVrdJRQDXB) |
| 2   | [SHAPEIT2 Phase 3 (per chromosome)](https://lamin.ai/laminlabs/1000genomes/collection/hVu9puwdRGskm1I60000) | 88M CNVs/SNVs/indels | 26    | [notebook](https://lamin.ai/laminlabs/1000genomes/transform/VcYcsRVR74Sm0000) | [schema](https://lamin.ai/laminlabs/1000genomes/schema/us6vnu91oS5xNMpl) |

## Query benchmarks

| Engine            | Notebook                                                                                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Polars            | [analysis/polars.ipynb](https://lamin.ai/laminlabs/1000genomes/transform/2Wdo02w0MDgH0008)                                                                                         |
| DuckDB            | [analysis/duckdb.ipynb](https://lamin.ai/laminlabs/1000genomes/transform/tQaG9uhSD7BO0006)                                                                                         |
| PyArrow           | [analysis/pyarrow.ipynb](https://lamin.ai/laminlabs/1000genomes/transform/D10UPamv70IP000C)                                                                                        |
| Iceberg / LanceDB | [iceberg](https://lamin.ai/laminlabs/1000genomes/transform/wnVO8cu0qtOP0007) · [lancedb](https://lamin.ai/laminlabs/1000genomes/transform/WtZF9OX9v3uM0008)                        |
| Plots             | [plot_benchmark.py](https://lamin.ai/laminlabs/1000genomes/transform/0BTaXwKDZVRM000N) · [lakehouse comparison](https://lamin.ai/laminlabs/1000genomes/transform/882Pv8r1HdBz0003) |

## Agent analyses

Example task: count variants in a genomic band (chr1:150–200 Mb) — raw Parquet files vs. collection schema contract ([blog Fig. 1](https://blog.lamin.ai/1000genomes)).

| Approach       | Script                                                                                      | Agent run                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Via collection | [count_variants_band.py](https://lamin.ai/laminlabs/1000genomes/transform/X4viXPeYaUL90000) | [run](https://lamin.ai/laminlabs/1000genomes/transform/SnfuhjObaAKR0000/ydgt2ApOZ41szGwv) |
| Via raw files  | [count_chr1_band.py](https://lamin.ai/laminlabs/1000genomes/transform/4hanQjMg7hpk0000)     | [run](https://lamin.ai/laminlabs/1000genomes/transform/SnfuhjObaAKR0000/JglGIr0IRE4BFM4y) |
