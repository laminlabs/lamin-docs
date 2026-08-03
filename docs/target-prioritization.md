# Target prioritization

Extend the [Schmidt et al. (2022)](https://pubmed.ncbi.nlm.nih.gov/35113687/) CRISPRa IFNG screen lineage toward immunotherapy target prioritization.

The human pipeline calls positive IFNG hits from a genome-wide CRISPRa screen in primary T cells and joins them with Perturb-seq cell states. Agent-tracked scripts then map those hits to mechanisms of action, score druggability and drug-repurposing candidates, and re-rank targets by enrichment in IFNG-high transcriptional states.

**Project:** [Schmidt22](https://lamin.ai/laminlabs/lamindata/project/iD3P5kq1LPtM) · **Repo:** [laminlabs/schmidt22](https://github.com/laminlabs/schmidt22)

## Upstream (human)

|                               | Link                                                                                                                                                           |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IFNG hits (`pos\|fdr < 0.01`) | [artifact](https://lamin.ai/laminlabs/lamindata/artifact/Ywz5JiVNHOWSJDiK0001)                                                                                 |
| Perturb-seq joint analysis    | [artifact](https://lamin.ai/laminlabs/lamindata/artifact/W1AiST5wLrbNEyVq0001) · [lineage](https://lamin.ai/laminlabs/lamindata/artifact/W1AiST5wLrbNEyVq0001) |

## Agent analyses

| Step                            | Transform                                                                                                                                                                 | Outputs                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. MoA + immunotherapy map      | [script](https://lamin.ai/laminlabs/lamindata/transform/SSHeA8scWaLi0000) · [agent run](https://lamin.ai/laminlabs/lamindata/transform/SnfuhjObaAKR0000/I9sh2MDwS75XX3bf) | [moa map](https://lamin.ai/laminlabs/lamindata/artifact/FydRpUZu93QVCXVD0001)                                                                                          |
| 2. Druggability + repurposing   | [script](https://lamin.ai/laminlabs/lamindata/transform/eT8whOVrV8II0002) · [agent run](https://lamin.ai/laminlabs/lamindata/transform/SnfuhjObaAKR0000/gIXbKgKHFPlq2mgi) | [druggability](https://lamin.ai/laminlabs/lamindata/artifact/sHqkE5Vz9M9C6C900000) · [repurposing](https://lamin.ai/laminlabs/lamindata/artifact/v5yV12AQGsqqkiVo0002) |
| 3. Cell-state prioritization    | [script](https://lamin.ai/laminlabs/lamindata/transform/7tVVuExlIJaN0002) · [agent run](https://lamin.ai/laminlabs/lamindata/transform/SnfuhjObaAKR0000/BAV5qIH6maaFHqgN) | [prioritized targets](https://lamin.ai/laminlabs/lamindata/artifact/NuZqfITKaDxHtL8J0000)                                                                              |
| 4. Top-20 therapeutic shortlist | [script](https://lamin.ai/laminlabs/lamindata/transform/cFJ4WtpGmlVj0000) · [agent run](https://lamin.ai/laminlabs/lamindata/transform/SnfuhjObaAKR0000/904hjoV9vGRln30H) | [shortlist](https://lamin.ai/laminlabs/lamindata/artifact/KshPxhUepcTpayYj0000)                                                                                        |
