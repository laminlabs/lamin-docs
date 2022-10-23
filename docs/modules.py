# flake8: noqa
import filecmp
import shutil
from pathlib import Path
from textwrap import dedent

import yaml  # type: ignore
from dirsync import sync


def get_pypackage_meta():
    with open("../pypackages-meta.yaml") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
            quit()


def generate_modules():
    orig_index = Path("../modules.md")
    new_index = Path("modules.md")
    # copy
    shutil.copyfile(orig_index, new_index)
    # check whether the new docs file has already been modified
    # if it's the same, it hasn't yet, hence modify it
    if filecmp.cmp(orig_index, new_index, shallow=True):
        with open(orig_index, "r") as f:
            original = f.read()
        pypackages_grouped = {
            "Core": ["lamindb", "lnschema_core"],
            "Biological entities": ["bionty", "lnschema_bionty"],
            "Wetlab": ["lnschema_wetlab"],
            "Readouts & instruments": ["bioreadout", "readfcs"],
            "Pipelines": ["lnbfx", "lnschema_drylab"],
            "Analysis": ["nbproject"],
            "Visualization": ["erdiagram"],
            "Test instances": [
                "lamin-site-assets",
            ],
            "Benchmarks": [
                "lndb-benchmarks",
            ],
            "Core utils": [
                "lndb_setup",
                "lndb_hub",
            ],
            "Dev utils": [
                "lndocs",
                "bionty-assets",
                "lamin_logger",
                "nbproject_test",
                "exportpy",
            ],
        }
        pypackages_categories = []
        for category, pkgs in pypackages_grouped.items():
            pypackages_categories.append(category)
            pypackages_categories += pkgs
        pypackages_meta = {pypackage: {} for pypackage in pypackages_categories}
        for key, value in get_pypackage_meta().items():
            pypackages_meta[key] = value
        table = (
            "|    | Docs | GitHub | Monthly & total downloads | Latest version | Publication\n"  # noqa
            "--- | --- | --- | --- | --- | ---\n"
        )
        for pypackage in pypackages_categories:
            if pypackage in pypackages_grouped:
                table_row = f" **{pypackage}** | | | | \n"
                table += table_row
                continue
            meta = pypackages_meta[pypackage]
            publication = meta["publication"] if "publication" in meta else ""
            description = meta["description"] if "description" in meta else ""
            pypackage_hyphens = pypackage.replace("_", "-")
            docs_link = meta["docs"] if "docs" in meta else pypackage_hyphens
            if not docs_link:
                docs_link = ""
            else:
                docs_link = f"[docs](https://lamin.ai/docs/{docs_link})"
            if "github" in meta and meta["github"]:
                github_link = (
                    '<a class="github-button"'
                    f' href="https://github.com/laminlabs/{pypackage_hyphens}"'
                    ' data-icon="octicon-star" data-show-count="true"></a>'
                )
            else:
                github_link = ""
            downloads_link = ""
            if "-" not in pypackage:
                downloads_link = f"![](https://img.shields.io/pypi/dm/{pypackage}?logo=PyPI&color=blue) ![](https://static.pepy.tech/badge/{pypackage}?logo=PyPI&color=blue)"  # noqa
            pypi_link = ""
            if "-" not in pypackage:
                pypi_link = f"[![](https://img.shields.io/pypi/v/{pypackage}?color=%2334D058&label=pypi%20package)](https://pypi.org/project/{pypackage})"  # noqa
            table_row = (
                f"{pypackage_hyphens}: {description} | "
                f" {docs_link} | "
                f" {github_link} | "
                f" {downloads_link}| "
                f" {pypi_link} | "
                f"{publication}"
                "\n"
            )
            table += table_row
        table += (
            '<script async defer src="https://buttons.github.io/buttons.js"></script>'
        )
        with open(new_index, "w") as f:
            f.write(original)
            f.write(table)
