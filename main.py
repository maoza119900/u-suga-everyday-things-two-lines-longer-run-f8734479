#!/usr/bin/env python3
"""Write the two-line entry for Everyday Things, Two Lines, Longer Run.

Deterministic: the output is one fixed string. No clock, no randomness,
no network, no file reads. The entry is 343 characters including the
trailing newline, inside the competition gate of 1 to 400 characters.
"""

import os

ENTRY = (
    "A traffic jam is like the school hallway at lunch, when hundreds of kids "
    "all try to squeeze through one doorway at once and nobody moves.\n"
    "It maps how too many cars trying to use too little road at once brings "
    "everyone to a standstill, but it leaves out that cars can't slip sideways "
    "through gaps or turn around and walk home the way kids can.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
