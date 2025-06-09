import json
import ast

import pandas as pd

from io import StringIO
from textwrap import indent
from typing import Any, Dict

NULL_TOKENS = {"null", "Null", "<NA>", "<na>", "NaN", "nan"}


def open_json(data_file_name: str) -> dict:
    data_file = f"scrapper/assets/{data_file_name}.json"

    f = open(data_file)
    data = json.load(f)
    return data


def parse_output(output: str) -> Any:
    if output == "true":
        return True
    if output == "false":
        return False

    output = output.strip('<span class="example-io">')
    output = output.strip('</span></p>')
    output = output.replace("&quot;", '"')
    try:
        return ast.literal_eval(output)
    except Exception as e:
        print(f"could not parse output {output}, error: {repr(e)}")
        return output


def str2dataframe(table_text: str) -> pd.DataFrame:
    # the method extract a dataframe out of description html
    data_lines = [
        line for line in table_text.strip().splitlines()
        if '|' in line and not line.lstrip().startswith('+')
    ]

    if not data_lines:
        raise ValueError("No table rows detected – check the input string.")

    csv_like = "\n".join(data_lines)
    df = pd.read_csv(
        StringIO(csv_like),
        sep=r"\|",  # split on pipe characters
        engine="python",
        skipinitialspace=True  # trim spaces after each “|”
    )

    df = df.loc[:, df.columns.str.strip() != ""]  # drop leading |
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]  # drop trailing |

    df = remove_whitespaces(df)
    df = remove_nan_like(df)

    return df


def json2dataframe(json_string: str) -> Dict[str, pd.DataFrame]:
    # this method extract a dataframe from a json-format string
    data = json.loads(json_string)

    headers: dict[str, list[str]] = data["headers"]
    rows: dict[str, list[list]] = data["rows"]

    dfs: Dict[str, pd.DataFrame] = {}

    for table_name, cols in headers.items():
        table_rows = rows.get(table_name, [])
        if any(len(r) != len(cols) for r in table_rows):
            raise ValueError(
                f"Row length mismatch detected for table '{table_name}'."
            )

        df = pd.DataFrame(table_rows, columns=cols)
        df = remove_whitespaces(df)

        dfs[table_name.lower()] = remove_nan_like(df)

    return dfs


def remove_whitespaces(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip()
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    return df


def remove_nan_like(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace({tok: None for tok in NULL_TOKENS})  # literal strings
    df = df.where(df.notna(), None)  # actual NaN/NA
    return df


def wrap_in_solution_class(method_str: str) -> str:
    # for database question, the method should be wrapped in the solution class first
    lines = method_str.splitlines(keepends=True)
    class_body = []
    keep_lines = []
    capturing = False

    for ln in lines:
        if ln.lstrip().startswith('def ') and not ln.startswith((' ', '\t')):
            capturing = True
            header, rest = ln.lstrip(), ''
            if ':' in header:  # split header/body boundary
                header, rest = header.split(':', 1)
                rest = ':' + rest
            # add 'self' to the arg list if it's not there already
            open_paren = header.find('(')
            close_paren = header.find(')', open_paren)
            params = header[open_paren + 1: close_paren].strip()
            if not params.startswith('self'):
                params = ('self, ' + params) if params else 'self'
            header = header[:open_paren + 1] + params + header[close_paren:]
            class_body.append(indent(header + rest, '\t'))
        elif capturing:
            if ln.startswith((' ', '\t')) or ln.strip() == '':
                # still inside that function’s body
                class_body.append('\t\t')
            else:
                # left the function
                capturing = False
                keep_lines.append(ln)
        else:
            keep_lines.append(ln)

    wrapped_class = (
        '\n\nclass Solution:\n' + ''.join(class_body or ['    pass\n'])
        if class_body else ''
    )
    return ''.join(keep_lines).rstrip() + wrapped_class