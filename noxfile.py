import os
import shutil
import subprocess
from pathlib import Path

import lamindb as ln
import nox
from dirsync import sync
from laminci import run_notebooks
from laminci.nox import install_lamindb, login_testuser2, run, run_pre_commit

IS_PR = os.getenv("GITHUB_EVENT_NAME") == "pull_request"

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


# for Introduction & FAQ

INTRODUCTION = """
```{toctree}
:hidden:
:caption: Overview

introduction
tutorial
```
"""

FAQ_MATCH = """\
```
"""

# currently moot, because no additional FAQ content is here
FAQ_APPEND = """\
```
"""

# for Guide

ORIG_HOW_TO = """\
```{toctree}
:hidden:
:caption: "How to"

query-search
track
curate
bio-registries
transfer
```
"""

REPLACE_HOW_TO = """\
```{toctree}
:hidden:
:caption: "How to"

setup
query-search
track
curate
ontologies
transfer
```
"""


USECASES = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Use cases

atlases
../by-datatype
../by-registry
../data-flow
pipelines
mlops
visualization
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: The Hub

access
sheets
security
```

"""

BY_DATATYPE_ORIG = """
multimodal
ehr
```
"""

BY_DATATYPE = """
multimodal
perturbation
ehr
```
"""

# for other topics

OTHER_TOPICS_ORIG = """
```{toctree}
:hidden:
:caption: Other topics

faq
storage
"""

OTHER_TOPICS = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Other topics

design
hub
faq
influences
glossary
"""

README0_ORIG = """<details>
<summary>Why?</summary>"""

README0_REPLACE = """```{dropdown} Why?"""

README1_ORIG = """</details>

**Highlights.**"""

README1_REPLACE = """```

```{dropdown} Highlights"""

README2_ORIG = """
LaminDB can be connected to LaminHub to serve as a [LIMS](https://en.wikipedia.org/wiki/Laboratory_information_management_system) for wetlab scientists, closing the drylab-wetlab feedback loop: [lamin.ai](https://lamin.ai)

## Docs

Copy [summary.md](https://docs.lamin.ai/summary.md) into an LLM chat and let AI explain or read the [docs](https://docs.lamin.ai)."""

README2_REPLACE = """```

LaminHub is a data collaboration hub built on LaminDB similar to how GitHub is built on git.

:::{dropdown} Explore

```{include} includes/specs-laminhub.md

```

:::

You can copy this [summary.md](https://docs.lamin.ai/summary.md) into an LLM chat and let AI explain."""


README3_ORIG = """
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

README3_REPLACE = """
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


# below is needed if we have TOCs in notebooks

# def jsonify(text: str):
#     new_lines = []
#     # skip last line
#     for line in text.split("\n")[:-1]:
#         line = rf'    "{line}\n",'
#         new_lines.append(line)
#     return "\n".join(new_lines)


# USECASES = jsonify(USECASES_TEXT)
# OTHER_TOPICS_ORIG = jsonify(OTHER_TOPICS_ORIG_TEXT)
# OTHER_TOPICS = jsonify(OTHER_TOPICS_TEXT)


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
    subprocess.run(  # noqa S602
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
    # lamindb
    pull_from_s3_and_unpack("lamindb.zip")
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
    replace_content("docs/faq.md", {FAQ_MATCH: FAQ_APPEND})

    # laminr
    pull_from_s3_and_unpack("laminr.zip")
    Path("laminr/r-quickstart.R").rename("docs/includes/r-quickstart.R")

    # pipelines
    pull_from_s3_and_unpack("redun-lamin.zip")
    Path("redun-lamin/redun.ipynb").rename("docs/redun.ipynb")
    pull_from_s3_and_unpack("nextflow-lamin.zip")
    Path("nextflow-lamin/nf_core_scrnaseq.ipynb").rename("docs/nextflow.ipynb")
    Path("nextflow-lamin/register_scrnaseq_run.py").rename(
        "docs/register_scrnaseq_run.py"
    )
    pull_from_s3_and_unpack("snakemake_lamin_usecases_docs.zip")
    Path("snakemake_lamin_usecases_docs/bulk_rna_seq.ipynb").rename(
        "docs/snakemake.ipynb"
    )

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

    # use-cases
    pull_from_s3_and_unpack("lamin-usecases.zip")
    for path in Path("lamin-usecases/").glob("*"):
        if (
            path.name == "index.md"
            or path.name == "usecases.md"
            or path.name == "changelog.md"
            or path.name == "conf.py"
        ):
            continue
        print("syncing", path)
        sync_path(path, Path("docs") / path.name)

    replace_content("docs/by-datatype.md", {BY_DATATYPE_ORIG: BY_DATATYPE})

    # wetlab (must be after use-cases)
    # pull_from_s3_and_unpack("wetlab.zip")
    # sync_path(
    #     Path("wetlab/guide/pert-curator.ipynb"),
    #     Path("docs/perturbation.ipynb"),
    # )

    # amend toctree & README
    with open("docs/guide.md") as f:
        content = f.read()
    with open("docs/guide.md", "w") as f:
        content = content.replace("# Guide", "# Guide" + INTRODUCTION)
        content = content.replace(ORIG_HOW_TO, REPLACE_HOW_TO)
        content = content.replace(OTHER_TOPICS_ORIG, USECASES + OTHER_TOPICS)
        f.write(content)

    with open("docs/includes/README.md") as f:
        content = f.read()
    with open("docs/includes/README.md", "w") as f:
        assert README0_ORIG in content  # noqa: S101
        assert README1_ORIG in content  # noqa: S101
        assert README2_ORIG in content  # noqa: S101
        assert README3_ORIG in content  # noqa: S101
        content = content.replace(README0_ORIG, README0_REPLACE)
        content = content.replace(README1_ORIG, README1_REPLACE)
        content = content.replace(README2_ORIG, README2_REPLACE)
        content = content.replace(README3_ORIG, README3_REPLACE)
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
            "uv pip install --system lamindb[bionty,jupyter,gcp,wetlab]",
        )
    else:
        install_lamindb(
            session,
            branch=branch,
            extras="bionty,jupyter,gcp,wetlab",
            target_dir="tmp_lamindb",
        )
    run(session, "uv pip install --system spatialdata")  # temporarily
    run(session, "uv pip install --system scanpy")
    run(session, "lamin settings set private-django-api true")


