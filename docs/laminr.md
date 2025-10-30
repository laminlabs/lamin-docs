# R: `laminr`

R client for LaminDB [[source](https://github.com/laminlabs/laminr)].

```{include} includes/quick-setup-laminr.md

```

For more detailed instructions, see {doc}`setup-laminr`.

In an R session, create the central API object as follows.

```R
library(laminr)
ln <- import_module("lamindb")
```

The `ln` object the offers the full `lamindb` API and can be used in the same way up to replacing Python's `.` with R's `$`.

To access the `lamin` CLI functionality, import the `lamin_cli` module:

```R
lc <- import_module("lamin_cli")

lc$init()
lc$connect()
lc$disconnect()
lc$login()
lc$logout()
lc$save()
lc$delete()
```

```{toctree}
:maxdepth: 1
:hidden:

setup-laminr.md
```
