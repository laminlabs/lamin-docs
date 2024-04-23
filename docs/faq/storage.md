# Storage FAQ

Often, one works with temporary files but ultimately wants to store them in persistent storage locations, typically in the cloud. Hence, LaminDB comes with

1. a default storage location for persisting data
2. a registry for managing storage locations: {class}`~lamindb.Storage`

## What is the default storage location?

It's the directory or cloud bucket that you pass when initializing a LaminDB instance:

```bash
lamin init --storage ./default-storage  # or s3://default-bucket or gs://default-bucket
```

It's easiest to see and update default storage in the Python API ({attr}`~lamindb.core.Settings.storage`):

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

The SQLite file is in the default storage location of the instance and called: `f"{instance_name}.lndb"`

You can also see it as part of the database connection string:

```python
ln.setup.settings.instance.db
#> sqlite:///path-to-sqlite
```

If default storage is in the cloud, the SQLite file is cached in the local cache directory ({attr}`~lamindb.setup.core.StorageSettings.cache_dir`):

```python
ln.setup.settings.storage.cache_dir
#> path-to-cache-dir
```

## What happens if I move the SQLite `.lndb` file around?

The SQLite file has to remain in the default storage location of the instance.

You can, however, take the SQLite file and place it in a new location (`./mydir`, `s3://my-bucket`) and create a new LaminDB instance passing `--storage ./mydir` (or `--storage s3://my-bucket`). All your metadata is then present in the new instance.

## What is the `.lamindb/` directory?

It stores files that are merely referenced by metadata (the `key` field of {attr}`~lamindb.Artifact` is `None`).

There is only a single `.lamindb/` directory per LaminDB instance.

## What should I do if I want to bulk migrate files to another storage?

Currently, you can only achieve this manually:

1. Copy or move files into the desired new storage location
2. Adapt the corresponding record in the {class}`~lamindb.Storage` registry by setting the `root` field to the new location

## When should I pass `key`, and when should I rely purely on metadata to register a file?

The recommended way of making files findable in LaminDB is to link them to labels and use the `description` field of {attr}`~lamindb.Artifact`.
Generally, we discourage the usage of semantic `keys` for files due to the need for standards and potential ambiguity.

## How does LaminDB store existing (legacy) data

Existing data is often stored in hierarchical structures with semantic folder names.
Hence, LaminDB automatically stores such data with a semantic `key` (the relative path within the storage location) upon saving and overwrites the default set by {attr}`~docs:lamindb.core.Settings.artifact_use_virtual_keys`.

## Will I never be able to find my file if I don’t give it a description?

You can't create files that have _none_ of `description`, `key` and `run` set.
Hence, you will always be able to find your find through either of these or
through additional metadata.

## What should I do if I have a local file and want to upload it to S3?

You can either create a file object from the local file and auto-upload it to the cloud during `file.save()`:

```python
artifact = ln.Artifact(local_filepath)
artifact.save()  # this will upload to the cloud
```

You can also create a file object from an existing cloud path:

```python
artifact = ln.Artifact("s3://my-bucket/my-file.csv")
artifact.save()  # this will only save metadata as the file is already in registered storage
```

This enables to use any tool to move data into the cloud.

## How to replace an artifact in storage?

```python
artifact.replace(new_data)
```

## How to update metadata of an artifact?

You can edit metadata of the artifact by querying it and then resetting its attributes. For instance,

```python
artifact.description = "My new description"
artifact.save()  # save the change to the database
```

## What should I do if I accidentally delete a file from storage?

`Artifact` and `Dataset` records follow a "trash" behavior as many file systems. When you perform `file.delete()`, the record is moved into a "trash" from which it can be restored. Deleting an artifact from the trash triggers a permanent delete:

- prompt to ask if user wants to delete the metadata record
- prompt to ask if user wants to delete the file from storage if semantic key is used (otherwise the file is automatically deleted from the storage)

If you delete an artifact from storage outside LaminDB, you are left with a file record without valid storage. In this case, you can:

- use `ln.delete(permanent=True)` to delete the file record from database
- alternatively, if you'd like to keep the record, link the storage back via `file.cache()`

```python
file.description = "My new description"
file.save()  # save the change to the database
```

## How do I version a file?

You use the `is_new_version_of` parameter:

```python
new_artifact = ln.Artifact(df, is_new_version_of=old_file)
```

Then, `new_artifact` automatically has the `version` field set, incrementing the version number by one.

You can also pass a custom version:

```python
new_artifact = ln.Artifact(df, version="1.1", is_new_version_of=old_file)
```

It doesn't matter which old version of the file you use, any old version is good!

## How to set up a public read-only instance on an s3 bucket?

For a public read-only instance the bucket should have certain policies configured.
You can read about s3 bucket policies [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html). For a public read-only instance the bucket should have `s3:GetObject` and `s3:ListBucket` permissions. The example policy is given below:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AddPerm",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    },
    {
      "Sid": "AllowList",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::your-bucket-name"
    }
  ]
}
```

Change `your-bucket-name` above to the name of your s3 bucket.
