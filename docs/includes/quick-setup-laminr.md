Install the `laminr` package.

```R
install.packages("laminr", dependencies = TRUE)
```

Create a LaminDB instance:

```R
lc <- import_module("lamin_cli")
lc$init(storage = "./mydata", modules = "bionty")
```

Or if you have write access to an instance, login and connect to it:

```R
lc$login()
lc$connect("<account>/<instance>")
```
