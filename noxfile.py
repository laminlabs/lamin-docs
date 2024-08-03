import os
import shutil
import subprocess
from pathlib import Path
from subprocess import run
from typing import Dict

import nox
from laminci.nox import login_testuser1, run_pre_commit

nox.options.default_venv_backend = "none"

IS_PR = os.getenv("GITHUB_EVENT_NAME") != "push"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session
def install(session: nox.Session) -> None:
    session.run(*"git clone https://github.com/laminlabs/lamindb --depth 1".split())
    session.run(*"pip install ./lamindb[aws,bionty]".split())


# for FAQ

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

features
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


def replace_content(filename: Path, mapped_content: Dict[str, str]) -> None:
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
    run(
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
    pull_from_s3_and_unpack("lamindb_docs.zip")
    Path("lamindb_docs/README.md").rename("README.md")
    Path("lamindb_docs/includes/features-lamindb.md").unlink()
    Path("lamindb_docs/includes/features-laminhub.md").unlink()
    Path("lamindb_docs/changelog.md").unlink()
    for path in Path("lamindb_docs").glob("*"):
        if (
            path.name == "index.md"
            or path.name in {"storage", "storage.md"}  # not user facing
            or path.name == "faq"  # directory treated below
        ):
            continue
        print("copying", path)
        sync_path(path, Path("docs") / path.name)

    # # lamindb faq
    # for path in Path("lamindb_docs/faq").glob("*"):
    #     sync_path(path, Path("docs/faq") / path.name)
    # replace_content("docs/faq.md", {FAQ_MATCH: FAQ_APPEND})

    # # pipelines
    # pull_from_s3_and_unpack("redun_lamin_fasta_docs.zip")
    # Path("redun_lamin_fasta_docs/redun.ipynb").rename("docs/redun.ipynb")
    # pull_from_s3_and_unpack("nextflow_lamin_docs.zip")
    # Path("nextflow_lamin_docs/mcmicro.ipynb").rename("docs/nextflow.ipynb")
    # pull_from_s3_and_unpack("snakemake_lamin_usecases_docs.zip")
    # Path("snakemake_lamin_usecases_docs/bulk_rna_seq.ipynb").rename(
    #     "docs/snakemake.ipynb"
    # )

    # # mlops
    # pull_from_s3_and_unpack("lamin_mlops_docs.zip")
    # Path("lamin_mlops_docs/wandb.ipynb").rename("docs/wandb.ipynb")

    # # cellxgene-lamin
    # pull_from_s3_and_unpack("cellxgene_lamin_docs.zip")
    # for path in Path("cellxgene_lamin_docs/").glob("*"):
    #     if path.name.endswith(
    #         ("cellxgene.ipynb", "census.ipynb", "cellxgene-curate.ipynb")
    #     ):
    #         sync_path(path, Path("docs") / path.name)

    # # lamin-spatial
    # pull_from_s3_and_unpack("rxrx_lamin_docs.zip")
    # for path in Path("rxrx_lamin_docs/").glob("*"):
    #     if path.name == "rxrx.ipynb":
    #         sync_path(path, Path("docs") / path.name)
    #     elif path.name == "vitessce.ipynb":
    #         sync_path(path, Path("docs") / path.name)

    # # use-cases
    # pull_from_s3_and_unpack("lamin_usecases_docs.zip")
    # for path in Path("lamin_usecases_docs/").glob("*"):
    #     if (
    #         path.name == "index.md"
    #         or path.name == "usecases.md"
    #         or path.name == "changelog.md"
    #     ):
    #         continue
    #     print("copying", path)
    #     sync_path(path, Path("docs") / path.name)

    # # amend toctree
    # with open("docs/guide.md") as f:
    #     content = f.read()
    # with open("docs/guide.md", "w") as f:
    #     content = content.replace(OTHER_TOPICS_ORIG, USECASES + OTHER_TOPICS)
    #     content = add_line_after(content, "curate", "public-ontologies")
    #     f.write(content)

    assert Path("docs/includes/features-lamindb.md").exists()


@nox.session
def docs(session):
    # session.run(
    #     *"pip install --no-deps git+https://github.com/laminlabs/lnschema-core".split()  # noqa
    # )
    session.run(*"pip install git+https://github.com/laminlabs/bionty".split())
    session.run(
        *"pip install --no-deps git+https://github.com/laminlabs/wetlab".split()  # noqa
    )
    session.run(*"pip install git+https://github.com/laminlabs/lamindb@release".split())
    login_testuser1(session)
    session.run(*"lamin init --storage ./docsbuild --schema bionty,wetlab".split())
    prefix = "." if Path("./lndocs").exists() else ".."
    if nox.options.default_venv_backend == "none":
        session.run(*f"pip install {prefix}/lndocs".split())
    else:
        session.install(f"{prefix}/lndocs")
    process = subprocess.run(
        "lndocs --strip-prefix --error-on-index --strict", shell=True
    )
    if process.returncode != 0:
        # rerun without strict option so see all warnings
        session.run(*"lndocs --strip-prefix --error-on-index".split())
        # exit with error
        exit(1)
