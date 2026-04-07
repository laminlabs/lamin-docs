# Integrations

## Storage

Read & write:

- Local file systems
- AWS S3
- S3-compatible storage services, e.g., MinIO & Cloudflare R2
- Google Cloud Storage

Read only:

- http/https: `ln.Artifact("https://a-website.com/a-dataset.txt")`
- [Hugging Face](https://huggingface.co): `ln.Artifact("hf://datasets/org/repo/dataset.parquet")`

## Ontologies & registries

- [bionty](/bionty): Biological ontologies, with easy import from >20 public ontologies
- [pertdb](/pertdb): Registries for perturbations (compounds, biologics, genetic interventions, etc.)

## Git

- auto-sync with `git`: [track guide](track.ipynb#sync-scripts-with-git)

## MLOps

- [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning): {mod}`~lamindb.integrations.lightning`
- [Weights & Biases](https://wandb.ai/): see the [Weigths & Biases guide](wandb)
- [MLFlow](https://github.com/mlflow/mlflow): see the [MLFlow guide](mlflow)
- [Croissant format](https://github.com/mlcommons/croissant): see the [Croissant guide](croissant)
- [scVI](https://scvi-tools.org/): see the [guide on the scVI docs](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/custom_dl/lamin.html)

## Workflow managers

- `nextflow` & the [Seqera](https://seqera.io) platform: see the [Nextflow guide](nextflow) and the [nf-lamin](nf-lamin) reference
- `redun`: via the Python API, see the [redun guide](redun)
- `prefect`, `airflow`, `dagster`, etc.: see the [workflows guide](track)
- `snakemake`: via post-run logic, see the [snakemake example](snakemake)

## Tables & arrays

- `pyarrow` & `polars`: see the `engine` argument of {meth}`~lamindb.Artifact.open` and the [arrays guide](arrays)
- `tiledbsoma`: [inhouse guide](scrna-tiledbsoma) or [cellxgene](cellxgene)
- `duckdb`: via parquet files, see [rxrx](rxrx)

## Visualization

- [Vitessce](https://vitessce.io): see the [vitessce guide](vitessce)
- [DataVisyn](https://datavisyn.io) visualization solutions

## ELN systems

- [Benchling](https://benchling.com): sync schema and data from your registries within our team/enterprise plan
