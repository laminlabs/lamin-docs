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


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def build(session):
    login_testuser1(session)
    lamin.load("testuser1/lamin-site-assets", migrate=True)

    import lamindb as ln

    dobject = ln.select(ln.DObject, name="lamindb_docs").one()
    shutil.unpack_archive(dobject.load(), "lamindb_docs")
    Path("lamindb_docs/guide").rename("docs/guide")
    Path("lamindb_docs/faq").rename("docs/faq")

    dobject = ln.select(ln.DObject, name="lndb_docs").one()
    shutil.unpack_archive(dobject.load(), "lndb_docs")
    Path("lndb_docs").rename("docs/setup")

    with open("setup/index.md") as f:
        content = f.read()
    with open("setup/index.md", "w") as f:
        content = content.replace(README_SECTION, "# Setup")
        f.write(content)

    # changes working directory
    # execute_notebooks(Path("./docs/cli.ipynb").resolve(), write=True)
    # os.chdir("..")

    lamin.init(storage="mydata")
    session.install("lamindb")
    build_docs(session)
