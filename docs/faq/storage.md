# Storage FAQ

## What is the default storage location?

It's the directory or cloud bucket that you pass when initializing a LaminDB instance:

```bash
lamin init --storage ./default-storage  # or s3://default-bucket or gs://default-bucket
```

You can see and change it in the Python API using :attr:`~lamindb.Settings.storage`:

```python
import lamindb as ln
ln.settings.storage  # or set a value via ln.settings.storage = "s3://other-bucket"
#> s3://default-bucket
```

You can also change it using the CLI via

```
lamin set --storage s3://other-bucket
```

## Where is my SQLite file? What happens if I move the `.lndb` file around?

## What is the `.lamindb/` folder? Will there be multiple `.lamindb/` folders if I have multiple storage locations?

## What happens if I move files around? What should I do if I want to bulk migrate files to another storage (let’s say another s3 bucket)?

## When should I pass `key=` and when should I rely on cryptic ids to register a file? What’s the recommended process to register a file?

## Will I never be able to find my file if I don’t give it a description? (should this even be allowed?)

## What should I do if I have a local file and want to upload it to S3? (Shall I register a File first and upload it with `.save`, or shall I upload outside of Lamin before registering it?)

## How to update a file in storage? What’s the process to update file records after I moved files around or updated files?

## How do I version a file? Do I always make a new file record and a new transform if I want to track the parent files?
