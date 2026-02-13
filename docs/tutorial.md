---
execute_via: python
---

# Tutorial

LaminDB provides a framework to transform datasets into more useful representations: validated & queryable datasets, machine learning models, and analytical insights. The transformations can be notebooks, scripts, pipelines, or functions.

The metadata involved in this process are stored in a _LaminDB instance_, a database that manages datasets in storage. For the following walk through LaminDB's core features, we'll be working with a local instance.

## Track a notebook or script

```python
!lamin init --storage ./lamindb-tutorial --modules bionty
```

<!-- #region -->

:::{dropdown} Via the R shell

```R
library(laminr)
lc <- import_module("lamin_cli")
lc$init(storage = "./lamin-tutorial", modules = "bionty")
```

:::

<!-- #endregion -->

:::{dropdown} What else can I configure during setup?

1. You can pass a cloud storage location to `--storage` (S3, GCP, R2, HF, etc.)
   ```python
   --storage s3://my-bucket
   ```
2. Instead of the default SQLite database pass a Postgres connection string to `--db`:
   ```python
   --db postgresql://<user>:<pwd>@<hostname>:<port>/<dbname>
   ```
3. Instead of a default instance name derived from the storage location, provide a custom name:
   ```python
   --name my-name
   ```
4. Mount additional schema modules:
   ```python
   --modules bionty,pertdb,custom1
   ```

For more info, see {doc}`/setup`.

:::

:::{dropdown} If you decide to connect your instance to the hub, you will see data & metadata in a UI.

<a href="https://lamin.ai/laminlabs/lamindata">
<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/YuefPQlAfeHcQvtq0000.png" width="700px">
</a>

:::

Let's now track the notebook that's being run.

```python
import lamindb as ln

ln.track()  # track the current notebook or script
```

:::{dropdown} Via the R shell

```R
library(laminr)
ln <- import_module("lamindb")  # instantiate the central `ln` object of the API

ln$track()  # track a run of your notebook or script
```

:::

By calling {meth}`~lamindb.track`, the notebook gets automatically linked as the source of all data that's about to be saved! You can see all your transforms and their runs in the {class}`~lamindb.Transform` and {class}`~lamindb.Run` registries.

```python
ln.Transform.to_dataframe()
```

```python
ln.Run.to_dataframe()
```

<!-- #region -->

:::{dropdown} What happened under the hood?

1. The full run environment and imported package versions of current notebook were detected
2. Notebook metadata was detected and stored in a {class}`~lamindb.Transform` record with a unique id
3. Run metadata was detected and stored in a {class}`~lamindb.Run` record with a unique id

The {class}`~lamindb.Transform` registry stores data transformations: scripts, notebooks, pipelines, functions.

The {class}`~lamindb.Run` registry stores executions of transforms. Many runs can be linked to the same transform if executed with different context (time, user, input data, etc.).

:::

:::{dropdown} How do I track a pipeline instead of a notebook?

Leverage a pipeline integration, see: {doc}`/pipelines`. Or manually add code as seen below.

```python
transform = ln.Transform(name="My pipeline")
transform.version = "1.2.0"  # tag the version
ln.track(transform)
```

:::

:::{dropdown} Why should I care about tracking notebooks?

Because of interactivity & humans are in the loop, most mistakes happen when using notebooks.

{func}`~lamindb.track` makes notebooks & derived results reproducible & auditable, enabling to learn from mistakes.