@nox.session
def run_nbs(session):
    pass


@nox.session
def init(session):
    run(
        session,
        "lamin init --storage ./docsbuild --modules bionty,wetlab",
    )


@nox.session
def docs(session):
    # this testuser2 is only needed for writing to lamin-site-assets
    # testuser1 cannot have access to lamin-site-assets
    login_testuser2(session)
    process = subprocess.run(  # noqa S602
        "lndocs --strip-prefix --error-on-index",  # --strict back
        shell=True,
    )
    # if process.returncode != 0:
    #     # rerun without strict option so see all warnings
    #     run(session, "lndocs --strip-prefix --error-on-index")
    #     # exit with error
    #     exit(1)

    # now strip outputs for llms.txt
    os.system("rm -rf _docs_tmp")  # noqa S605 clean build directory
    strip_notebook_outputs("docs")

    Path("docs/changelog/2022.md").unlink()
    Path("docs/changelog/2023.md").unlink()
    Path("docs/changelog/2024.md").unlink()
    Path("docs/changelog/2025.md").unlink()
    Path("docs/changelog/soon.md").unlink()

    # Use cases
    Path("docs/sc-imaging.ipynb").unlink()
    Path("docs/sc-imaging2.ipynb").unlink()
    Path("docs/sc-imaging3.ipynb").unlink()
    Path("docs/sc-imaging4.ipynb").unlink()
    Path("docs/project-flow-scripts/integrated-analysis.ipynb").unlink()
    Path("docs/project-flow-scripts/hit-identification.ipynb").unlink()
    Path("docs/facs.ipynb").unlink()
    Path("docs/facs2.ipynb").unlink()
    Path("docs/facs3.ipynb").unlink()
    Path("docs/facs4.ipynb").unlink()
    Path("docs/celltypist.ipynb").unlink()
    Path("docs/data-flow.md").unlink()
    Path("docs/enrichr.ipynb").unlink()
    # Path("docs/perturbation.ipynb").unlink()
    Path("docs/rdf-sparql.ipynb").unlink()
    Path("docs/project-flow.ipynb").unlink()
    Path("docs/analysis-flow.ipynb").unlink()
    Path("docs/analysis-registries.ipynb").unlink()
    Path("docs/mnist.ipynb").unlink()
    Path("docs/cellxgene-curate.ipynb").unlink()
    Path("docs/organism.ipynb").unlink()
    Path("docs/rxrx.ipynb").unlink()
    Path("docs/protein.ipynb").unlink()
    Path("docs/cell_line.ipynb").unlink()
    Path("docs/cell_type.ipynb").unlink()
    Path("docs/cell_marker.ipynb").unlink()
    Path("docs/tissue.ipynb").unlink()
    Path("docs/phenotype.ipynb").unlink()
    Path("docs/pathway.ipynb").unlink()
    Path("docs/experimental_factor.ipynb").unlink()
    Path("docs/developmental_stage.ipynb").unlink()
    Path("docs/ethnicity.ipynb").unlink()
    Path("docs/snakemake.ipynb").unlink()

    # Aux information
    Path("docs/clinicore.md").unlink(missing_ok=True)
    Path("docs/influences.md").unlink()
    Path("docs/glossary.md").unlink()

    # FAQ
    Path("docs/faq/idempotency.ipynb").unlink()
    Path("docs/faq/reference-field.ipynb").unlink()
    Path("docs/faq/track-run-inputs.ipynb").unlink()
    Path("docs/faq/acid.ipynb").unlink()
    Path("docs/faq/validate-fields.ipynb").unlink()
    Path("docs/faq/symbol-mapping.ipynb").unlink()
    Path("docs/faq/search.ipynb").unlink()
    Path("docs/faq/curate-any.ipynb").unlink()

    # API & CLI
    Path("docs/lamindb.md").unlink()
    Path("docs/bionty.md").unlink()
    Path("docs/cli.md").unlink()

    if not IS_PR:
        process = subprocess.run(  # noqa S602
            "lndocs --strip-prefix --format text --error-on-index",  # --strict back
            shell=True,
        )
        ln.connect("laminlabs/lamin-site-assets")
        ln.track()
        ln.Artifact("_build/html/summary.md", key="docs-as-txt/summary.md").save()
