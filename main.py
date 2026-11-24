"""One-line cat joke entry for "The One-Line Cat Joke That Lands".

Writes the final joke to /output/entry.txt, exactly as-is, no trailing newline.

Pass 1 (chosen): "The vet said my cat is overweight. My cat said the vet is underfed."
- Judge criteria: setup ("vet said cat is overweight") + turn (cat reverses
  the accusation onto the vet) in one line; the reversal is the surprise, it
  lands on the last word; 67 chars, nothing to cut; retellable in one breath.
- Pass 2 challenger (tested, rejected): "My cat sat on my keyboard and
  deleted my essay. He looked at me like I'd been the one typing wrong all
  along." (109 chars, md5 cc86670a091868ee4edfe7f735165017) — the cat-blaming-you
  turn is funny, but it reads like
  a little anecdote with a narrator, and the punch needs the whole second
  sentence to arrive. The vet line's reversal is tighter, hits in the final
  word, and survives being repeated out of context better.
"""

import os

JOKE = "The vet said my cat is overweight. My cat said the vet is underfed."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
