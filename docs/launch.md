# Launch computational pipelines

## Configure your Seqera workspace

- If your pipeline is from private GitHub repos, make sure you add Workspace credentials to allow access
- Create a new `Compute environment` with that includes:
  - `LAMIN_API_KEY` : as an env variable
  - If you want to use `nf-lamin`, add the following content to the `nextflow config`

    ```jsx
    plugins {
      id 'nf-lamin'
    }

    lamin {
      instance = "{instance-full}"
      env = "{env}"
      api_key = System.getenv("LAMIN_API_KEY")
      transform_uid = "{transform-uid}"
      run_uid = "{run-uid}"
    }
    ```

## Walkthrough

### Step 0: Navigate to a pipeline

1. Navigate to a database, e.g. [https://lamin.ai/laminlabs/lamindata](https://lamin.ai/laminlabs/lamindata)
2. Make sure you have `write` or `admin` access to the database
   - `read` access won’t be able to launch pipelines or edit sheets
   - only `admin` can configure Pipeline settings on the launch page (advanced view)
3. Navigate to `/transforms` page, e.g. [https://lamin.ai/laminlabs/lamindata/transforms](https://lamin.ai/laminlabs/lamindata/transforms)
4. Next to `Runs` on the right side of the page, select `Pipelines` to see all pipeline runs
5. Select your pipeline and version, e.g. [nf-core/scrnaseq](https://lamin.ai/laminlabs/lamindata/transform/PhX5TXQhj3l6wowC)
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/tSUdXKBMpm9Z7tbv0000.png" style="width: 80%;"/>
6. Click on `Launch` , you will be auto-directed to the launch page. Provide your "Seqera API token" and then choose the `Organization`, `Workspace` and `Compute environment`. You can also choose to "Remember this token" if you want to avoid entering the token every time.
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/3KMXObe6NemRo41j0000.png" style="width: 80%;"/>

### Step 0a: Register a pipeline as a new transform - Admin

- To register a new pipeline or a new version of an existing pipeline, (please always use `Transform.from_git()` , here is the [API doc](https://docs.lamin.ai/lamindb.transform#lamindb.Transform.from_git))

  ```python
  # a versioned pipeline transform that points to a commit
  ln.Transform.from_git(
      url="https://github.com/nf-core/scrnaseq",
      path="main.nf",  # Path to the main script within the repository
      key="nf-core/scrnaseq",  # Optional key for the transform
      version="4.0.0",  # Optional version tag to checkout in the repository
  ).save()

  # a sliding pipeline transform that points to a branch
  ln.Transform.from_git(
      url="https://github.com/nf-core/scrnaseq",
      path="main.nf",  # Path to the main script within the repository
      key="nf-core/scrnaseq",  # Optional key for the transform
      version="dev",  # Version tag needs to equal branch
      branch="dev",  # Branch to checkout
  ).save()
  ```

### Step 0b: Configure the settings of a pipeline - Admin

1. Switch on the `Show configuration` toggle and you will see the `Configuration` session.
2. Click on `Settings`, you will see a pop-up window with 3 tabs: `Input schemas`, `Run metadata` and `Environment defaults`.
   1. `Input schemas`: You can configure a schema for a parameter (e.g. `input`), which allows you to create a sheet according to the schema configurations.
      <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/F4VVXZREJxTTMlxP0000.png" style="width: 80%;"/>
   2. `Run metadata`: You can configure which sheet you want to select the metadata from.
      <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/xEoxgY2NSBEucKzw0000.png" style="width: 80%;"/>
   3. `Environment defaults` : You can configure the environment defaults for the pipeline.
      <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/5shVPlptFMqymEdm0000.png" style="width: 80%;"/>

## Step 0c: Configuration and Pipeline sessions - Advanced users

1. **Configuration**

   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/qA0n4h9t9uGwbyUl0000.png" style="width: 80%;"/>
   1. `pre-run script`, `post-run script` and `nextflow config` are automatically pulled from the selected `Compute environment`
   2. Check the `nf-lamin` plugin is specified in `nextflow config` (synced from the selected compute environment)

2. **Pipeline**

   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/Vs0VyQsuDHZA3fKp0000.png" style="width: 80%;"/>
   1. `Pipeline URL` and `Revision` are specified in transform attributes, therefore immutable here (register a new transform if you want to run a different revision of the pipeline)
   2. `Workspace directory` is pre-filled from the compute environment
   3. Optional: select `Profiles`. Once profiles are selected, you will see parameters automatically populated based on the profiles.
   4. Optional: enter a `Run name` if you don’t want use the default name

### Step 1: Launch a pipeline

1. Optional: enter a `Run name` if you don’t want use the auto-generated name (in form of `{transform-key}-{run-number}`)
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/qzJycfLYDF4633We0000.png" style="width: 80%;"/>
2. **Parameters** (`Form` or `JSON`)

   If one prefers, can directly edit the JSON without going through the form.
   1. Fill out `Run metadata` if configured (see Step 0b-2 for configuration)
      1. Directly fill out the form via `+ Record`
         <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/23tmjAnGkC33Ynkp0000.png" style="width: 80%;"/>
      2. Or click `Select` to select an existing row from a sheet
         <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/8WlDJtu6lWfrUXtJ0000.png" style="width: 80%;"/>
   2. Specify a file/artifact/sheet for parameters of type **file**
      1. Click on `Select` to directly select a sheet, an artifact, or a file from the s3.
         <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/EAhZBrhfYDXHDlmO0000.png" style="width: 80%;"/>
      2. For parameters configured via `Input schemas`, click the `+ Create` button to fill out a new sheet.
         <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/zpPHRNTqRHyUenAK0000.png" style="width: 80%;"/>
   3. Fill out the rest required fields marked with **\***, e.g. `outdir` for the scrnaseq pipeline
   4. Optional: provide the rest of parameters.

### Step 2: Review and submit to Seqera

1. Click `Review and Submit` at the bottom of the page
2. Review all the information you entered (can go back to edit if needed)
   <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/vSPVCzF3h85QZZOV0000.png" style="width: 80%;"/>
3. Click on `Submit` to send the launch request to Seqera
4. You will be see a success message if things go well (otherwise error messages) and a run id.
5. You can check the triggered run on your Seqera platform.
6. Once the pipeline run started, `nf-lamin` automatically tracks the run status. You can view them on the runs list.
