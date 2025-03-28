# `laminr`

R client for LaminDB [[source](https://github.com/laminlabs/laminr)].

```{include} includes/setup-laminr.md

```

In an R session, create the central API object as follows.

```R
library(laminr)
ln <- import_module("lamindb")
```

The `ln` object the offers the full `lamindb` API and can be used in the same way up to replacing Python's `.` with R's `$`.

In addition to `lamindb`'s functionality, `laminr` exposes some functionality of the CLI to ease managing the Python environment used by `reticulate`.

- `lamin_connect`
- `lamin_init`
- `lamin_delete`
- `lamin_disconnect`
- `lamin_login`
- `lamin_logout`
- `lamin_save`
- `install_lamindb`
