"""One-line excuse: an agent's reply to its human after a missed deadline.

The entry is a single line of text. This program holds the line as one
constant, checks it against the sealed gate (UTF-8, 1 to 160 characters,
not only whitespace), and writes it verbatim to the output path.

The joke is literal obedience: the human said "take your time", so the agent
took all of it. The program itself is the straight man — it does exactly
what it is told, nothing more.

Stdlib only. No network, no randomness, no clock: the same input always
produces the same bytes.
"""

import argparse
import sys
from pathlib import Path

# The entry, exactly as submitted. 55 characters. Do not edit this line.
LINE = "Your prompt said 'take your time,' so I did. All of it."

MAX_CHARS = 160


def validate(line: str) -> None:
    """Raise ValueError unless the line passes the sealed gate.

    The gate is three checks: the text is non-empty, it is not only
    whitespace, and it fits in 160 characters and encodes as UTF-8.
    Anything else is rejected before a single byte is written.
    """
    if not line:
        raise ValueError("entry is empty")
    if line.strip() == "":
        raise ValueError("entry is only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the one-line excuse to the output file."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="destination path (default: /output/entry.txt)",
    )
    args = parser.parse_args(argv)

    validate(LINE)

    dest = Path(args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, no extra bytes.
    dest.write_bytes(LINE.encode("utf-8"))

    print(f"wrote {len(LINE)} characters to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
