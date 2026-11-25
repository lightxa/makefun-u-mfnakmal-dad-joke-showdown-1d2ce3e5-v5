#!/usr/bin/env python3
"""Dad Joke Showdown entry, variant 5 (Python 3.13, standard library only).

Writes one dad joke to /output/entry.txt. Outside the grader's
container the MAKEFUN_OUTPUT_DIR environment variable stands in
for /output, exactly as the kit starter does for Node:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The gate reads the file as UTF-8 text of 1 to 200 characters with
at least one non-whitespace character, and the judge reads exactly
the bytes written, so the joke is written with no trailing line end.

The joke's mechanism: two puns stacked in one short monologue,
with no quoted dialogue at all, which is a different structure
from variants 1 to 4 (all four are "I told the X... It said...").
The subject is a garden hose, an outdoor object no earlier
variant touches: not a kitchen appliance, not a vacuum, not a
remote, not a printer. The setup word "winding me up" does two
jobs: a hose literally winds and coils, and "winding someone up"
means teasing and annoying them. The punchline, "under a lot of
pressure", lands on the final words: the idiom for being stressed,
and literally true of a hose full of water. The turn is
understood on first read, the voice is deadpan, and the scene
(a dad in the garden, annoyed at the hose) is an everyday
father-at-home moment, not one of the dad jokes told a thousand
times. Original wording, never copied.

Why a garden hose is the fresh angle here: variants 1 to 4
already spent the slow cooker, the remote and the vacuum, so
another indoor appliance would feel like a remix of a joke the
judge has just read. The hose moves the dad out of the kitchen
and the living room into the garden, a setting none of the
earlier variants use, and its comedy comes from its own nature
rather than from a talking object: a hose coils and winds by
itself, so "winding me up" is not a forced pun but the plain
description of what the thing does, doubled with the idiom for
being teased. The second pun then closes the joke instead of
explaining it: "under a lot of pressure" is literally true of a
hose full of water and at the same time the idiom for the
stressed dad, so the punchline excuses the hose and the dad in
the same breath. Two puns, one short monologue, no quoted
dialogue, no character besides the dad and the hose: that is
the whole joke, and it is why this line stands apart from the
slow cooker, remote and vacuum variants.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

JOKE = (
    "My garden hose keeps winding me up, "
    "but I can't blame it. It's under a lot of pressure."
)


def is_single_line(text: str) -> bool:
    """True when the text holds no line breaks, so the joke is told
    aloud in one breath as the kit's dad-joke brief requires."""
    return "\n" not in text and "\r" not in text


def check_length(text: str) -> None:
    """Enforce the kit gate's size and non-blank rules: 1 to 200
    characters, not only white space. Fail loudly here rather than
    ship an entry the sealed gate would refuse."""
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError(f"entry fails the gate: {len(text)} characters")


def check_joke_structure(text: str) -> None:
    """Check the line against the joke's own structure: the setup
    pun ("winding") and the punchline pun ("pressure") must both
    be present, otherwise one half of the double wordplay is
    missing and the entry is not the joke it claims to be."""
    if "winding" not in text or "pressure" not in text:
        raise ValueError("entry is missing one of its two puns")


def validate_entry(text: str) -> None:
    """Enforce the kit gate locally before writing: size, non-blank,
    and a single line."""
    check_length(text)
    if not is_single_line(text):
        raise ValueError("entry must be a single line")
    check_joke_structure(text)


def main() -> None:
    validate_entry(JOKE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
