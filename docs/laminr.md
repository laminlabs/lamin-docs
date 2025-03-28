# `laminr`

R client for LaminDB [source](https://github.com/laminlabs/laminr).

```{include} includes/setup-laminr.md

```

In an R session, create the central API object as follows.

```{r import-lamindb}
library(laminr)

ln <- import_module("lamindb")
```

The `ln` object offers the full `lamindb` API and can be used in the same way up to replacing `.` with `$`.
