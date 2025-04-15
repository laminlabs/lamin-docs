# Integrations

## Data storage

Read & write:

- Local file systems
- Amazon S3
- S3 Compatible Storages (such as MinIO)
- Google Cloud Storage

Read only:

- http/https: `ln.Artifact("https://some-site.com/some.data")`
- HuggingFace: `ln.Artifact("hf://datasets/org/repo/data")`

## Schema modules

Additional registries can be found here:

- [bionty](/bionty): Basic biological entities, coupled to public ontologies
- [wetlab](/wetlab): Basic wetlab entities
- [clinicore](/clinicore): Basic clinical entities
- [omop](https://omop.lamin.ai): OMOP Common Data Model

Please [reach out](https://lamin.ai/contact) to have your schema module featured.

## Git

Sync tracked scripts in lamindb with git commits: [guide](track.ipynb#sync-scripts-with-git)

## MLOps

- [Weights & Biases](wandb)
- [MLflow](mlflow)
- Hugging Face paths are supported: `ln.Artifact("hf://datasets/laminlabs/repo/sharded_parquet")`

## Workflow managers

- [redun](redun)
- [Nextflow](nextflow)
- [Snakemake](snakemake)

## Array stores

- `tiledbsoma`: [inhouse guide](scrna-tiledbsoma) or [cellxgene](cellxgene)
- [DuckDB](rxrx)

## Visualization tools

- [Vitessce](vitessce)

## ELN systems

- Sync schema and data from your Benchling registries within our team/enterprise plan. [Reach out](https://lamin.ai/contact) to learn more!
