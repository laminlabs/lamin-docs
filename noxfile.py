# import os
import shutil
from pathlib import Path

import lamindb as ln
import nox
from laminci.nox import build_docs, login_testuser1, run_pre_commit

# from nbproject_test import execute_notebooks

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


LAMINDB_GUIDE_FROM = "\nsetup\n"

LAMINDB_GUIDE_TO = ""

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
:caption: Use cases

redun-get-started
redun-run-workflow
```
"""


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def build(session):
    login_testuser1(session)
    ln.setup.load("testuser1/lamin-site-assets", migrate=True)

    # LaminDB

    dobject = ln.select(ln.DObject, name="lamindb_docs").one()
    shutil.unpack_archive(dobject.load(), "tmp")
    Path("tmp/docs").rename("lamindb_docs")
    Path("lamindb_docs/guide").rename("docs/guide")
    Path("lamindb_docs/faq").rename("docs/faq")
    Path("lamindb_docs/changelog.md").rename("docs/changelog.md")

    # Setup / Lamin

    dobject = ln.select(ln.DObject, name="lndb_docs").one()
    shutil.unpack_archive(dobject.load(), "tmp")
    Path("tmp/docs").rename("lndb_docs")
    Path("lndb_docs/guide").rename("docs/setup")

    # Move setup within LaminDB to setup section as overview
    Path("docs/guide/01-setup.ipynb").rename("docs/setup/overview.ipynb")

    # Fix indexes

    # lamindb guide
    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content = content.replace(LAMINDB_GUIDE_FROM, LAMINDB_GUIDE_TO)
        f.write(content)

    # lndb guide
    with open("docs/setup/index.md") as f:
        content = f.read()
    with open("docs/setup/index.md", "w") as f:
        content = content.replace("# Guide", "# Setup")
        content = content.replace(LNDB_GUIDE_FROM, LNDB_GUIDE_TO)
        f.write(content)

    # Use cases

    dobject = ln.select(ln.DObject, name="redun_lamin_fasta_docs").one()
    shutil.unpack_archive(dobject.load(), "tmp")
    Path("tmp/docs").rename("redun_lamin_fasta_docs")
    Path("redun_lamin_fasta_docs/guide/1-get-started.ipynb").rename(
        "docs/guide/redun-get-started.ipynb"
    )
    Path("redun_lamin_fasta_docs/guide/2-run-workflow.ipynb").rename(
        "docs/guide/redun-run-workflow.ipynb"
    )

    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content += USE_CASES
        f.write(content)

    # Build docs

    # init an instance so that docs can be built
    ln.setup.init(storage="mydata")
    build_docs(session)
