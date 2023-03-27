# import os
import shutil
from pathlib import Path
from typing import List, Tuple

import lamindb as ln
import nox
from laminci.nox import build_docs, login_testuser1, run_pre_commit

# from nbproject_test import execute_notebooks

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
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

USE_CASES = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Integrations

redun
mnist-local
```
"""


def replace_content(filename: Path, mapped_content: List[Tuple[str, str]]) -> None:
    with open(filename) as f:
        content = f.read()
    with open(filename, "w") as f:
        for args in mapped_content:
            content = content.replace(*args)
        f.write(content)


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def build(session):
    login_testuser1(session)
    ln.setup.load("testuser1/lamin-site-assets", migrate=True)

    # LaminDB

    file = ln.select(ln.File, name="lamindb_docs").one()
    shutil.unpack_archive(file.load(), "lamindb_docs")
    Path("lamindb_docs/README.md").rename("README.md")
    Path("lamindb_docs/guide").rename("docs/guide")
    Path("lamindb_docs/faq").rename("docs/faq")
    Path("lamindb_docs/changelog.md").rename("docs/changelog.md")

    # Setup / Lamin

    file = ln.select(ln.File, name="lndb_docs").one()
    shutil.unpack_archive(file.load(), "lndb_docs")
    Path("lndb_docs/guide").rename("docs/setup")

    # Move setup within LaminDB to setup section as overview
    Path("docs/guide/01-setup.ipynb").rename("docs/setup/quickstart.ipynb")

    # Bionty

    file = ln.select(ln.File, name="bionty_docs").one()
    shutil.unpack_archive(file.load(), "bionty_docs")
    Path("bionty_docs").rename("docs/bionty")

    # Fix indexes

    # lamindb guide
    mapped_content = [("\nsetup\n", "\n"), ("/guide/setup", "/setup/quickstart")]
    replace_content("docs/guide/index.md", mapped_content=mapped_content)
    replace_content("README.md", [("/guide/setup", "/setup/quickstart")])

    # lndb guide
    mapped_content = [("# Guide", "# Setup"), (LNDB_GUIDE_FROM, LNDB_GUIDE_TO)]
    replace_content("docs/setup/index.md", mapped_content=mapped_content)

    # bionty index
    mapped_content = [
        ("../README.md", "./README.md"),
    ]
    replace_content("docs/bionty/index.md", mapped_content=mapped_content)
    mapped_content = [
        ("# Bionty: Manage ontologies & curate metadata", "# Bionty"),
    ]
    replace_content("docs/bionty/README.md", mapped_content=mapped_content)

    # Special guides

    # knowledge
    file = ln.select(ln.File, name="lnschema_bionty_docs").one()
    shutil.unpack_archive(file.load(), "lnschema_bionty_docs")
    Path("lnschema_bionty_docs/guide/knowledge.ipynb").rename(
        "docs/guide/knowledge.ipynb"
    )
    replace_content(
        "docs/guide/index.md",
        [(":caption: Biology\n\n", ":caption: Biology\n\nknowledge\n")],
    )

    # Use cases

    file = ln.select(ln.File, name="redun_lamin_fasta_docs").one()
    shutil.unpack_archive(file.load(), "redun_lamin_fasta_docs")
    Path("redun_lamin_fasta_docs/guide/1-redun.ipynb").rename("docs/guide/redun.ipynb")
    Path("redun_lamin_fasta_docs/guide/2-redun-run.ipynb").rename(
        "docs/guide/redun-run.ipynb"
    )

    file = ln.select(ln.File, name="pytorch_lamin_mnist_docs").one()
    shutil.unpack_archive(file.load(), "pytorch_lamin_mnist_docs")
    Path("pytorch_lamin_mnist_docs/guide/mnist-local.ipynb").rename(
        "docs/guide/mnist-local.ipynb"
    )

    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content += USE_CASES
        f.write(content)

    # Build docs

    # init an instance so that docs can be built
    # install lamindb and bionty from github
    session.install("git+https://github.com/laminlabs/bionty")
    session.install("git+https://github.com/laminlabs/lamindb")
    import lamindb

    lamindb.Run.transform.__doc__ = ""
    ln.setup.init(storage="mydata")
    build_docs(session)
