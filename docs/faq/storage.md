# Storage FAQ

## What is the default storage location?

It's the directory or cloud bucket that you pass when initializing a LaminDB instance:

```bash
lamin init --storage ./default-storage  # or s3://default-bucket or gs://default-bucket
```

It's easiest to see and update default storage in the Python API ({attr}`~lamindb.dev.Settings.storage`):

```python
import lamindb as ln
ln.settings.storage  # set via ln.settings.storage = "s3://other-bucket"
#> s3://default-bucket
```

You can also change it using the CLI via

```
lamin set --storage s3://other-bucket
```

## Where is my SQLite file?

The SQLite file is in the default storage location of the instance and name `f'{instance_name}.lndb'`.

You can see it as part of the database connection string:

```
ln.setup.settings.instance.db
#> sqlite:///path-to-sqlite
```

If default storage is in the cloud, the SQLite file is cached in the local cache directory ({attr}`~lamindb.setup.dev.StorageSettings.cache_dir`):

```
ln.setup.settings.storage.cache_dir
#> path-to-cache-dir
```

## What happens if I move the `.lndb` file around?

The SQLite file has to remain in the default storage location of the instance.

You can, however, take the SQLite file and place it in a new location (`./mydir`, `s3://my-bucket`) and create a new LaminDB instance passing `--storage ./mydir` (or `--storage s3://my-bucket`). All your metadata is then present in the new instance.

## What is the `.lamindb/` directory?

It stores files that are merely referenced by metadata ({attr}`~lamindb.File.key` is `None`).

There is only a single `.lamindb/` directory per LaminDB instance.

## What should I do if I want to bulk migrate files to another storage (let’s say another s3 bucket)?

Currently, you can only achieve this manually:

1. Copy or move files into the desired new storage location
2. Adapt the corresponding record in the {class}`~lamindb.Storage` registry by setting the `root` field to the new location

## When should I pass `key` and when should I rely purely on metadata to register a file?

The recommended way of making files findable in LaminDB is to link them to labels and use the {attr}`~lamindb.File.description` field.

When you're registering existing data, however, they'll often come with a semantic `key`, defined as the relative path within the storage location.

## Will I never be able to find my file if I don’t give it a description?

## What should I do if I have a local file and want to upload it to S3? (Shall I register a File first and upload it with `.save`, or shall I upload outside of Lamin before registering it?)

## How to update a file in storage? What’s the process to update file records after I moved files around or updated files?

## How do I version a file? Do I always make a new file record and a new transform if I want to track the parent files?
