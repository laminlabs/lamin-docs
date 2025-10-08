import lamindb as ln

# Access inputs -------------------------------------------

ln.track()  # track your run of a notebook or script
artifact = ln.Artifact.using("laminlabs/cellxgene").get(
    "7dVluLROpalzEh8m"
)  # query the artifact https://lamin.ai/laminlabs/cellxgene/artifact/7dVluLROpalzEh8m
adata = artifact.load()[
    :, :100
]  # load into memory or sync to cache: filepath = artifact.cache()

# Your transformation -------------------------------------

import scanpy as sc  # find marker genes with Scanpy

sc.pp.normalize_total(adata)
sc.pp.log1p(adata)
sc.tl.rank_genes_groups(adata, groupby="cell_type")

# Save outputs --------------------------------------------

ln.Artifact.from_anndata(
    adata, key="my-datasets/my-result.h5ad"
).save()  # save versioned output
ln.finish()  # finish the run, save source code & run report
