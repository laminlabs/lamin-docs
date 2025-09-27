<!-- this is in sync with what's on the README -->

Install the `lamindb` Python package:

```shell
pip install lamindb
```

Create a LaminDB instance:

```shell
lamin init --storage ./quickstart-data  # or s3://my-bucket, gs://my-bucket
```

Or if you have write access to an instance, connect to it:

```shell
lamin connect account/name
```
