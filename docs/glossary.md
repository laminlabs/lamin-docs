# Glossary

```{glossary}

FAIR
    FAIR data is data which meets the principles of findability, accessibility, interoperability, and reusability [wikipedia](https://en.wikipedia.org/wiki/FAIR_data).

UI
    Graphical user interface, for instance, a browser-based data catalog.

feature
    A feature is a property of a measurement [[Wikipedia](https://en.wikipedia.org/wiki/Feature_(machine_learning))]. It's equivalent to a {term}`variable` in statistics and is typically equated with a dimension of a dataset.

    LaminDB comes with a {class}`~lamindb.Feature` registry to organize dataset dimensions and equates them with statistical variables.

label
    A label refers to a descriptor or tag that is assigned to something to describe, identify, or categorize it.

lakehouse
    A data lakehouse combines the flexibility and cost-effectiveness of a data lake with the data management and ACID transaction support of a data warehouse, enabling both structured and unstructured data analytics in a single framework. Lakehouse frameworks include Databrick's [Delta Lake](https://delta.io/), Google's [BigLake](https://cloud.google.com/biglake), Amazon's [Lake Formation](https://aws.amazon.com/lake-formation/), [Dremio](https://www.dremio.com/), [Starburst](https://www.starburst.io/) and others. Here is a [blog post](https://cloud.google.com/blog/products/data-analytics/unify-data-lakes-and-warehouses-with-biglake-now-generally-available) from Google, a [blog post](https://aws.amazon.com/blogs/big-data/build-a-lake-house-architecture-on-aws/) from AWS, a [glossary entry](https://www.databricks.com/glossary/data-lakehouse) and a [paper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) from Databricks.

ORM
    Object-relational mapper. In LaminDB every sub-class of `Record` (every instance of `Registry`) is an ORM that corresponds to a SQL table in the underlying metadata database [wikipedia](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping).

observation
    In statistics (machine learning), an observation refers to a particular measured instance of a set of random variable.

    In biology, an observation typically corresponds to measuring (reading out) a set of properties from a biological sample.

record
    A record is a data structure that consists in a sequence of typed [fields](https://en.wikipedia.org/wiki/Field_(computer_science)) that hold values [[Wikipedia](https://en.wikipedia.org/wiki/Record_(computer_science))].

    In LaminDB, a metadata record is modeled as a {class}`~lamindb.models.Record`.

sample
    In biology, a sample is an instance or part of a biological system.

    In statistics (machine learning), a sample is an observation of a set of random variables (features, labels, metadata).

    Depending on the observational unit chosen for representing data, the statistical sample might correspond 1:1 to a biological sample.
    Often, this choice presents an interesting cases, as variation across physical samples - targeted in the experimental design - can directly be explained by variation across statistical (digital) samples.

variable
    We almost always mean "random variable", when we say "variable".

    Random variables and their observations are core to statistics [[Wikipedia](https://en.wikipedia.org/wiki/Random_variable)].

    An independent variable is sometimes called a {term}`feature`, "predictor variable", "regressor", "covariate", "explanatory variable", "risk factor", "input variable", among others [[Wikipedia](https://en.wikipedia.org/wiki/Dependent_and_independent_variables)].

    A dependent variable is sometimes called a "response variable", "regressand", "criterion", "predicted variable", "measured variable", "explained variable", "experimental variable", "responding variable", "outcome variable", "output variable", "target" or "label".

schema
    Blueprint for your data’s structure. Tool for curating and validating the organization of your data, helping maintain data integrity as it evolves through various processing steps.

curator
    - Object class designed to ensure your dataset conforms to a desired schema. 
    - Helps with validation, standardization (e.g., by fixing typos or mapping synonyms), and annotation (linking it against metadata entities so that it becomes queryable).

registry
    - A specialized kind of Record that represents a table in the metadata SQL database. A record is an instance (or row) of that registry.
    - It automatically sets up important behaviors and methods (like filtering, querying, and converting records to DataFrames) needed to interact with the metadata database.

instance
    A database that manages metadata for datasets in different storage locations.

transform
    A piece of code (script, notebook, pipeline, function) that can be applied to input data to produce output data.

artifact
    Stores a dataset or model as a file or folder.

```
