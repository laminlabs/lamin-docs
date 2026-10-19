# Integrations

```{eval-rst}
.. role:: small
```

## Agent harnesses [{small}`docs`](track.ipynb#track-agent-runs)

- Claude Code {small}`db 2.8`
- GitHub Copilot {small}`db 2.9`
- Cursor {small}`db 2.11`
- Codex {small}`db 2.12`

## Storage [{small}`docs`](https://docs.lamin.ai/lamindb.storage)

Read & write:

- Local file systems
- AWS S3
- S3-compatible storage services, e.g., MinIO & Cloudflare R2
- Google Cloud Storage

Read only:

- http/https: `ln.Artifact("https://a-website.com/a-dataset.txt")`
- Hugging Face: `ln.Artifact("hf://datasets/org/repo/dataset.parquet")`

## Ontologies & registries

- [bionty](/bionty): Biological ontologies, with easy import from >20 public ontologies
- [pertdb](/pertdb): Registries for perturbations (compounds, biologics, genetic interventions, etc.)

## Git <span class="small">{ref}`docs <sync-code-with-git>`</span>

Auto-sync code with `git`.

## Computational notebooks [{small}`docs`](/track)

You can call `ln.track()` and `ln.finish()` (or the R versions) in four notebook types:

- Jupyter
- Marimo
- R markdown
- Quarto

For Jupyter notebooks, source code is stored in `.py` format and run reports as html.

## MLOps

- [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning) → {mod}`~lamindb.integrations.lightning`
- [Weights & Biases](https://wandb.ai/) → {doc}`docs </wandb>`
- [MLFlow](https://github.com/mlflow/mlflow) → {doc}`docs </mlflow>`
- [Croissant format](https://github.com/mlcommons/croissant) → {doc}`docs </croissant>`
- [scVI](https://scvi-tools.org/) → [docs](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/custom_dl/lamin.html)

## Workflow managers

- `nextflow` & `seqera.io` → [nf-lamin](nf-lamin)
- `redun` → [docs](redun)
- `prefect`, `airflow`, `dagster`, etc. → {doc}`docs </track>`
- `snakemake` → [docs](snakemake)

## Tables & arrays

- `pyarrow` & `polars`: see the `engine` argument of {meth}`~lamindb.Artifact.open` and the [arrays guide](arrays)
- `tiledbsoma`: [inhouse guide](scrna-tiledbsoma) or {doc}`cellxgene </cellxgene>`
- `duckdb`: via parquet files, see [rxrx](rxrx)

## Visualization

- [Vitessce](https://vitessce.io): see the [vitessce guide](vitessce)
- [DataVisyn](https://datavisyn.io): reach out for custom visualization solutions

## ELN systems

- [Benchling](https://benchling.com): sync schema and data from your registries within our team/enterprise plan
