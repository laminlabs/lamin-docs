# Glossary

```{glossary}

artifact
    Stores a dataset or model as a file or folder. Is the output of a (tracked or untracked) process.

curator
    - Object designed to ensure your dataset conforms with a desired schema.
    - Helps with validation, standardization (e.g., by fixing typos or mapping synonyms), and annotation (linking it against metadata entities so that it becomes queryable).

FAIR
    FAIR data is data which meets the principles of findability, accessibility, interoperability, and reusability [wikipedia](https://en.wikipedia.org/wiki/FAIR_data).

feature
    A feature is a property of a measurement [[Wikipedia](https://en.wikipedia.org/wiki/Feature_(machine_learning))]. It's equivalent to a {term}`variable` in statistics and is typically equated with a dimension of a dataset.

    LaminDB comes with a {class}`~lamindb.Feature` registry to organize dataset dimensions and equates them with statistical variables.

GUI
    Graphical user interface, for instance, a browser-based data catalog.

instance
    Shorthand for "LaminDB instance", a database that manages metadata for datasets in different storage locations.

label
    A label in LaminDB is an entity in a registry -- e.g. a sample, cell type, or perturbation -- that can be linked to another entity -- e.g. a dataset or model.

lakehouse
    A data lakehouse combines the flexibility and cost-effectiveness of a data lake with schema management to enable structured analytics similar to what's possible in a data warehouse.
    In addition, data lakehouses typically come with ACID guarantees on transactions, making
    data corruption due to failed transactions impossible.
    Finally, a data lakehouse typically provides indexes into datasets so that a query doesn't require full scans of datasets.
    The industry standard for creating schema management, ACID, and indexes on top of a table that's represented as parquet files is [Apache Iceberg](https://iceberg.apache.org/).
    Early lakehouse frameworks include Databricks' [Delta Lake](https://delta.io/), Google's [BigLake](https://cloud.google.com/biglake), Amazon's [Lake Formation](https://aws.amazon.com/lake-formation/), [Dremio](https://www.dremio.com/), [Starburst](https://www.starburst.io/) and others. Here is a [blog post](https://cloud.google.com/blog/products/data-analytics/unify-data-lakes-and-warehouses-with-biglake-now-generally-available) from Google, a [blog post](https://aws.amazon.com/blogs/big-data/build-a-lake-house-architecture-on-aws/) from AWS, a [glossary entry](https://www.databricks.com/glossary/data-lakehouse) and a [paper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) from Databricks.

ORM
    Object-relational mapper. In LaminDB every sub-class of `Record` (every instance of `Registry`) is an ORM model that corresponds to a SQL table in the underlying metadata database [wikipedia](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping).

observation
    In statistics (machine learning), an observation refers to a particular measured instance of a set of random variables.

    In biology, an observation typically corresponds to measuring (reading out) a set of properties from a biological sample.

record
    A record is a data structure that consists of a sequence of typed [fields](https://en.wikipedia.org/wiki/Field_(computer_science)) that hold values [[Wikipedia](https://en.wikipedia.org/wiki/Record_(computer_science))].

    In LaminDB, any metadata record -- including {class}`~lamindb.Artifact`, {class}`~lamindb.Transform`, {class}`~lamindb.Run`, etc. -- is modeled as a {class}`~lamindb.models.SQLRecord` and is stored in a row in a table in the SQL database. LaminDB also comes with a class to dynamically model records, {class}`~lamindb.Record`. This is useful for describing more frequently changing dataset schemas, for example, the columns in dynamically ingested parquet files or dynamically created sheets. While changing the fields of a `SQLRecord` requires updating its Python data model definition and running a migration in the SQL database, changing the features of a `Record` can be done dynamically.

sample
    In biology, a sample is an instance or part of a biological system.

    In statistics (machine learning), a sample is an observation of a set of random variables (features, labels, metadata).

    Depending on the observational unit chosen for representing data, the statistical sample might correspond 1:1 to a biological sample.
    Often, this choice presents interesting cases, as variation across physical samples -- targeted in the experimental design -- can be directly explained by variation across statistical (digital) samples.

variable
    We almost always mean "random variable", when we say "variable".

    Random variables and their observations are core to statistics [[Wikipedia](https://en.wikipedia.org/wiki/Random_variable)].

    An independent variable is sometimes called a {term}`feature`, "predictor variable", "regressor", "covariate", "explanatory variable", "risk factor", "input variable", among others [[Wikipedia](https://en.wikipedia.org/wiki/Dependent_and_independent_variables)].

    A dependent variable is sometimes called a "response variable", "regressand", "criterion", "predicted variable", "measured variable", "explained variable", "experimental variable", "responding variable", "outcome variable", "output variable", "target" or "label".

schema
    A schema is a blueprint for your data's structure and a tool for curating and validating the organization of your data, helping maintain data integrity as it evolves through various processing steps.

registry
    A table in a SQL database (SQLite/Postgres) holding records, enabling queries, enforcing integrity, and fine-grained access management.

transform
    A piece of code (script, notebook, pipeline, function) that can be applied to input data to produce output data.

```
