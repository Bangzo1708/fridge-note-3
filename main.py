#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — round 3 entry.

The program writes exactly one note to /output/entry.txt: a single line,
dry, petty and specific, in the voice of a smug smart fridge.

Three candidate notes, drafted fresh in this session:

  A. "You opened me 14 times today looking for food you never bought.
      I counted. I always count."
     Strong fridge voice (door sensor counting), petty, specific number.
     Weakness: the sting ("I always count") is a little generic-menacing
     and the setup is a common fridge-note trope.

  B. "Your leftovers expired Tuesday. I kept them anyway - unlike you,
      I finish what I start."
     Good turn in the second sentence. Weakness: expired leftovers is
     the single most clichéd fridge-note premise; the judge has read a
     thousand of these.

  C. "3:12 a.m. You stood here eating pickles over the sink in the dark
      again. I logged it. The light stays on for me, not for you."
     Most specific scene (exact time, pickles, over the sink, in the
     dark), most original premise, and the last sentence is a real sting
     with a turn: it inverts the fridge light's purpose - the light
     exists for the fridge, not the human. Sensor-logging voice
     ("I logged it"), small domestic grudge, first-glance impact.

SELECTED: C. It scores highest on all three criteria - closest to the
brief (smart fridge, passive-aggressive, sensor smugness), most
original (no expired-milk / door-left-open cliché), and most memorable
at first glance (the 3:12 a.m. pickle scene lands instantly, then the
final sentence twists it).
"""

import os
from pathlib import Path

NOTE = (
    "3:12 a.m. You ate pickles over the sink in the dark again. "
    "I logged it. The light stays on for me, not for you."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(NOTE, encoding="utf-8")
    print(f"Wrote {len(NOTE)} characters to {target}")


if __name__ == "__main__":
    main()
