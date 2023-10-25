# Glossary

```{glossary}

label
    A label refers to a descriptor or tag that is assigned to something to describe, identify, or categorize it.

feature
    A feature is an individual measurable property of a phenomenon [[Wikipedia](https://en.wikipedia.org/wiki/Feature_(machine_learning))], a measured event like a microscopy image or transcriptomic readout of a biological system.

    It's equivalent to the term "independent {term}`variable`" in statistics, but is the preferred term to denote dimensions of "feature spaces" in machine learning.

observation
    In statistics (machine learning), an observation refers to a particular measured instance of a set of random variable.

    In biology, an observation typically corresponds to measuring (reading out) a set of properties from a biological sample.

record
    A record is a data structure that consists in [fields](https://en.wikipedia.org/wiki/Field_(computer_science)), typically of different types but in a fixed sequence [[Wikipedia](https://en.wikipedia.org/wiki/Record_(computer_science))].

    Importantly, we refer to instances of `SQLModel` as records. Once a record is inserted into a database table, it becomes a row in that table.
    Every `SQLModel` class (in LaminDB) has a 1:1 correspondence with a database table and a pydantic `BaseModel`, every row in a database table has a 1:1 correspondence with a record.

    A record often stores jointly measured {term}`variables <variable>` in its fields, but in general allows updating fields when more information becomes available or changes.

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

```
