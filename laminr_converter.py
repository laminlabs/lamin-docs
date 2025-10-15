import ast
import re
from typing import Any


def convert_markdown_python_to_tabbed(content: str) -> str:
    """Convert markdown content with Python code blocks to tabbed sections.

    Args:
        content (str): Markdown content with ```python code blocks
        converter_function: Function that converts Python code to R code

    Returns:
        str: Modified markdown with tabbed Python/R sections
    """

    def replace_code_block(match):
        """Replace a single Python code block with a tabbed section."""
        python_code = match.group(1)

        # Convert Python code to R using the provided converter
        r_code = convert_lamindb_to_laminr(python_code)

        # Create the tabbed section
        tabbed_section = f"""::::{{tab-set}}
:::{{tab-item}} Py
:sync: python

```python
{python_code}
```

:::
:::{{tab-item}} R
:sync: r

```r
{r_code}
```

:::
::::"""

        return tabbed_section

    # Pattern to match ```python ... ``` code blocks
    # This pattern captures the code content between the markers
    python_code_pattern = r"```python\s*\n(.*?)\n```"

    # Replace all Python code blocks with tabbed sections
    content_with_r_code = re.sub(
        python_code_pattern, replace_code_block, content, flags=re.DOTALL
    )

    return content_with_r_code


class LaminDBToLaminRConverter:
    """Converts LaminDB Python code to LaminR (R) code.

    Handles the main syntax differences between Python and R LaminDB APIs.
    """

    def __init__(self):
        # Common Python to R function mappings
        self.function_mappings = {
            "open": "file",
            "print": "print",
            "len": "length",
            "str": "as.character",
            "int": "as.integer",
            "float": "as.numeric",
            "list": "list",
            "dict": "list",
            "range": "seq",
        }

        # File operations that need special handling
        self.file_operations = {
            r'open\("([^"]+)",\s*"w"\)\.write\("([^"]+)"\)': r'writeLines("\2", "\1")',
            r'open\("([^"]+)",\s*"r"\)\.read\(\)': r'readLines("\1")',
            r'open\("([^"]+)",\s*"rb"\)\.read\(\)': r'readBin("\1", "raw", file.info("\1")$size)',
        }

    def convert_import_statement(self, line: str) -> str:
        """Convert Python import statements to R equivalents."""
        line = line.strip()

        # Handle lamindb import
        if "import lamindb as ln" in line:
            return 'library(laminr)\nln <- import_module("lamindb")'
        elif "import lamindb" in line:
            return 'library(laminr)\nlamindb <- import_module("lamindb")'
        elif line.startswith("from lamindb import"):
            # Extract imported items
            imports = line.split("import")[1].strip()
            return f'library(laminr)\nln <- import_module("lamindb")  # Access {imports} via ln${imports.replace(", ", ", ln$")}'

        # Handle other common imports
        elif "import pandas as pd" in line:
            return '# library(reticulate)\n# pd <- import("pandas")  # or use native R data.frame'
        elif "import numpy as np" in line:
            return '# library(reticulate)\n# np <- import("numpy")  # or use native R arrays'

        return f"# {line}  # TODO: Convert this import manually"

    def convert_dot_notation(self, line: str) -> str:
        """Convert Python dot notation to R dollar notation for LaminDB objects, preserving dots in strings."""
        # First, we need to protect dots inside string literals
        # Find all string literals (both single and double quoted)
        string_pattern = r'(["\'])((?:\\.|(?!\1)[^\\])*)\1'
        strings = []

        def replace_strings(match):
            strings.append(match.group(0))
            return f"__STRING_{len(strings) - 1}__"

        # Replace strings with placeholders
        line_with_placeholders = re.sub(string_pattern, replace_strings, line)

        # Now apply dot to dollar conversion on the line without string literals
        # Handle the ln. prefix specifically
        line_with_placeholders = re.sub(r"\bln\.", "ln$", line_with_placeholders)

        # Then handle method chaining with parentheses
        # Convert .method() to $method()
        line_with_placeholders = re.sub(r"\.(\w+)\(", r"$\1(", line_with_placeholders)

        # Handle simple attribute access (no parentheses)
        line_with_placeholders = re.sub(
            r"\.(\w+)(?!\()", r"$\1", line_with_placeholders
        )

        # Restore the original strings
        result = line_with_placeholders
        for i, string_literal in enumerate(strings):
            result = result.replace(f"__STRING_{i}__", string_literal)

        return result

    def convert_file_operations(self, line: str) -> str:
        """Convert Python file operations to R equivalents."""
        for python_pattern, r_replacement in self.file_operations.items():
            line = re.sub(python_pattern, r_replacement, line)
        return line

    def convert_string_formatting(self, line: str) -> str:
        """Convert Python string formatting to R equivalents."""
        # Convert f-strings to paste0 or sprintf
        # This is a basic conversion - complex f-strings may need manual adjustment
        if 'f"' in line or "f'" in line:
            line = re.sub(
                r'f"([^"]*\{[^}]+\}[^"]*)"',
                r"# TODO: Convert f-string manually: \1",
                line,
            )

        # Convert .format() calls
        line = re.sub(r'"([^"]*)"\.format\(([^)]+)\)', r'sprintf("\1", \2)', line)

        return line

    def convert_comments(self, line: str) -> str:
        """Ensure comments use R syntax."""
        # Python and R both use # for comments, so this is mainly for consistency
        return line

    def convert_boolean_values(self, line: str) -> str:
        """Convert Python boolean values to R equivalents."""
        line = re.sub(r"\bTrue\b", "TRUE", line)
        line = re.sub(r"\bFalse\b", "FALSE", line)
        line = re.sub(r"\bNone\b", "NULL", line)
        return line

    def add_r_header(self) -> str:
        """Add necessary R library imports at the top."""
        return """library(laminr)
ln <- import_module("lamindb")

"""

    def convert_line(self, line: str) -> str:
        """Convert a single line from Python to R."""
        line = line.rstrip()

        # Skip empty lines
        if not line.strip():
            return line

        # Handle imports
        if "import" in line and line.strip().startswith(("import", "from")):
            return self.convert_import_statement(line)

        # Apply conversions in order
        line = self.convert_file_operations(line)
        line = self.convert_dot_notation(line)
        line = self.convert_string_formatting(line)
        line = self.convert_boolean_values(line)
        line = self.convert_comments(line)

        return line

    def convert_code(self, python_code: str) -> str:
        """Convert complete Python code to R code."""
        lines = python_code.split("\n")
        converted_lines = []

        has_lamindb_import = any(
            "lamindb" in line for line in lines if "import" in line
        )
        header_added = False

        for line in lines:
            converted_line = self.convert_line(line)

            # Add header after the first lamindb import
            if (
                has_lamindb_import
                and "lamindb" in converted_line
                and "import_module" in converted_line
                and not header_added
            ):
                converted_lines.append(converted_line)
                header_added = True
            else:
                converted_lines.append(converted_line)

        return "\n".join(converted_lines)


