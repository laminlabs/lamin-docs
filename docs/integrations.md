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

## Ontologies & registries

- [bionty](/bionty): Basic biological ontologies, with easy import from >20 public ontologies
- [pertdb](/pertdb): Registries for perturbations (compounds, biologics, genetic interventions, etc.)

## Git

Sync tracked scripts in lamindb with git commits: [guide](track.ipynb#sync-scripts-with-git)

## MLOps

- {mod}`~lamindb.integrations.lightning`
- [Weights & Biases](wandb)
- [MLflow](mlflow)
- [Croissant files](croissant)
- [scVI](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/custom_dl/lamin.html)

## Workflow managers

- `nextflow` & the [Seqera](https://seqera.io) web platform: see the [Nextflow guide](nextflow) and the [nf-lamin](nf-lamin) reference
- `redun`: via the Python API, see the [redun guide](redun)
- the established Python workflow managers, see the [workflows guide](track)
- `snakemake`: via post-run logic, see the [snakemake example](snakemake)

## Tables & arrays

- `pyarrow` & `polars`: see the `engine` argument of `~lamindb.Artifact.open`
- `tiledbsoma`: [inhouse guide](scrna-tiledbsoma) or [cellxgene](cellxgene)
- `duckdb`: via parquet files, see [rxrx](rxrx)

## Visualization

- [Vitessce](vitessce)
- `Aevidence` from [DataVisyn](https://datavisyn.io)

## ELN systems

- [Benchling](https://benchling.com): sync schema and data from your registries within our team/enterprise plan. [Reach out](https://lamin.ai/contact) to learn more!
