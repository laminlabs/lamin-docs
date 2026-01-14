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
        elif "from datetime import" in line:
            return '# library(reticulate)\n# datetime <- import("datetime")'

        return f"# {line}  # TODO: Convert this import manually"

    def convert_dot_notation(self, line: str) -> str:
        """Convert Python dot notation to R dollar notation, preserving dots in strings and numbers."""
        # Protect string and numeric literals before converting dots
        protected = {}
        placeholder_id = 0
        
        # Protect strings
        for match in re.finditer(r'(["\'])((?:\\.|(?!\1)[^\\])*)\1', line):
            placeholder = f"__PROTECT_{placeholder_id}__"
            protected[placeholder] = match.group(0)
            line = line.replace(match.group(0), placeholder, 1)
            placeholder_id += 1
        
        # Protect numbers (e.g., 0.55, 1.23e-4)
        for match in re.finditer(r'\b\d+\.\d+(?:[eE][+-]?\d+)?\b', line):
            placeholder = f"__PROTECT_{placeholder_id}__"
            protected[placeholder] = match.group(0)
            line = line.replace(match.group(0), placeholder, 1)
            placeholder_id += 1
        
        # Convert dots to dollars
        line = re.sub(r"\bln\.", "ln$", line)
        line = re.sub(r"\.(\w+)\(", r"$\1(", line)
        line = re.sub(r"\.(\w+)(?!\()", r"$\1", line)
        
        # Restore protected literals
        for placeholder, original in protected.items():
            line = line.replace(placeholder, original)
        
        return line

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

    def convert_assignment_operator(self, line: str) -> str:
        """Convert Python assignment operator = to R's <- for variable assignments.
        
        Matches 'var = ' pattern at the start of the line (after leading whitespace).
        Skips conversion if `=` is inside a function call, list definition, or indented context.
        """
        # Get leading whitespace
        match = re.match(r'^(\s*)', line)
        indent = match.group(1) if match else ''
        
        # Skip conversion for indented lines (likely inside function args or data structures)
        # Only convert if at top level (no indentation)
        if len(indent) > 0:
            return line
        
        # Match: optional whitespace, variable name, spaces, =, space
        pattern = r'^(\s*)([a-zA-Z_]\w*)\s*=\s+'
        # Replace: optional whitespace, variable name, ' <- '
        replacement = r'\1\2 <- '
        return re.sub(pattern, replacement, line)

    def convert_function_arguments(self, line: str) -> str:
        """Add spaces around = in function arguments."""
        # Match argument=value where the = is not part of ==
        pattern = r'(\b\w+)\s*=\s*(?=[^=])'
        return re.sub(pattern, r'\1 = ', line)

    def convert_dtype_arguments(self, line: str) -> str:
        """Quote dtype argument values.

        Converts `dtype = float` to `dtype = "float"`, etc.
        This works and is easier than getting the Python type object
        """
        pattern = r'(dtype\s*=\s*)([a-zA-Z_]\w*)(?!["\'])'
        return re.sub(pattern, r'\1"\2"', line)
    
    def convert_date_function(self, line: str) -> str:
        """Convert date( calls to datetime$date( for R and add L suffix to integer arguments."""
        def add_integer_suffix(match):
            content = match.group(1)
            # Replace numeric literals with integer literals (add L suffix)
            content = re.sub(r'\b(\d+)(?![\.\dL])', r'\1L', content)
            return f'datetime$date({content})'
        
        # Match date( followed by its arguments until the closing )
        return re.sub(r'\bdate\(([^)]+)\)', add_integer_suffix, line)

    def convert_collections(self, code: str) -> str:
        """Convert Python lists and dicts to R lists"""
        
        def find_matching_close(text: str, start: int, open_char: str, close_char: str) -> int:
            """Find the index of the matching closing bracket/brace.
            
            Args:
                text: The string to search
                start: Index of the opening bracket
                open_char: Opening bracket character (e.g., '[', '{', '(')
                close_char: Closing bracket character (e.g., ']', '}', ')')
            
            Returns:
                Index of matching close bracket, or -1 if not found
            """
            depth = 1
            i = start + 1
            in_string = None
            escaped = False
            
            while i < len(text) and depth > 0:
                if in_string:
                    # Handle escape sequences and string termination
                    if escaped:
                        escaped = False
                    elif text[i] == '\\':
                        escaped = True
                    elif text[i] == in_string:
                        in_string = None
                elif text[i] in ('"', "'"):
                    # Track string literals to ignore brackets inside them
                    in_string = text[i]
                elif text[i] == open_char:
                    depth += 1
                elif text[i] == close_char:
                    depth -= 1
                i += 1
            return i - 1 if depth == 0 else -1
        
        # Convert lists: [a, b, c] → list(a, b, c)
        prev = None
        while prev != code:
            prev = code
            i = 0
            while i < len(code):
                if code[i] == '[':
                    close = find_matching_close(code, i, '[', ']')
                    if close != -1:
                        content = code[i+1:close]
                        code = code[:i] + f"list({content})" + code[close+1:]
                        i += len(f"list({content})")
                        continue
                i += 1
        
        # Convert dicts: {key: value} → list(key = value)
        def dict_to_list(content: str) -> str:
            def convert_key(match: re.Match) -> str:
                key = match.group(1)
                if (key.startswith('"') and key.endswith('"')) or (key.startswith("'") and key.endswith("'")):
                    key = key[1:-1]
                return f"{key} = "
            return re.sub(r"((?:\w+|\"[^\"]*\"|'[^']*'))\s*:\s*", convert_key, content)
        
        prev = None
        while prev != code:
            prev = code
            i = 0
            while i < len(code):
                if code[i] == '{':
                    close = find_matching_close(code, i, '{', '}')
                    if close != -1:
                        content = code[i+1:close]
                        converted = dict_to_list(content)
                        code = code[:i] + f"list({converted})" + code[close+1:]
                        i += len(f"list({converted})")
                        continue
                i += 1
        
        # Remove trailing commas in list() calls
        i = 0
        while i < len(code):
            if code[i:i+5] == 'list(':
                close = find_matching_close(code, i+4, '(', ')')
                if close != -1:
                    # Check if there's a comma before the closing paren
                    content = code[i+5:close]
                    stripped = content.rstrip()
                    if stripped.endswith(','):
                        # Remove the trailing comma
                        new_content = stripped[:-1] + content[len(stripped):]
                        code = code[:i+5] + new_content + code[close:]
                i += 1
            else:
                i += 1
        
        return code

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

        line = self.convert_file_operations(line)
        line = self.convert_boolean_values(line)
        line = self.convert_dot_notation(line)
        line = self.convert_string_formatting(line)
        line = self.convert_assignment_operator(line)
        line = self.convert_function_arguments(line)
        line = self.convert_dtype_arguments(line)
        line = self.convert_date_function(line)
        line = self.convert_comments(line)

        return line

    def convert_code(self, python_code: str) -> str:
        """Convert complete Python code to R code."""
        python_code = self.convert_collections(python_code)
        
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