def convert_lamindb_to_laminr(python_code: str) -> str:
    """Main function to convert LaminDB Python code to LaminR code.

    Args:
        python_code (str): Python code using LaminDB

    Returns:
        str: Converted R code for LaminR
    """
    converter = LaminDBToLaminRConverter()
    return converter.convert_code(python_code)


# Example usage and test
if __name__ == "__main__":
    # Test with the provided example
    test_code = """import lamindb as ln

ln.track()  # track a run
open("sample.fasta", "w").write(">seq1\\nACGT\\n")
ln.Artifact("sample.fasta", key="sample.fasta").save()  # create an artifact
ln.finish()  # finish the run"""

    print("Original Python code:")
    print(test_code)
    print("\nConverted R code:")
    print(convert_lamindb_to_laminr(test_code))

    # Test with the problematic example
    problem_test = """artifact = ln.Artifact.get(key="sample.fasta")  # query artifact by key
artifact.view_lineage()"""

    print("\n" + "=" * 50)
    print("Problem example test:")
    print("Original Python code:")
    print(problem_test)
    print("\nConverted R code:")
    print(convert_lamindb_to_laminr(problem_test))

    # Test with more complex example
    complex_test = """import lamindb as ln
import pandas as pd

ln.track()
df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
artifact = ln.Artifact.from_df(df, key="my_data.parquet")
artifact.save()
collection = ln.Collection([artifact], name="my_collection")
collection.save()
ln.finish()"""

    print("\n" + "=" * 50)
    print("Complex example:")
    print("Original Python code:")
    print(complex_test)
    print("\nConverted R code:")
    print(convert_lamindb_to_laminr(complex_test))
