[![stars](https://img.shields.io/github/stars/laminlabs/lamindb?logo=GitHub&color=yellow)](https://github.com/laminlabs/lamindb)
[![pypi](https://img.shields.io/pypi/v/lamindb?color=blue&label=PyPI)](https://pypi.org/project/lamindb)
[![PyPI Downloads](https://img.shields.io/pepy/dt/lamindb?logo=pypi&color=blue)](https://pepy.tech/project/lamindb)
[![cran](https://www.r-pkg.org/badges/version/laminr?color=green)](https://cran.r-project.org/package=laminr)
[![DocsLLMs](https://img.shields.io/badge/LLMs-summary-yellow)](https://docs.lamin.ai/summary.md)

# Introduction

```{include} includes/README.md

```

LaminHub is a data collaboration hub built on LaminDB similar to how GitHub is built on git.

:::{dropdown} LaminHub specs

```{include} includes/specs-laminhub.md

```

:::

You can copy this [summary.md](https://docs.lamin.ai/summary.md) into an LLM chat and let AI explain Lamin.

## Quickstart

::::{tab-set}
:::{tab-item} Py
:sync: python

```{include} includes/quick-setup-lamindb.md

```

<!-- keep in sync with README -->

Track a script or notebook run with source code, inputs, outputs, logs, and environment.

```{eval-rst}
.. literalinclude:: includes/create-fasta.py
   :language: python
```

:::
:::{tab-item} R
:sync: r

```{include} includes/quick-setup-laminr.md

```

In an R session, transfer an scRNA-seq dataset from the `laminlabs/cellxgene` instance, compute marker genes with Seurat, and save results.

```{eval-rst}
.. literalinclude:: includes/r-quickstart.R
   :language: R
```

If you did _not_ use RStudio's notebook mode, create an html export and then run the following.

```R
laminr::lamin_save("my-analyis.Rmd")  # save source code and html report for a `.qmd` or `.Rmd` file
```

:::
::::

The script produced the following data lineage.

::::{tab-set}
:::{tab-item} Py

```python
artifact.view_lineage()
```

<div style="height: 0.5em;"></div>
<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/EkQATsQL5wqC95Wj0003.png" width="220">
:::
:::{tab-item} Hub

Explore data lineage for a more complicated example interactively [here](https://lamin.ai/laminlabs/lamindata/artifact/qQ6DCPnSKWMvA5GC0000).

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/mfFvKdqpvlbOyQ1d0000.png" width="800">
:::
::::
