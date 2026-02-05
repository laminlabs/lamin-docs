import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import nox
from dirsync import sync
from laminci import convert_executable_md_files, run_notebooks
from laminci.nox import install_lamindb, run, run_pre_commit

current_dir = Path(__file__).parent.resolve()
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

# has to come after updating sys.path because local in this repo
from laminr_converter import convert_markdown_python_to_tabbed

IS_PR = os.getenv("GITHUB_EVENT_NAME") == "pull_request"

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


README0_ORIG = """<details>
<summary>Why?</summary>"""

README0_REPLACE = """```{dropdown} Why?"""

README1_ORIG = """</details>

<img width="800px" src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/BunYmHkyFLITlM5M000C.svg">

Highlights:"""

README1_REPLACE = """```

<img width="800px" src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/BunYmHkyFLITlM5M000C.svg">

```{dropdown} DB highlights"""

README2_ORIG = """
If you want a GUI: [LaminHub](https://lamin.ai) is a data collaboration hub built on LaminDB similar to how GitHub is built on git.

<details>
<summary>Who uses it?</summary>"""

README2_REPLACE = """```

LaminHub is a data collaboration hub built on LaminDB similar to how GitHub is built on git.

:::{dropdown} Hub highlights

```{include} includes/specs-laminhub.md
```

:::

```{dropdown} Who uses it?"""


README3_ORIG = """</details>

## Docs

Copy [llms.txt](https://docs.lamin.ai/llms.txt) into an LLM chat and let AI explain or read the [docs](https://docs.lamin.ai)."""

README3_REPLACE = """```

**Tip:** Copy [llms.txt](https://docs.lamin.ai/llms.txt) into an LLM chat and let AI explain."""


README4_ORIG = """
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
"""

README4_REPLACE = """
::::{tab-set}
:::{tab-item} Py
:sync: python

```{include} includes/quick-setup-lamindb.md
```

:::
:::{tab-item} R
:sync: r

```{include} includes/quick-setup-laminr.md
```
:::
::::
"""


def replace_content(filename: Path, mapped_content: dict[str, str]) -> None:
    with open(filename) as f:
        content = f.read()
    with open(filename, "w") as f:
        for key, value in mapped_content.items():
            content = content.replace(key, value)
        f.write(content)


def add_line_after(content: str, after: str, new_line: str) -> str:
    lines = content.splitlines()

    for line_idx, line in enumerate(lines):
        if after in line:
            lines.insert(line_idx + 1, new_line)
            break

    return "\n".join(lines)


def pull_from_s3_and_unpack(zip_filename) -> None:
    subprocess.run(
        f"aws s3 cp s3://lamin-site-assets/docs/{zip_filename} {zip_filename}",
        shell=True,
    )
    shutil.unpack_archive(zip_filename, zip_filename.replace(".zip", ""))


def sync_path(path, target_path):
    if target_path.exists():
        if target_path.is_dir():
            shutil.rmtree(target_path)
        else:
            target_path.unlink()
    path.rename(target_path)


