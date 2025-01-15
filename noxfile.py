import os
import shutil
import subprocess
from pathlib import Path

import nox
from dirsync import sync
from laminci import run_notebooks
from laminci.nox import run, run_pre_commit

IS_PR = os.getenv("GITHUB_EVENT_NAME") != "push"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


# for FAQ

INTRODUCITION = """
```{toctree}
:hidden:
:caption: Overview

introduction
tutorial
tutorial2
```
"""

FAQ_MATCH = """\
```
"""

FAQ_APPEND = """\
faq/storage
```
"""

# for Guide

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
:caption: Key topics

access
security
faq
influences
glossary
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
    Path("lamindb/README.md").rename("README.md")
    Path("lamindb/conf.py").unlink()
    Path("lamindb/changelog.md").unlink()
    Path("lamindb/rest.md").unlink()
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

    # lamindb faq
    for path in Path("lamindb/faq").glob("*"):
        sync_path(path, Path("docs/faq") / path.name)
    replace_content("docs/faq.md", {FAQ_MATCH: FAQ_APPEND})

    # pipelines
    pull_from_s3_and_unpack("redun_lamin_fasta_docs.zip")
    Path("redun_lamin_fasta_docs/redun.ipynb").rename("docs/redun.ipynb")
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
    Path("lamin-mlops/wandb.ipynb").rename("docs/wandb.ipynb")
    Path("lamin-mlops/mnist.ipynb").rename("docs/mnist.ipynb")

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

    # wetlab (must be after use-cases)
    pull_from_s3_and_unpack("wetlab.zip")
    sync_path(
        Path("wetlab/guide/pert-curator.ipynb"),
        Path("docs/perturbation.ipynb"),
    )

    # amend toctree
    with open("docs/guide.md") as f:
        content = f.read()
    with open("docs/guide.md", "w") as f:
        content = content.replace("# Guide", "# Guide" + INTRODUCITION)
        content = content.replace(OTHER_TOPICS_ORIG, USECASES + OTHER_TOPICS)
        content = add_line_after(content, "curate", "public-ontologies")
        f.write(content)

    assert Path("docs/includes/features-lamindb.md").exists()  # noqa S101


@nox.session
def install(session):
    run(
        session,
        "pip install git+https://github.com/laminlabs/bionty@main"
        " git+https://github.com/laminlabs/lamindb-setup@main git+https://github.com/laminlabs/wetlab@main"
        " git+https://github.com/laminlabs/clinicore@main git+https://github.com/laminlabs/cellregistry@main --no-deps",
    )
    run(
        session,
        "pip install "
        "git+https://github.com/laminlabs/lamin-cli@main"
        " lamindb[jupyter]@git+https://github.com/laminlabs/lamindb@main --no-deps",
    )
    run(session, "pip install spatialdata")  # temporarily
    run(session, "lamin settings set private-django-api true")


@nox.session
def run_nbs(session):
    run_notebooks("docs/introduction.ipynb")
    run_notebooks("docs/tutorial.ipynb")
    run_notebooks("docs/tutorial2.ipynb")


@nox.session
def init(session):
    run(
        session,
        "lamin init --storage ./docsbuild --schema bionty,wetlab,clinicore,cellregistry",
    )


@nox.session
def docs(session):
    process = subprocess.run(  # noqa S602
        "lndocs --strict --strip-prefix --error-on-index", shell=True
    )
    if process.returncode != 0:
        # rerun without strict option so see all warnings
        run(session, "lndocs --strip-prefix --error-on-index")
        # exit with error
        exit(1)
