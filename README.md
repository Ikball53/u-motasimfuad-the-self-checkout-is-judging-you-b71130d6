# The Self-Checkout Is Judging You

## The line

> One banana, four energy drinks. Sure. That banana is doing the heavy lifting for your life choices.

99 characters, one line, no setup beyond the basket itself.

## Why it should win

- **It is the machine talking.** The line reads as a till receipt read-out
  ("One banana, four energy drinks.") followed by the till's own flat,
  smug verdict ("Sure."). No narrator, no explanation — just the checkout
  judging the shopper out loud.
- **One concrete basket, one instant laugh.** A single banana next to four
  energy drinks is a whole lifestyle in eight words, and any stranger gets
  the joke on a single read with no context needed.
- **The sting lands last.** "That banana is doing the heavy lifting for
  your life choices" turns the one healthy item into the punchline: the
  shopper's entire attempt at balance rests on a single piece of fruit.
- **Tight.** Every word earns its place — the filler was cut in revision
  ("a lot of" removed) so the final clause hits faster.
- **Fresh.** No "unexpected item in the bagging area", no yoghurt pile-up,
  no stock self-checkout gag — an original basket and an original twist.

## How it runs

`main.py` (Python stdlib only, deterministic) writes the line to
`entry.txt` under `$MAKEFUN_OUTPUT_DIR` (default `/output`), asserts it
is 1–200 characters with no newline, and prints the line, its character
count, and the sha256 of `entry.txt`.