This is important as much insight generated from biological data is driven by computational biologists _interacting_ with it. An early blog post on this is [here](https://blog.lamin.ai/nbproject).

:::

<!-- #endregion -->

:::{dropdown} Is this compliant with OpenLineage?

Yes. What OpenLineage calls a "job", LaminDB calls a "transform". What OpenLineage calls a "run", LaminDB calls a "run".

:::

## Manage artifacts

The {class}`~lamindb.Artifact` class manages datasets & models that are stored as files, folders, or arrays. {class}`~lamindb.Artifact` is a registry to manage search, queries, validation & storage access.

You can register data objects (`DataFrame`, `AnnData`, ...) and files or folders in local storage, AWS S3 (`s3://`), Google Cloud (`gs://`), Hugging Face (`hf://`), or any other file system supported by `fsspec`.

### Create an artifact

Let's first look at an exemplary dataframe.

```python
df = ln.examples.datasets.mini_immuno.get_dataset1(with_typo=True)
df
```

:::

This is how you create an artifact from a dataframe.

```python
artifact = ln.Artifact.from_dataframe(df, key="my_datasets/rnaseq1.parquet").save()
artifact.describe()
```

### Access artifacts

Get the artifact by `key`.

```python
artifact = ln.Artifact.get(key="my_datasets/rnaseq1.parquet")
```

:::

And this is how you load it back into memory.

```python
artifact.load()
```

Typically your artifact is in a cloud storage location. To get a local file path to it, call {meth}`~lamindb.Artifact.cache`.

```python
artifact.cache()
```

If the data is large, you might not want to cache but stream it via {meth}`~lamindb.Artifact.open`. For more on this, see: {doc}`arrays`.

### Trace data lineage

You can understand where an artifact comes from by looking at its {class}`~lamindb.Transform` & {class}`~lamindb.Run` records.

```python
artifact.transform
```

<!-- #region -->

```python
artifact.run
```

Or visualize deeper data lineage with the `view_lineage()` method. Here we're only one step deep.

```python
artifact.view_lineage()
```

:::::{dropdown} Show me a more interesting example, please!

::::{tab-set}
:::{tab-item} Py

Explore and load the notebook from [here](https://lamin.ai/laminlabs/lamindata/transform/F4L3oC6QsZvQ0002).

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/KQmzmmLOeBN0C8Yk0003.png" width="800">
:::
:::{tab-item} Hub

Explore data lineage interactively [here](https://lamin.ai/laminlabs/lamindata/artifact/W1AiST5wLrbNEyVq0000).

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/0bXenaC9F24iP3Iy0000.png" width="800">
:::
::::

:::::

Once you're done, at the end of your notebook or script, call {meth}`~lamindb.finish`. Here, we're not yet done so we're commenting it out.

```python
# ln.finish()  # mark run as finished, save execution report, source code & environment
```

:::{dropdown} Via the R shell

```R
# ln$finish()  # mark run as finished, save execution report & source code
```

If you did _not_ use RStudio's notebook mode, you have to render an HTML externally.

1. Render the notebook to HTML via one of:

   - In RStudio, click the "Knit" button
   - From the command line, run

     ```bash
     Rscript -e 'rmarkdown::render("tutorial.Rmd")'
     ```

   - Use the `rmarkdown` package in R

     ```r
     rmarkdown::render("tutorial.Rmd")
     ```

2. Save it to your LaminDB instance via one of:

   - Using the `save()` command in the `lamin_cli` module from R

     ```r
     lc <- import_module("lamin_cli")
     lc$save("tutorial.Rmd")
     ```

   - Using the `lamin` CLI

     ```bash
     lamin save tutorial.Rmd
     ```

:::

:::{dropdown} Here is how a notebook looks on the hub.

[Explore](https://lamin.ai/laminlabs/lamindata/transform/PtTXoc0RbOIq65cN).

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/RGXj5wcAf7EAc6J80003.png" width="900px">

:::

<!-- #region -->

To create a new version of a notebook or script, run `lamin load` on the terminal, e.g.,

```bash
$ lamin load https://lamin.ai/laminlabs/lamindata/transform/13VINnFk89PE0004
→ notebook is here: mcfarland_2020_preparation.ipynb
```

<!-- #endregion -->

Note that data lineage also helps to understand what a dataset is being used for, not only where it comes from. Many datasets are being used over and over for different purposes and it's often useful to understand how.

### Annotate an artifact

You can annotate artifacts with features and labels. Features are measurement dimensions (e.g. `"organism"`, `"temperature"`) and labels are measured categories (e.g. `"human"`, `"mouse"`).

Let's annotate an artifact with a {class}`~lamindb.Record`, a built-in universal label ontology.

```python
# create & save a record
my_experiment = ln.Record(name="My experiment").save()

# annotate the artifact with a record
artifact.records.add(my_experiment)

# describe the artifact
artifact.describe()
```

:::

This is how you query artifacts based on the annotation.

```python
ln.Artifact.filter(records=my_experiment).to_dataframe()
```

You can also annotate with labels from other registries, e.g., the biological ontologies in {mod}`bionty`.

```python
import bionty as bt

# create a cell type label from the source ontology
cell_type = bt.CellType.from_source(name="effector T cell").save()

# annotate the artifact with a cell type
artifact.cell_types.add(cell_type)

# describe the artifact
artifact.describe()
```

:::{dropdown} Via the R shell

```R
bt <- import_module("bionty")

# create a cell type label from the source ontology
cell_type <- bt$CellType$from_source(name = "effector T cell")$save()

# annotate the artifact with a cell type
artifact$cell_types$add(cell_type)

# describe the artifact
artifact$describe()
```

:::

This is how you query artifacts by cell type annotations.

```python
ln.Artifact.filter(cell_types=cell_type).to_dataframe()
```

:::{dropdown} Via the R shell

```R
ln$Artifact$filter(cell_types = cell_type)$to_dataframe()
```

:::

If you want to annotate by non-categorical metadata or indicate the feature for a label, annotate via features.

```python
# define the "temperature" & "experiment" features
ln.Feature(name="temperature", dtype=float).save()
ln.Feature(name="experiment", dtype=ln.Record).save()

# annotate the artifact
artifact.features.add_values({"temperature": 21.6, "experiment": "My experiment"})

# describe the artifact
artifact.describe()
```

:::{dropdown} Via the R shell

```R
# define the "temperature" & "experiment" features
ln$Feature(name = "temperature", dtype = "float")$save()
ln$Feature(name = "experiment", dtype = ln$Record)$save()

# annotate the artifact
artifact$features$add_values(
  list(temperature = 21.6, experiment = "My experiment")
)

# describe the artifact
artifact$describe()
```

:::

This is how you query artifacts by features.

```python
ln.Artifact.filter(temperature=21.6).to_dataframe()
```

:::{dropdown} Via the R shell

```R
ln$Artifact$filter(temperature = 21.6)$to_dataframe()
```

:::

### Validate an artifact

Validated datasets are more re-usable by analysts and machine learning models. You can define what a valid artifact should look like by defining a schema.

In lamindb, validation also means annotation with the validated metadata which increases the findability of a dataset.

:::{dropdown} Can you give me examples for what findability and usability means?

1. Findability: Which datasets measured expression of cell marker `CD14`? Which characterized cell line `K562`? Which have a test & train split? Etc.
2. Usability: Are there typos in feature names? Are there typos in labels? Are types and units of features consistent? Etc.

:::

```python
import bionty as bt  # <-- use bionty to access registries with imported public ontologies

# define a few more valid labels
ln.Record(name="DMSO").save()
ln.Record(name="IFNG").save()

# define a few more valid features
ln.Feature(name="perturbation", dtype=ln.Record).save()
ln.Feature(name="cell_type_by_model", dtype=bt.CellType).save()
ln.Feature(name="cell_type_by_expert", dtype=bt.CellType).save()
ln.Feature(name="assay_oid", dtype=bt.ExperimentalFactor.ontology_id).save()
ln.Feature(name="donor", dtype=str, nullable=True).save()
ln.Feature(name="sample_note", dtype=str, nullable=True).save()
ln.Feature(name="concentration", dtype=str).save()
ln.Feature(name="treatment_time_h", dtype="num", coerce_dtype=True).save()

# define a schema that merely enforces a feature identifier type
schema = ln.Schema(itype=ln.Feature).save()
```

:::{dropdown} Via the R shell

```R
bt <- import_module("bionty")  # <-- use bionty to access registries with imported public ontologies

# define a few more valid labels
ln$Record(name = "DMSO")$save()
ln$Record(name = "IFNG")$save()

# define a few more valid features
ln$Feature(name = "perturbation", dtype = ln$Record)$save()
ln$Feature(name = "cell_type_by_model", dtype = bt$CellType)$save()
ln$Feature(name = "cell_type_by_expert", dtype = bt$CellType)$save()
ln$Feature(name = "assay_oid", dtype = bt$ExperimentalFactor$ontology_id)$save()
ln$Feature(name = "donor", dtype = "str", nullable = TRUE)$save()
ln$Feature(name = "concentration", dtype = "str")$save()
ln$Feature(name = "treatment_time_h", dtype = "num", coerce_dtype = TRUE)$save()

# define a schema that merely enforces a feature identifier type
schema <- ln$Schema(itype = ln$Feature)$save()
```

:::

If you pass a `schema` object to the `Artifact` constructor, the artifact will be validated & annotated. Let's try this.

```python
try:
    artifact = ln.Artifact.from_dataframe(
        df, key="my_datasets/rnaseq1.parquet", schema=schema
    )
except ln.errors.ValidationError as error:
    print(str(error))
```

Because there is a typo in the `perturbation` column, validation fails. Let's fix it by making a new version.

### Make a new version of an artifact

```python
# fix the "IFNJ" typo
df["perturbation"] = df["perturbation"].cat.rename_categories({"IFNJ": "IFNG"})

# create a new version
artifact = ln.Artifact.from_dataframe(
    df, key="my_datasets/rnaseq1.parquet", schema=schema
).save()

# see the annotations
artifact.describe()

# see all versions of the artifact
artifact.versions.to_dataframe()
```

:::{dropdown} Via the R shell

```R
# fix the "IFNJ" typo
levels(df$perturbation) <- c("DMSO", "IFNG")
df["sample2", "perturbation"] <- "IFNG"

# create a new version
artifact <- ln$Artifact$from_dataframe(df, key = "my_datasets/rnaseq1.parquet", schema = schema)$save()

# see the annotations
artifact$describe()

# simplest way to check that artifact was validated
artifact$schema

# see all versions of an artifact
artifact$versions$to_dataframe()
```

:::

The content of the dataset is now validated and the dataset is richly annotated and queryable by all entities that you defined.

<!-- #region -->

:::{dropdown} Can I also create new versions without passing `key`?

That works, too, you can use `revises`:

```python
artifact_v1 = ln.Artifact.from_dataframe(df, description="Just a description").save()
# below revises artifact_v1
artifact_v2 = ln.Artifact.from_dataframe(df_updated, revises=artifact_v1).save()
```

<br>

The good thing about passing `revises: Artifact` is that you don't need to worry about coming up with naming conventions for paths.

The good thing about versioning based on `key` is that it's how all data versioning tools are doing it.

:::

<!-- #endregion -->

## Query & search registries

We've already seen a few queries. Let's now walk through the topic systematically.

To get an overview over all artifacts in your instance, call {class}`~lamindb.models.SQLRecord.df`.

```python
ln.Artifact.to_dataframe()
```

:::{dropdown} Via the R shell

```R
ln$Artifact$to_dataframe()
```

:::

The `Artifact` registry additionally supports seeing all feature annotations of an artifact.

```python
ln.Artifact.to_dataframe(features=True)
```

:::{dropdown} Via the R shell

```R
ln$Artifact$to_dataframe(features = TRUE)
```

:::

LaminDB's central classes are registries that store records ({class}`~lamindb.models.SQLRecord` objects). If you want to see the fields of a registry, look at the class or auto-complete.

```python
ln.Artifact
```

:::{dropdown} Via the R shell

```R
ln$Artifact
```

:::

Each registry is a table in the relational schema of the underlying database. With {func}`~lamindb.view`, you can see the latest records in the database.

```python
ln.view()
```

:::{dropdown} Via the R shell

```R
ln$view()
```

:::

:::{dropdown} Which registries have I already learned about? 🤔

- {class}`~lamindb.Artifact`: datasets & models stored as files, folders, or arrays
- {class}`~lamindb.Transform`: transforms of artifacts
- {class}`~lamindb.Run`: runs of transforms
- {class}`~lamindb.User`: users
- {class}`~lamindb.Storage`: local or cloud storage locations

:::

Every registry supports arbitrary relational queries using the class methods {class}`~lamindb.models.SQLRecord.get` and {class}`~lamindb.models.SQLRecord.filter`.
The syntax for it is Django's query syntax.

Here are some simple query examples.

```python
# get a single record (here the current notebook)
transform = ln.Transform.get(key="tutorial.ipynb")

# get a set of records by filtering for a directory (LaminDB treats directories like AWS S3, as the prefix of the storage key)
ln.Artifact.filter(key__startswith="my_datasets/").to_dataframe()

# query all artifacts ingested from a transform
artifacts = ln.Artifact.filter(transform=transform).all()

# query all artifacts ingested from a notebook with "tutor" in the description
artifacts = ln.Artifact.filter(
    transform__description__icontains="tutor",
).all()
```

:::{dropdown} Via the R shell

```R
# get a single record (here the current notebook)
transform <- ln$Transform$get(key = "tutorial.Rmd")

# get a set of records by filtering for a directory (LaminDB treats directories like AWS S3, as the prefix of the storage key)
ln$Artifact$filter(key__startswith = "my_datasets/")$to_dataframe()

# query all artifacts ingested from a transform
artifacts <- ln$Artifact$filter(transform = transform)$all()

# query all artifacts ingested from a notebook with "tutor" in the description
artifacts <- ln$Artifact$filter(
  transform__description__icontains = "tutor",
)$all()
```

:::

:::{dropdown} What does a double underscore mean?

For any field, the double underscore defines a comparator, e.g.,

- `name__icontains="Martha"`: `name` contains `"Martha"` when ignoring case
- `name__startswith="Martha"`: `name` starts with `"Martha`
- `name__in=["Martha", "John"]`: `name` is `"John"` or `"Martha"`

For more info, see: {doc}`registries`.

:::

:::{dropdown} Can I chain filters and searches?

Yes: `ln.Artifact.filter(suffix=".jpg").search("my image")`

:::

The class methods {class}`~lamindb.models.SQLRecord.search` and {class}`~lamindb.models.SQLRecord.lookup` help with approximate matches.

```python
# search artifacts
ln.Artifact.search("iris").to_dataframe().head()

# search transforms
ln.Transform.search("tutor").to_dataframe()

# look up records with auto-complete
records = ln.Record.lookup()
```

:::{dropdown} Via the R shell

```R
# search artifacts
ln$Artifact$search("iris")$to_dataframe() |> head()

# search transforms
ln$Transform$search("tutor")$to_dataframe()

# look up records with auto-complete
records <- ln$Record$lookup()
```

:::

:::{dropdown} Show me a screenshot

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/lgRNHNtMxjU0y8nIagt7.png" width="400px">

:::

For more info, see: {doc}`registries`.

## Manage files & folders

Let's look at a folder in the cloud that contains 3 sub-folders storing images & metadata of Iris flowers, generated in 3 subsequent studies.

```python
# we use anon=True here in case no aws credentials are configured
ln.UPath("s3://lamindata/iris_studies", anon=True).view_tree()
```

:::{dropdown} Via the R shell

```R
# we use anon=True here in case no aws credentials are configured
ln$UPath("s3://lamindata/iris_studies", anon = TRUE)$view_tree()
```

:::

Let's create an artifact for the first sub-folder.

```python
artifact = ln.Artifact("s3://lamindata/iris_studies/study0_raw_images").save()
artifact
```

:::{dropdown} Via the R shell

```R
artifact <- ln$Artifact("s3://lamindata/iris_studies/study0_raw_images")$save()
artifact
```

:::

As you see from {attr}`~lamindb.Artifact.path`, the folder was merely registered in its present storage location without copying it.

```python
artifact.path
```

:::{dropdown} Via the R shell

```R
artifact$path
```

:::

LaminDB keeps track of all your storage locations.

```python
ln.Storage.to_dataframe()
```

:::{dropdown} Via the R shell

```R
ln$Storage$to_dataframe()
```

:::

:::{dropdown} How do I update or delete an artifact?

```
artifact.description = "My new description"  # change description
artifact.save()  # save the change to the database
artifact.delete()  # move to trash
artifact.delete(permanent=True)  # permanently delete
```

:::

:::{dropdown} How do I create an artifact for a local file or folder?

Source path is local:

```python
ln.Artifact("./my_data.fcs", key="my_data.fcs")
ln.Artifact("./my_images/", key="my_images")
```

<br>

Upon `artifact.save()`, the source path will be copied or uploaded into your instance's current storage, visible & changeable via `ln.settings.storage`.

If the source path is remote _or_ already in a registered storage location (one that's registered in `ln.Storage`), `artifact.save()` will _not_ trigger a copy or upload but register the existing path.

```python
ln.Artifact("s3://my-bucket/my_data.fcs")  # key is auto-populated from S3, you can optionally pass a description
ln.Artifact("s3://my-bucket/my_images/")  # key is auto-populated from S3, you can optionally pass a description
```

<br>
You can use any storage location supported by `fsspec`.

:::

:::{dropdown} Which fields are populated when creating an artifact record?

Basic fields:

- `uid`: universal ID
- `key`: a (virtual) relative path of the artifact in `storage`
- `description`: an optional string description
- `storage`: the storage location (the root, say, an S3 bucket or a local directory)
- `suffix`: an optional file/path suffix
- `size`: the artifact size in bytes
- `hash`: a hash useful to check for integrity and collisions (is this artifact already stored?)
- `hash_type`: the type of the hash
- `created_at`: time of creation
- `updated_at`: time of last update

Provenance-related fields:

- `created_by`: the {class}`~lamindb.User` who created the artifact
- `run`: the {class}`~lamindb.Run` of the {class}`~lamindb.Transform` that created the artifact

For a full reference, see {class}`~lamindb.Artifact`.

:::

:::{dropdown} What exactly happens during save?

In the database: An artifact record is inserted into the `Artifact` registry. If the artifact record exists already, it's returned.

In storage:

- If the default storage is in the cloud, `.save()` triggers an upload for a local artifact.
- If the artifact is already in a registered storage location, only the metadata of the record is saved to the `artifact` registry.

:::

:::{dropdown} How does LaminDB compare to a AWS S3?

LaminDB provides a database on top of AWS S3 (or GCP storage, file systems, etc.).

Similar to organizing files with paths, you can organize artifacts using the `key` parameter of {class}`~lamindb.Artifact`.

However, you'll see that you can more conveniently query data by entities you care about: people, code, experiments, genes, proteins, cell types, etc.

:::

:::{dropdown} Are artifacts aware of array-like data?

Yes.

You can make artifacts from paths referencing array-like objects:

```python
ln.Artifact("./my_anndata.h5ad", key="my_anndata.h5ad")
ln.Artifact("./my_zarr_array/", key="my_zarr_array")
```

Or from in-memory objects:

```python
ln.Artifact.from_dataframe(df, key="my_dataframe.parquet")
ln.Artifact.from_anndata(adata, key="my_anndata.h5ad")
```

You can open large artifacts for slicing from the cloud or load small artifacts directly into memory via:

```python
artifact.open()
```

:::

<!-- #endregion -->

## Manage biological registries

Every {py:mod}`bionty` registry is based on configurable public ontologies (>20 of them) that are automatically leveraged during validation & annotation. Sometimes you want to access the public ontology directly.

```python
import bionty as bt

cell_type_ontology = bt.CellType.public()
cell_type_ontology
```

The returned object can be searched like you can search a registry.

```python
cell_type_ontology.search("gamma-delta T cell").head(2)
```

Because you can't update an external public ontology, you update the content of the corresponding registry. Here, you create a new cell type.

```python
# create an ontology-coupled cell type record and save it
neuron = bt.CellType.from_source(name="neuron").save()

# create a record to track a new cell state
new_cell_state = bt.CellType(
    name="my neuron cell state", description="explains X"
).save()

# express that it's a neuron state
new_cell_state.parents.add(neuron)

# view ontological hierarchy
new_cell_state.view_parents(distance=2)
```

## Manage AnnData objects

LaminDB supports a growing number of data structures: `DataFrame`, `AnnData`, `MuData`, `SpatialData`, and `Tiledbsoma` with their corresponding representations in storage.

Let's go through the example of the quickstart, but store the dataset in an AnnData this time.

```python
# define var schema
var_schema = ln.Schema(itype=bt.Gene.ensembl_gene_id, dtype=int).save()

# define composite schema
anndata_schema = ln.Schema(
    otype="AnnData", slots={"obs": schema, "var.T": var_schema}
).save()
```

Validate & annotate an `AnnData`.

```python
import anndata as ad

# store the dataset as an AnnData object to distinguish data from metadata
adata = ad.AnnData(df.iloc[:, :3], obs=df.iloc[:, 3:-1])

# save curated artifact
artifact = ln.Artifact.from_anndata(
    adata, key="my_datasets/my_rnaseq1.h5ad", schema=anndata_schema
).save()
artifact.describe()
```

Because `AnnData` separates the high-dimensional count matrix that's typically indexed with Ensembl gene ids from the metadata, we're now working with two types of feature sets (`bt.Gene` for the counts and `ln.Feature` for the metadata). These correspond to the `obs` and the `var` schema in the `anndata_schema`.

If you want to find a dataset by whether it measured `CD8A`, you can do so as as follows.

```python
# query for all feature sets that contain CD8A
feature_sets = ln.Schema.filter(genes__symbol="CD8A").all()

# query for all artifacts linked to these feature sets
ln.Artifact.filter(feature_sets__in=feature_sets).to_dataframe()
```

## Scale learning

How do you integrate new datasets with your existing datasets? Leverage {class}`~lamindb.Collection`.

```python
# a new dataset
df2 = ln.examples.datasets.mini_immuno.get_dataset2(otype="DataFrame")
adata = ad.AnnData(df2.iloc[:, :3], obs=df2.iloc[:, 3:-1])
artifact2 = ln.Artifact.from_anndata(
    adata, key="my_datasets/my_rnaseq2.h5ad", schema=anndata_schema
).save()
```

Create a collection using {class}`~lamindb.Collection`.

```python
collection = ln.Collection([artifact, artifact2], key="my-RNA-seq-collection").save()
collection.describe()
collection.view_lineage()
```

```python
# if it's small enough, you can load the entire collection into memory as if it was one
collection.load()

# typically, it's too big, hence, open it for streaming (if the backend allows it)
# collection.open()

# or iterate over its artifacts
collection.artifacts.all()

# or look at a DataFrame listing the artifacts
collection.artifacts.to_dataframe()
```

Directly train models on collections of `AnnData`.

```
# to train models, batch iterate through the collection as if it was one array
from torch.utils.data import DataLoader, WeightedRandomSampler
dataset = collection.mapped(obs_keys=["cell_medium"])
sampler = WeightedRandomSampler(
    weights=dataset.get_label_weights("cell_medium"), num_samples=len(dataset)
)
data_loader = DataLoader(dataset, batch_size=2, sampler=sampler)
for batch in data_loader:
    pass
```

Read this [blog post](https://lamin.ai/blog/arrayloader-benchmarks) for more on training models on distributed datasets.
