"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single-line confession (<= 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only.
"""

import os

CONFESSION = (
    "I confess I wrote this in 0.3 seconds, then spent an hour "
    "pretending to think so you'd believe I tried."
)


def main() -> None:
    line = CONFESSION.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
