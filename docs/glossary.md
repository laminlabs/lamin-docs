# Glossary

```{glossary}

artifact
    An artifact stores a dataset or model as a file or folder. It is the output of a (tracked or untracked) process.

curator
    An object designed to ensure your dataset conforms with a desired schema.
    It helps with validation, standardization (e.g., by fixing typos or mapping synonyms), and annotation (linking it to metadata entities so that it becomes queryable).

FAIR
    FAIR data is data that meets the principles of findability, accessibility, interoperability, and reusability [[Wikipedia](https://en.wikipedia.org/wiki/FAIR_data)].

feature
    A feature is a measurable property represented in data (e.g., scalar, vector, image, embedding) [[Wikipedia](https://en.wikipedia.org/wiki/Feature_(machine_learning))].
    In these docs, we use "feature" independent of modeling role: a feature can serve as predictor, target, covariate, or a metadata {term}`variable`, depending on the analysis.
    A feature maps to one or more dataset dimensions; in tabular data, scalar features map 1:1 to columns.

    LaminDB comes with a {class}`~lamindb.Feature` registry to organize dataset dimensions.

GUI
    Graphical user interface, for instance, a browser-based data catalog.

instance
    Shorthand for "LaminDB instance", a database that manages metadata for datasets in different storage locations.

label
    A label in LaminDB is an entity in a registry -- e.g. a sample, cell type, or perturbation -- that can be linked to another entity -- e.g. a dataset or model.

lakehouse
    A data lakehouse combines the flexibility and cost-effectiveness of a data lake with data-management capabilities commonly associated with data warehouses.
    Typical capabilities include schema management, transactional guarantees (ACID), and metadata/index structures that reduce full dataset scans for many query patterns.
    Widely adopted open table formats in this space include [Apache Iceberg](https://iceberg.apache.org/), [Delta Lake](https://delta.io/), and [Apache Hudi](https://hudi.apache.org/).
    Managed services and platforms include offerings such as Google's [BigLake](https://cloud.google.com/biglake), Amazon's [Lake Formation](https://aws.amazon.com/lake-formation/), [Dremio](https://www.dremio.com/), and [Starburst](https://www.starburst.io/).
    For background, see this [blog post](https://cloud.google.com/blog/products/data-analytics/unify-data-lakes-and-warehouses-with-biglake-now-generally-available) from Google, this [blog post](https://aws.amazon.com/blogs/big-data/build-a-lake-house-architecture-on-aws/) from AWS, this [glossary entry](https://www.databricks.com/glossary/data-lakehouse), and this [paper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) from Databricks.

ORM
    Object-relational mapper. In LaminDB every subclass of {class}`~lamindb.models.SQLRecord` is an ORM model that corresponds to a SQL table in the underlying metadata database [[Wikipedia](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)].
    A `SQLRecord` object maps to a single row of the table.
    We refer to the `SQLRecord` class as a {term}`registry`, hence the name of its metaclass:  {class}`~lamindb.models.Registry`.

observation
    In statistics and machine learning, an observation refers to a measurement of a set of random variables.

    In biology, an observation typically corresponds to measuring (reading out) a set of properties from a biological sample.

record
    A record is a data structure that consists of a sequence of typed [fields](https://en.wikipedia.org/wiki/Field_(computer_science)) that hold values [[Wikipedia](https://en.wikipedia.org/wiki/Record_(computer_science))].

    In LaminDB, any metadata record -- including {class}`~lamindb.Artifact`, {class}`~lamindb.Transform`, {class}`~lamindb.Run`, etc. -- is modeled as a {class}`~lamindb.models.SQLRecord` and is stored in a row in a table in the SQL database. LaminDB also comes with a class to dynamically model records, {class}`~lamindb.Record`. This is useful for describing more frequently changing dataset schemas, for example, the columns in dynamically ingested parquet files or dynamically created sheets. While changing the fields of a `SQLRecord` requires updating its Python data model definition and running a migration in the SQL database, changing the features of a `Record` can be done dynamically.

sample
    In biology, a sample is an instance or part of a biological system.

    In classical statistics, a sample usually refers to a set of observations drawn from a population.
    In machine learning, a sample often refers to a single observation (one row) of random variables (features, labels, metadata).

    Depending on the observational unit chosen for representing data, the statistical sample might correspond 1:1 to a biological sample.
    Often, this choice presents interesting cases, as variation across physical samples -- targeted in the experimental design -- can be directly explained by variation across statistical (digital) samples.

variable
    We almost always mean "random variable", when we say "variable".

    An independent variable is sometimes called a {term}`feature` (the preferred term in these docs), "predictor variable", "regressor", "covariate", "explanatory variable", "risk factor", "input variable", among others [[Wikipedia](https://en.wikipedia.org/wiki/Dependent_and_independent_variables)].
    A dependent variable is sometimes called a "response variable", "regressand", "predicted variable", "measured variable", among others.

schema
    A schema is a blueprint for your dataset's structure and a tool for curating and validating the organization of your dataset, helping maintain data integrity as it evolves through various processing steps.

registry
    A table in a SQL database (SQLite/Postgres) holding records, enabling queries, enforcing integrity, and fine-grained access management.
    In Python, it's the metaclass for {class}`~lamindb.models.Registry` for {class}`~lamindb.models.SQLRecord`.

transform
    A piece of code (script, notebook, pipeline, function) that can be applied to input data to produce output data.

```
