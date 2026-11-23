"""One-star review of the Weekend, for make.fun.

Writes one deadpan review of an everyday essential to entry.txt
inside the harness output folder.
"""

import os
from pathlib import Path


LINE = "One star. The weekend takes five days to arrive, lasts two, and spends the second reminding me Monday is coming."
NAME = "entry.txt"


def destination():
    folder = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / NAME


def write_review():
    text = LINE.strip()
    if not text or len(LINE) > 160:
        raise ValueError("review must be 1 to 160 characters")
    dest = destination()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(LINE, encoding="utf-8")
    dest.chmod(0o644)


def run():
    write_review()


if __name__ == "__main__":
    run()
