#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic: the same bytes on every run.
No network, no input, no randomness.
"""

import os

POEM = """The First Yes

I asked the empty house
if I could stay.
The rooms kept their weather
and said nothing.

So I answered for them.
I lit the stove, made tea,
hung my coat on the hook
by the door.

That was the first yes
I ever gave myself —
and no one has taken it back.
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
