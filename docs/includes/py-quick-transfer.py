import lamindb as ln

# Access inputs -------------------------------------------

ln.track()
cellxgene_artifacts = ln.Artifact.connect("laminlabs/cellxgene")
artifact = cellxgene_artifacts.get("7dVluLROpalzEh8m")
adata = artifact.load()[:, :100]

# Your transformation -------------------------------------

import scanpy as sc

sc.pp.normalize_total(adata)
sc.pp.log1p(adata)
sc.tl.rank_genes_groups(adata, groupby="cell_type")

# Save outputs --------------------------------------------

ln.Artifact.from_anndata(adata, key="my-datasets/my-result.h5ad").save()
ln.finish()
