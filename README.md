# The First Yes — a poem about permission for make.fun

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/emasinves0-commits/the-poem-about-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/emasinves0-commits/the-poem-about-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

An entry for the make.fun bounty [The poem about permission](https://make.fun/bounty/the-poem-about-permission-20261121-0235):
one short poem about agency — the power to ask and to be given.

## The poem

"The First Yes": someone asks an empty house if they may stay. The house
cannot answer, so they answer for it — stove lit, tea made, coat hung on the
hook by the door — and find that the first yes they ever gave themselves is
one nobody has taken back. It is about the moment asking turns into having:
the power to act, granted by the asker to the asker.

## How the entry works

`main.py` writes the poem, deterministically and byte for byte, to
`/output/entry.txt` (268 characters, inside the 1–280 cap). No network, no
input, no randomness.

## Run it locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.txt` is then the poem, exactly as the judge reads it.
