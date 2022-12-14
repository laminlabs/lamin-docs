from pathlib import Path

import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session: nox.Session) -> None:
    session.install("pre-commit")
    session.run("pre-commit", "install")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def build(session):
    prefix = "." if Path("./lndocs").exists() else ".."
    session.install(f"{prefix}/lndocs")
    session.run("lndocs")
