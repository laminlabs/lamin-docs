For setup, install the `laminr` and `lamindb` packages and connect to a LaminDB instance.

```R
install.packages("laminr", dependencies = TRUE)  # install the laminr package from CRAN
laminr::install_lamindb(extra_packages = c("bionty"))  # install lamindb & bionty for use via reticulate
laminr::lamin_login()  # <-- you can skip this for local & self-hosted instances
laminr::lamin_connect("<account>/<instance>")  # <-- replace with your instance
```

<div style="height: 0.5em;"></div>

:::{dropdown} I don't have write access to an instance.

Here's how to create a local instance.

```R
laminr::lamin_init(storage = "./mydata", modules = c("bionty"))
```

:::
