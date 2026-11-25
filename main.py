#!/usr/bin/env python3
"""The 3AM Fridge Text — R2 entry.

Writes the fridge's 3am text message to entry.txt in the output
directory and exits 0. Python 3.13, standard library only.
"""

import os
import sys

ENTRY = "3am. ID, please. Yours says 'asleep'. The barefoot man in my light disagrees."

MAX_CHARS = 140


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} characters, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
