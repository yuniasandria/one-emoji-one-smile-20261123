#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji, U+1F31E SUN WITH FACE, to entry.txt in the
output directory. No trailing newline, no extra text, no caption.

Python standard library only; deterministic; no network access.
"""

import os
import sys

EMOJI = "\U0001F31E"  # SUN WITH FACE


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(EMOJI.encode("utf-8"))
    # Read-back gate check: UTF-8 text, 1-8 characters, not only whitespace.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 8, "entry must be 1-8 characters"
    assert text.strip(), "entry must not be whitespace-only"
    assert text == EMOJI, "entry must be exactly the chosen emoji"
    return 0


if __name__ == "__main__":
    sys.exit(main())
