# Integrations

## Data storage

Read & write:

- Local file systems
- AWS S3
- S3-compatible storage services, e.g., MinIO & Cloudflare R2
- Google Cloud Storage

Read only:

- http/https: `ln.Artifact("https://some-site.com/some.data")`
- HuggingFace: `ln.Artifact("hf://datasets/org/repo/data")`

## Schema modules

- [bionty](/bionty): Basic biological entities, with easy import from >20 public ontologies
- [wetlab](/wetlab): Basic wetlab entities
- [clinicore](/clinicore): Basic clinical entities
- [omop](https://omop.lamin.ai): OMOP Common Data Model

## Git

Sync tracked scripts in lamindb with git commits: [guide](track.ipynb#sync-scripts-with-git)

## ML Ops & frameworks

- [Weights & Biases](wandb)
- [MLflow](mlflow)
- Hugging Face paths are supported: `ln.Artifact("hf://datasets/laminlabs/repo/sharded_parquet")`
- [scVI](https://docs.scvi-tools.org/en/latest/tutorials/notebooks/use_cases/custom_dl/lamin.html)

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
