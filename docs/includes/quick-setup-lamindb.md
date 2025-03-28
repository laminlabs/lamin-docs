For setup, install the `lamindb` Python package and connect to a LaminDB instance.

```shell
pip install 'lamindb[jupyter,bionty]'  # support notebooks & biological ontologies
lamin login  # <-- you can skip this for local & self-hosted instances
lamin connect account/instance  # <-- replace with your instance
```

<div style="height: 0.5em;"></div>

:::{dropdown} I don't have write access to an instance.

Here's how to create a local instance.

```shell
lamin init --storage ./mydata --modules bionty
```

:::
