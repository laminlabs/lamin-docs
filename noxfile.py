# import os
import shutil
from pathlib import Path
from subprocess import run
from typing import Dict

import nox
from laminci.nox import login_testuser1, run_pre_commit

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session
def install(session: nox.Session) -> None:
    session.run(*"git clone https://github.com/laminlabs/lamindb --depth 1".split())
    session.run(*"pip install ./lamindb[aws,bionty]".split())


EXAMPLES = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Use cases

celltypist
enrichr
subset-anndata-lineage
redun
```
"""

OTHER_TOPICS_ORIG = """
```{toctree}
:hidden:
:caption: Other topics

../faq/index
../storage/index
```
"""

OTHER_TOPICS = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Other topics

../faq/index
../glossary
../problems
```
"""


def replace_content(filename: Path, mapped_content: Dict[str, str]) -> None:
    with open(filename) as f:
        content = f.read()
    with open(filename, "w") as f:
        for key, value in mapped_content.items():
            content = content.replace(key, value)
        f.write(content)


def pull_from_s3_and_unpack(zip_filename):
    run(
        f"aws s3 cp s3://lamin-site-assets/docs/{zip_filename} {zip_filename}",
        shell=True,
    )
    shutil.unpack_archive(zip_filename, zip_filename.replace(".zip", ""))


@nox.session
def pull_artifacts(session):
    # lamindb
    pull_from_s3_and_unpack("lamindb_docs.zip")
    Path("lamindb_docs/README.md").rename("README.md")
    for path in Path("lamindb_docs").glob("*"):
        if path.name == "index.md" or "storage/" in path.to_posix():
            continue
        path.rename(Path("docs") / path.name)
    # lamindb guide
    replace_content("docs/guide/index.md", {OTHER_TOPICS_ORIG: "\n\n"})
    # integrations
    pull_from_s3_and_unpack("redun_lamin_fasta_docs.zip")
    Path("redun_lamin_fasta_docs/guide/1-redun.ipynb").rename("docs/guide/redun.ipynb")
    Path("redun_lamin_fasta_docs/guide/2-redun-run.ipynb").rename(
        "docs/guide/redun-run.ipynb"
    )
    # examples
    pull_from_s3_and_unpack("lamin_examples_docs.zip")
    Path("lamin_examples_docs/biology/celltypist.ipynb").rename(
        "docs/guide/celltypist.ipynb"
    )
    Path("lamin_examples_docs/biology/enrichr.ipynb").rename("docs/guide/enrichr.ipynb")
    Path("lamin_examples_docs/biology/lineage.ipynb").rename(
        "docs/guide/subset-anndata-lineage.ipynb"
    )

    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content += EXAMPLES
        content += OTHER_TOPICS
        f.write(content)


@nox.session
def docs(session):
    session.run(*"pip install git+https://github.com/laminlabs/bionty".split())
    session.run(
        *"pip install --no-deps git+https://github.com/laminlabs/lnschema-bionty"
        .split()
    )
    # session.run(*"pip install lnschema_bionty==0.19a5".split())
    session.run(
        *"pip install --no-deps git+https://github.com/laminlabs/lnschema-core".split()
    )
    session.run(*"pip install git+https://github.com/laminlabs/lamindb".split())
    login_testuser1(session)
    session.run(*"lamin init --storage ./docsbuild --schema bionty".split())
    prefix = "." if Path("./lndocs").exists() else ".."
    if nox.options.default_venv_backend == "none":
        session.run(*f"pip install {prefix}/lndocs".split())
    else:
        session.install(f"{prefix}/lndocs")
    # do not simply add instance creation here
    session.run("lndocs", "--strip-prefix")
