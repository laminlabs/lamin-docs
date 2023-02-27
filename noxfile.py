# import os
import shutil
from pathlib import Path

import lamin
import nox
from laminci.nox import build_docs, login_testuser1, run_pre_commit

# from nbproject_test import execute_notebooks

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


README_SECTION = """\
```{include} ../README.md
:start-line: 0
:end-line: 1
```
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
    lamin.load("testuser1/lamin-site-assets", migrate=True)

    import lamindb as ln

    # LaminDB

    dobject = ln.select(ln.DObject, name="lamindb_docs").one()
    shutil.unpack_archive(dobject.load(), "lamindb_docs")
    Path("lamindb_docs/guide").rename("docs/guide")
    Path("lamindb_docs/faq").rename("docs/faq")

    # Setup / Lamin

    dobject = ln.select(ln.DObject, name="lndb_docs").one()
    shutil.unpack_archive(dobject.load(), "lndb_docs")
    Path("lndb_docs").rename("docs/setup")

    with open("docs/setup/index.md") as f:
        content = f.read()
    with open("docs/setup/index.md", "w") as f:
        content = content.replace(README_SECTION, "# Setup")
        f.write(content)

    # Use cases

    dobject = ln.select(ln.DObject, name="redun-lamin-fasta_docs").one()
    shutil.unpack_archive(dobject.load(), "redun-lamin-fasta_docs")
    Path("redun-lamin-fasta_docs/guide/1-get-started.ipynb").rename(
        "docs/guide/redun-get-started.ipynb"
    )
    Path("redun-lamin-fasta_docs/guide/1-run-workflow.ipynb").rename(
        "docs/guide/redun-run-workflow.ipynb"
    )

    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content += USE_CASES
        f.write(content)

    # Build docs

    # init an instance so that docs can be built
    lamin.init(storage="mydata")
    session.install("lamindb")
    build_docs(session)
