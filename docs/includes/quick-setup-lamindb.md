<!-- this is roughly in sync with what's on the README -->

Install the `lamindb` Python package:

```shell
pip install 'lamindb[jupyter,bionty]'  # support notebooks & biological ontologies
```

Either connect to a LaminDB instance for which you have write access:

```shell
lamin connect account/name
```

Or create a local instance:

```shell
lamin init --storage ./quickstart-data
```
