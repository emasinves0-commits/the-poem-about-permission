#!/usr/bin/env python3
"""The poem about permission — make.fun entry (v2, "The Photograph").

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic: the same bytes on every run.
No network, no input, no randomness.

v2 replaces v1 ("The First Yes", dev 9W/2D/0L, rate 83.91%): the new
poem follows the pattern of the top-ranked entries — a concrete domestic
ask, a family elder, a physical detail — with an unclaimed angle: the
giver keeps the power to decide the terms of the gift.
"""

import os

POEM = """The Photograph

May I take your picture?
Wait, Grandma said,
and put her earrings on —
blue ones — then sat
by the window, hands folded.

I waited for the yes.
She gave me light
on her face instead,
way she wanted
to be remembered.

The camera was mine.
The picture was hers.
"""


MAX_CHARS = 280


def main() -> None:
    # Guard the gate: the entry must be 1-280 characters, not only white space.
    if not POEM.strip():
        raise ValueError("poem must not be only white space")
    if len(POEM) > MAX_CHARS:
        raise ValueError(f"poem is {len(POEM)} characters, over the {MAX_CHARS} cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
