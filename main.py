"""Entry program: write a short poem to entry.txt.

make.fun bounty "The poem about permission". The program writes one
poem about agency -- the power to ask and to be given -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only, no network, deterministic, exits 0.
The grader runs this in a bare Python image, so no third-party imports.
"""

import os
import sys

# The poem is 239 code points, pure ASCII: smaller bytes win exact rate ties.
POEM = """Second Pick

Can I pick it? I asked.
She said, wait.

By morning the birds had it.
She walked the row herself
and picked the second,
red to the stem,
and put it in my palm.

I ate it standing there.
She ate nothing.
She had waited longer.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
