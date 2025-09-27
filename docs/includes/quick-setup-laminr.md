Install the `laminr` package.

```R
install.packages("laminr", dependencies = TRUE)
```

Create a LaminDB instance:

```R
laminr::lamin_init(storage = "./mydata", modules = c("bionty"))
```

Or if you have write access to an instance, login and connect to it:

```
laminr::lamin_login()
laminr::lamin_connect("<account>/<instance>")
```
