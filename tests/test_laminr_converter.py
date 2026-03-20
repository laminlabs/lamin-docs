import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from laminr_converter import convert_lamindb_to_laminr


def assert_conversion(py_code: str, expected_r_code: str) -> None:
    converted = convert_lamindb_to_laminr(py_code)
    assert converted.strip() == expected_r_code.strip()


def test_dtype_registry_reference_is_not_quoted() -> None:
    py_code = 'ln.Feature(name="experiment", dtype=ln.ULabel).save()'
    expected_r_code = 'ln$Feature(name = "experiment", dtype = ln$ULabel)$save()'
    assert_conversion(py_code, expected_r_code)


def test_dtype_builtin_types_are_quoted() -> None:
    py_code = 'ln.Feature(name="gc_content", dtype=float).save()'
    expected_r_code = 'ln$Feature(name = "gc_content", dtype = "float")$save()'
    assert_conversion(py_code, expected_r_code)


def test_try_except_is_converted_to_trycatch() -> None:
    py_code = """try:
    artifact = ln.Artifact.from_dataframe(
        df, key="my_datasets/rnaseq1.parquet", schema=schema
    )
except ln.errors.ValidationError as error:
    print(str(error))"""
    expected_r_code = """tryCatch({
artifact <- ln$Artifact$from_dataframe(
    df, key = "my_datasets/rnaseq1.parquet", schema = schema
)
}, error = function(error) {
print(str(error))
})"""
    assert_conversion(py_code, expected_r_code)


def test_try_except_is_converted_when_block_is_markdown_indented() -> None:
    py_code = """ try:
     artifact = ln.Artifact.from_dataframe(
         df, key="my_datasets/rnaseq1.parquet", schema=schema
     )
 except ln.errors.ValidationError as error:
     print(str(error))"""
    expected_r_code = """ tryCatch({
artifact <- ln$Artifact$from_dataframe(
    df, key = "my_datasets/rnaseq1.parquet", schema = schema
)
 }, error = function(error) {
print(str(error))
 })"""
    assert_conversion(py_code, expected_r_code)


def test_dataframe_string_indexing_does_not_corrupt_identifier() -> None:
    py_code = 'df["perturbation"] = df["perturbation"].cat.rename_categories({"IFNJ": "IFNG"})'
    expected_r_code = 'df[["perturbation"]] <- df[["perturbation"]]$cat$rename_categories(list(IFNJ = "IFNG"))'
    assert_conversion(py_code, expected_r_code)


@pytest.mark.parametrize(
    ("source", "py_code", "expected_r_code"),
    [
        (
            "tutorial.md",
            """import lamindb as ln

ln.track()  # track the current notebook or script""",
            """library(laminr)
ln <- import_module("lamindb")

ln$track()  # track the current notebook or script""",
        ),
        (
            "tutorial.md",
            'ln.track(plan=".plans/my-agent-plan.md")  # link plan artifact to this run',
            'ln$track(plan = ".plans/my-agent-plan.md")  # link plan artifact to this run',
        ),
        (
            "tutorial.md",
            "ln.Transform.to_dataframe()",
            "ln$Transform$to_dataframe()",
        ),
        (
            "tutorial.md",
            "ln.Run.to_dataframe()",
            "ln$Run$to_dataframe()",
        ),
        (
            "introduction.md",
            """import lamindb as ln

db = ln.DB("laminlabs/cellxgene")  # a database object for queries
df = db.Artifact.to_dataframe() # a dataframe listing datasets & models""",
            """library(laminr)
ln <- import_module("lamindb")

db <- ln$DB("laminlabs/cellxgene")  # a database object for queries
df <- db$Artifact$to_dataframe() # a dataframe listing datasets & models""",
        ),
        (
            "introduction.md",
            """from datetime import date

ln.Feature(name="gc_content", dtype=float).save()
ln.Feature(name="experiment_note", dtype=str).save()
ln.Feature(name="experiment_date", dtype=date, coerce=True).save()""",
            """datetime <- import_module("datetime")
date <- datetime$date

ln$Feature(name = "gc_content", dtype = "float")$save()
ln$Feature(name = "experiment_note", dtype = "str")$save()
ln$Feature(name = "experiment_date", dtype = date, coerce = TRUE)$save()""",
        ),
        (
            "introduction.md",
            """artifact.features.set_values({
 "gc_content": 0.55,
 "experiment_note": "Looks great",
 "experiment_date": "2025-10-24",
 })""",
            """artifact$features$set_values(list(
 gc_content = 0.55,
 experiment_note = "Looks great",
 experiment_date = "2025-10-24"
 ))""",
        ),
        (
            "introduction.md",
            'ln.Artifact.to_dataframe(include=["created_by__name", "storage__root"])',
            'ln$Artifact$to_dataframe(include = list("created_by__name", "storage__root"))',
        ),
        (
            "introduction.md",
            'ln.Artifact.filter(experiment_date="2025-10-24").to_dataframe()',
            'ln$Artifact$filter(experiment_date = "2025-10-24")$to_dataframe()',
        ),
        (
            "introduction.md",
            "ln.Artifact.filter(ulabels=my_label, projects=project).to_dataframe()",
            "ln$Artifact$filter(ulabels = my_label, projects = project)$to_dataframe()",
        ),
    ],
)
def test_examples_from_docs_are_converted(
    source: str, py_code: str, expected_r_code: str
) -> None:
    del source  # keeps fixture signature self-descriptive without linter noise
    assert_conversion(py_code, expected_r_code)
