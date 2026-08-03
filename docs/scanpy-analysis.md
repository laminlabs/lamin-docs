# Scanpy analysis

Agentic re-implementation of the classic [PBMC3k Scanpy tutorial](https://docs.lamin.ai/pbmc3k): QC, clustering, marker discovery, and cell-type annotation — with cutoffs and labels chosen from the data, not hard-coded from the docs.

**Instance:** [laminlabs/lamindata](https://lamin.ai/laminlabs/lamindata)

## Agentic analysis

| Step                          | Transform                                                                                                                                                                        | Outputs                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Preprocess, cluster, annotate | [clustering.py](https://lamin.ai/laminlabs/lamindata/transform/mOZ8OZwgmYM70003) · [agent run](https://lamin.ai/laminlabs/lamindata/transform/SnfuhjObaAKR0000/m4PktKjtLWsX2fZB) | [annotated h5ad](https://lamin.ai/laminlabs/lamindata/artifact/6IfHab1aTnAfSiDm0000) · [cluster markers](https://lamin.ai/laminlabs/lamindata/artifact/wbKbBGjO9qVG4POk0000) · [QC violins](https://lamin.ai/laminlabs/lamindata/artifact/6oRmhfhw3HsqyOr70004) · [UMAP](https://lamin.ai/laminlabs/lamindata/artifact/H2yWpa2lgfMEhCc00004) · [marker dotplot](https://lamin.ai/laminlabs/lamindata/artifact/DlQvDpIl6fkQtqY50004) |

The cell-type rationale (QC cutoffs, cluster→type map, caveats) is attached as [notes](https://lamin.ai/laminlabs/lamindata/artifact/6IfHab1aTnAfSiDm0000) on the annotated AnnData.
