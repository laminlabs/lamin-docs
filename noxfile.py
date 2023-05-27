# import os
import shutil
from pathlib import Path
from typing import List, Tuple

import lamindb as ln
import nox
from laminci.nox import build_docs, login_testuser1, run_pre_commit

# from nbproject_test import execute_notebooks

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


LNDB_GUIDE_FROM = """\
```{toctree}
:maxdepth: 1

setup-user
"""

LNDB_GUIDE_TO = """\
```{toctree}
:maxdepth: 1

quickstart
setup-user
"""

INTEGRATIONS = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Integrations

../bionty/index
redun
mnist-local
```
"""

OTHER_TOPICS_ORIG = """
```{toctree}
:hidden:
:caption: Other topics

../faq/index
```
"""

OTHER_TOPICS = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Other topics

../faq/index
../architecture
../glossary
../problems
```
"""


def replace_content(filename: Path, mapped_content: List[Tuple[str, str]]) -> None:
    with open(filename) as f:
        content = f.read()
    with open(filename, "w") as f:
        for args in mapped_content:
            content = content.replace(*args)
        f.write(content)


@nox.session
def build(session):
    login_testuser1(session)
    ln.setup.load("testuser1/lamin-site-assets", migrate=True)

    # LaminDB

    file = ln.select(ln.File, key="docs/lamindb_docs.zip").one()
    shutil.unpack_archive(file.stage(), "lamindb_docs")
    Path("lamindb_docs/README.md").rename("README.md")
    Path("lamindb_docs/guide").rename("docs/guide")
    Path("lamindb_docs/faq").rename("docs/faq")
    Path("lamindb_docs/changelog.md").rename("docs/changelog.md")

    # Setup

    file = ln.select(ln.File, key="docs/lndb_docs.zip").one()
    shutil.unpack_archive(file.stage(), "lndb_docs")
    Path("lndb_docs/guide").rename("docs/setup")

    mapped_content = [("# Guide", "# Setup"), (LNDB_GUIDE_FROM, LNDB_GUIDE_TO)]
    replace_content("docs/setup/00-index.ipynb", mapped_content=mapped_content)

    # Bionty

    file = ln.select(ln.File, key="docs/bionty_docs.zip").one()
    shutil.unpack_archive(file.stage(), "bionty_docs")
    Path("bionty_docs").rename("docs/bionty")

    replace_content(
        "docs/bionty/index.md",
        mapped_content=[
            ("../README.md", "./README.md"),
        ],
    )

    # Clean up LaminDB guide index
    mapped_content = [(OTHER_TOPICS_ORIG, "")]
    replace_content("docs/guide/index.md", mapped_content=mapped_content)

    # Add integrations

    file = ln.select(ln.File, key="docs/redun_lamin_fasta_docs.zip").one()
    shutil.unpack_archive(file.stage(), "redun_lamin_fasta_docs")
    Path("redun_lamin_fasta_docs/guide/1-redun.ipynb").rename("docs/guide/redun.ipynb")
    Path("redun_lamin_fasta_docs/guide/2-redun-run.ipynb").rename(
        "docs/guide/redun-run.ipynb"
    )

    file = ln.select(ln.File, key="docs/pytorch_lamin_mnist_docs.zip").one()
    shutil.unpack_archive(file.stage(), "pytorch_lamin_mnist_docs")
    Path("pytorch_lamin_mnist_docs/guide/mnist-local.ipynb").rename(
        "docs/guide/mnist-local.ipynb"
    )

    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content += INTEGRATIONS
        content += OTHER_TOPICS
        f.write(content)

    # Build docs

    # init an instance so that docs can be built
    # install lamindb and bionty from github
    session.install("git+https://github.com/laminlabs/bionty")
    session.install("git+https://github.com/laminlabs/lamindb")
    ln.setup.init(storage="mydata")
    build_docs(session)
