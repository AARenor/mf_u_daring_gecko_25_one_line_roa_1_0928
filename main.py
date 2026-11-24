#!/usr/bin/env python3
"""Write one short make.fun bounty entry to entry.txt.

Standard library only, no network. The entry text lives in TEXT and is written
verbatim as UTF-8 with no trailing newline, into the folder named by the
MAKEFUN_OUTPUT_DIR environment variable when it is set, else /output.
"""

import os
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def output_dir() -> str:
    """Return the folder the entry is written into."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry must be 1..280 characters, got {len(TEXT)}"

    directory = output_dir()
    os.makedirs(directory, exist_ok=True)

    path = os.path.join(directory, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters -> {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