@nox.session
def pull_artifacts(session):
    # git
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/laminlabs/schmidt22/main/README.md",
        "docs/schmidt22.md",
    )

    # lamindb
    pull_from_s3_and_unpack("lamindb.zip")
    Path("lamindb/README.ipynb").unlink()
    Path("lamindb/README.md").rename("docs/includes/README.md")
    Path("lamindb/conf.py").unlink()
    Path("lamindb/changelog.md").unlink()
    Path("lamindb/api.md").unlink()
    Path("lamindb/guide.md").unlink()
    for path in Path("lamindb").glob("*"):
        if (
            path.name == "index.md"
            or path.name in {"storage", "storage.md"}  # not user facing
            or path.name == "faq"  # directory treated below
        ):
            continue
        print("syncing", path)
        if path.is_dir():
            sync(path, Path("docs") / path.name, "sync", create=True, ctime=True)
        else:
            sync_path(path, Path("docs") / path.name)

    replace_content("docs/cli.md", {"# `CLI`": "# CLI"})
    replace_content("docs/lamindb.md", {"# `lamindb`": "# Python: `lamindb`"})

    # lamindb faq
    Path("docs/faq/").mkdir(exist_ok=True, parents=True)
    for path in Path("lamindb/faq").glob("*"):
        sync_path(path, Path("docs/faq") / path.name)

    # laminr
    pull_from_s3_and_unpack("laminr.zip")
    Path("laminr/r-quickstart.R").rename("docs/includes/r-quickstart.R")

    # pipelines
    pull_from_s3_and_unpack("redun-lamin.zip")
    Path("redun-lamin/redun.ipynb").rename("docs/redun.ipynb")
    pull_from_s3_and_unpack("nf-lamin.zip")
    nf_lamin_files = [
        "nextflow.ipynb",
        "nextflow-postrun.ipynb",
        "register_scrnaseq_run.py",
        "nf_core_scrnaseq_diagram.png",
        "nf_core_scrnaseq_run.png",
        "nextflow-plugin-reference.md",
    ]
    for file in nf_lamin_files:
        Path(f"nf-lamin/{file}").rename(f"docs/{file}")
    pull_from_s3_and_unpack("snakemake-lamin.zip")
    Path("snakemake-lamin/bulk_rna_seq.ipynb").rename("docs/snakemake.ipynb")

    # mlops
    pull_from_s3_and_unpack("lamin-mlops.zip")
    Path("lamin-mlops/mnist.ipynb").rename("docs/mnist.ipynb")
    Path("lamin-mlops/wandb.ipynb").rename("docs/wandb.ipynb")
    Path("lamin-mlops/mlflow.ipynb").rename("docs/mlflow.ipynb")
    Path("lamin-mlops/autoencoder.py").rename("docs/autoencoder.py")
    Path("lamin-mlops/croissant.ipynb").rename("docs/croissant.ipynb")

    # cellxgene-lamin
    pull_from_s3_and_unpack("cellxgene-lamin.zip")
    for path in Path("cellxgene-lamin/").glob("*"):
        if path.name.endswith(("cellxgene.ipynb", "cellxgene-curate.ipynb")):
            sync_path(path, Path("docs") / path.name)

    # lamin-spatial
    pull_from_s3_and_unpack("lamin-spatial.zip")
    for path in Path("lamin-spatial/").glob("*"):
        if path.name == "rxrx.ipynb":
            sync_path(path, Path("docs") / path.name)
        elif path.name == "vitessce.ipynb":
            sync_path(path, Path("docs") / path.name)
        elif path.name == "vitessce2.ipynb":
            sync_path(path, Path("docs") / path.name)

    # use-cases
    pull_from_s3_and_unpack("lamin-usecases.zip")
    for path in Path("lamin-usecases/").glob("*"):
        if (
            path.name == "index.md"
            or path.name == "usecases.md"
            or path.name == "changelog.md"
            or path.name == "conf.py"
            or path.name == "trace-data-code.md"
            or path.name == "atlases.md"
        ):
            continue
        print("syncing", path)
        sync_path(path, Path("docs") / path.name)

    # amend README to serve as introduction.md
    with open("docs/includes/README.md") as f:
        content = f.read()
    with open("docs/includes/README.md", "w") as f:
        assert README0_ORIG in content  # noqa: S101
        assert README1_ORIG in content  # noqa: S101
        assert README2_ORIG in content  # noqa: S101
        assert README3_ORIG in content  # noqa: S101
        assert README3_ORIG in content  # noqa: S101
        content = content.replace(README0_ORIG, README0_REPLACE)
        content = content.replace(README1_ORIG, README1_REPLACE)
        content = content.replace(README2_ORIG, README2_REPLACE)
        content = content.replace(README3_ORIG, README3_REPLACE)
        content = content.replace(README4_ORIG, README4_REPLACE)
        content = convert_markdown_python_to_tabbed(content)
        f.write(content)


def strip_notebook_outputs(directory="."):
    """Simple function to strip outputs from all notebooks in directory."""
    notebook_files = list(Path(directory).rglob("*.ipynb"))

    if not notebook_files:
        print("No notebooks found")
        return

    for nb_file in notebook_files:
        subprocess.run(["nbstripout", str(nb_file)])

    print(f"Processed {len(notebook_files)} notebooks")


@nox.session
def install(session):
    branch = "main" if IS_PR else "main"
    if branch == "pypi":
        run(
            session,
            "uv pip install --system lamindb",
        )
    else:
        install_lamindb(
            session,
            branch=branch,
            target_dir="tmp_lamindb",
        )
    run(session, "uv pip install --system spatialdata")  # temporarily
    run(session, "uv pip install --system scanpy")
    run(session, "lamin settings set private-django-api true")


@nox.session
def run_nbs(session):
    convert_executable_md_files("docs")
    os.system("lamin init --storage ./test-quickstart --modules bionty")
    exit_status = os.system("python docs/includes/create-fasta.py")
    assert exit_status == 0  # noqa S101
    run_notebooks("docs/tutorial.ipynb")
    run_notebooks("docs/setup.ipynb")


@nox.session
def docs(session):
    subprocess.run(
        "lndocs --error-on-index",
        shell=True,
    )
    # if process.returncode != 0:
    #     # rerun without strict option so see all warnings
    #     run(session, "lndocs --error-on-index")
    #     # exit with error
    #     exit(1)

    # strip outputs for llms.txt
    os.system("rm -rf _docs_tmp")
    strip_notebook_outputs("docs")
    subprocess.run(
        "lndocs --format text --error-on-index",
        shell=True,
    )
