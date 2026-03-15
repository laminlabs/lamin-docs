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
3. Navigate to `/transforms` page
4. Next to `Runs` on the right side of the page, select `Pipelines` to see all pipeline runs
5. Select your pipeline and version, e.g. ...
6. Click on `Launch` , you will be auto the **simplified view** as `Organization`, `Workspace` and `Compute environment` are auto-selected if there’s only one option.

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

1. Switch on the `Advanced view` toggle and you will see the `Configuration` session.
2. Click on `Settings` , you will see a pop-up window with 2 tabs: `Input schemas` and `Run metadata`
   1. `Input schemas` : You can configure a schema for a parameter (e.g. `input`), which allows you to create a sheet according to the schema configurations.
   2. `Run metadata` : You can configure which sheet you want to select the metadata from. Note a feature with the dtype that’s the same as the sheet must be present, meaning the feature selected must have `...` as the `dtype` if you want to use a sheet of type `...` in the Record registry.

## Step 0c: Configuration and Pipeline sessions - Advanced users

1. **Configuration**
   1. `pre-run script`, `post-run script` and `nextflow config` are automatically pulled from the selected `Compute environment`
   2. Check the `nf-lamin` plugin is specified in `nextflow config` (synced from the selected compute environment)
2. **Pipeline**
   1. `Pipeline URL` and `Revision` are specified in transform attributes, therefore immutable here (register a new transform if you want to run a different revision of the pipeline)
   2. `Workspace directory` is pre-filled from the compute environment
   3. Optional: select `Profiles`. For testing, can use `test` or `test_full` (multiple selection is possible). Once profiles are selected, you will see parameters automatically populated based on the profiles.
   4. Optional: enter a `Run name` if you don’t want use the default name

### Step 1: Launch a pipeline

1. Optional: enter a `Run name` if you don’t want use the auto-generated name
2. **Parameters** (`Form` or `JSON`)

   If one prefers, can directly edit the JSON without going through the form.

   1. Fill out run metadata if configured (See Step 0b-2 for configuration)
      1. Directly fill out the form
      2. Or click `Select existing row`
   2. Specify a file/artifact/sheet for parameters of type **file**
      1. Click on `select` to directly select a sheet, an artifact, or a file from the s3.
      2. Or click the `Create sheet` button to fill out a new sheet.
   3. Fill out the rest required fields marked with **\***, e.g. `input` and `outdir` for the scrnaseq pipeline
   4. Optional: provide the rest of parameters. Note: we group everything other than `input_output_options` and `mandatory_arguments` as advanced, if you want them to show up as the first session, you can group them under `input_output_options`.

### Step 2: Review and submit to Seqera

1. Click `Review` button at the bottom of the page
2. Review all the information you entered (can go back to edit if needed)
3. Click on `Submit` to send the launch request to Seqera
4. You will be see a success message if things go well (otherwise error messages) and a run id.
5. You can check the triggered run on Seqera: ...
6. Once the pipeline run started, `nf-lamin` automatically tracks the run status. You can view them on the runs list.
