# Integrations

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

## Storage systems

Read & write support - create an [instance](setup), register and slice [data](arrays):

- Amazon S3
- Google Cloud Storage

Read-only support:

- Hugging Face Hub:
  `ln.Artifact("hf://datasets/org/repo/data")`
- http / https:
  `ln.Artifact("https://some-site.com/some.data")`

## Array stores

- `tiledbsoma`: [inhouse guide](scrna-tiledbsoma) or [cellxgene](cellxgene)
- [DuckDB](rxrx)

## Visualization tools

- [Vitessce](vitessce)

## ELN systems

- Sync schema and data from your Benchling registries within our team/enterprise plan. [Reach out](https://lamin.ai/contact) to learn more!
