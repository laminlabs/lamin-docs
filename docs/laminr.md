# `laminr`

R client for LaminDB [source](https://github.com/laminlabs/laminr).

```{include} includes/setup-laminr.md

```

```{r disconnect, include = FALSE}
# Disconnect from this instance at the end of the vignette
withr::defer(laminr::lamin_disconnect())
```

# Import

To start working with **{laminr}**, import the **lamindb** module:

```{r import-lamindb}
ln <- import_module("lamindb")
```

This is equivalent to `import lamindb as ln` in Python.
