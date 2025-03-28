For setup, install the `lamindb` Python package and connect to a LaminDB instance.

```shell
pip install 'lamindb[jupyter,bionty]'  # support notebooks & biological ontologies
lamin login  # <-- you can skip this for public, local & self-hosted instances
lamin connect account/instance  # <-- replace with your instance
```

If you don't have write access to an instance, create a local instance.

```{r init}
lamin init --storage ./mydata --modules bionty
```
