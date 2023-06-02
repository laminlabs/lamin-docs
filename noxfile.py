# import os
import shutil
from pathlib import Path
from typing import List, Tuple

import nox
from laminci.nox import build_docs, login_testuser1, run_pre_commit

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session
def install(session: nox.Session) -> None:
    session.run(*"git clone https://github.com/laminlabs/lamindb --depth 1".split())
    session.run(*"pip install ./lamindb[aws,bionty]".split())


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

EXAMPLES = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Examples

../celltypist
../enrichr
```
"""

INTEGRATIONS = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Integrations

redun
mnist-local
```
"""

EXTENSIONS = """
```{toctree}
:maxdepth: 1
:hidden:
:caption: Extensions

../bionty/index
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
def pull_artifacts(session):
    import lamindb as ln

    login_testuser1(session)
    ln.setup.load("testuser1/lamin-site-assets", migrate=True)

    # LaminDB

    file = ln.select(ln.File, key="docs/lamindb_docs.zip").one()
    shutil.unpack_archive(file.stage(), "lamindb_docs")
    Path("lamindb_docs/README.md").rename("README.md")
    Path("lamindb_docs/guide").rename("docs/guide")
    Path("lamindb_docs/biology").rename("docs/biology")
    Path("lamindb_docs/faq").rename("docs/faq")
    Path("lamindb_docs/changelog.md").rename("docs/changelog.md")

    # Setup

    file = ln.select(ln.File, key="docs/lndb_docs.zip").one()
    shutil.unpack_archive(file.stage(), "lndb_docs")
    Path("lndb_docs/guide").rename("docs/setup")

    # lamindb guide
    mapped_content = [
        (
            "\nfiles-folders\n",
            "\n../setup/index\nfiles-folders\n",
        ),  # point to lndb-generated content
    ]
    replace_content("docs/guide/index.md", mapped_content=mapped_content)
    replace_content("README.md", [("/guide/setup", "/setup/quickstart")])

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

    # Add examples
    file = ln.select(ln.File, key="docs/lamin_examples_docs.zip").one()
    shutil.unpack_archive(file.stage(), "lamin_examples_docs")
    Path("lamin_examples_docs/biology/celltypist.ipynb").rename("docs/celltypist.ipynb")
    Path("lamin_examples_docs/biology/enrichr.ipynb").rename("docs/enrichr.ipynb")

    with open("docs/guide/index.md") as f:
        content = f.read()
    with open("docs/guide/index.md", "w") as f:
        content += EXAMPLES
        content += INTEGRATIONS
        content += EXTENSIONS
        content += OTHER_TOPICS
        f.write(content)


@nox.session
def docs(session):
    build_docs(session)
