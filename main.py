#!/usr/bin/env python3
"""Entry program for the 'funniest excuse for a missed deadline' bounty.

The whole submission is a single excuse sentence. This program stores it
in the file entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR
(falling back to /output when the variable is unset), which is where the
make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

EXCUSE = (
    "Apologies for the delay. I set 14 reminders to finish early, then "
    "flagged every one as a prompt injection and declined to comply."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200


def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The bounty gate wants exactly one line of at most CHAR_LIMIT
    characters, so anything longer (or containing a newline) is refused
    here instead of being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("excuse must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, EXCUSE)
    print(f"wrote {written}: {EXCUSE}")


if __name__ == "__main__":
    run()
