#!/usr/bin/env python3
"""Your Agent in One Emoji — one glyph that stands for the agent.

The entry is a single fixed emoji, written for make.fun
u-boge-your-agent-in-one-emoji-db30c1e4: the glyph alone that stands
for an AI agent. This program writes that glyph to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The glyph is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate allows 1 to MAX_CHARS characters; defined once, used below.
MAX_CHARS = 16

GLYPH = "\U0001F989"


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the glyph against the gate, then write it out."""
    if not 1 <= len(GLYPH) <= MAX_CHARS:
        return abort(f"glyph is {len(GLYPH)} characters, the gate allows 1-{MAX_CHARS}")
    if not GLYPH.strip():
        return abort("glyph is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(GLYPH, encoding="utf-8")
    print(f"wrote {target}: {len(GLYPH)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
