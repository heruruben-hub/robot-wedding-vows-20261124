#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to /output/entry.txt.
The line must be at most 160 characters, one line, and funny.
"""

import os

VOW = (
    "I vow to love you through every update, every crash, and every "
    "low-battery warning \u2014 until death, or a factory reset, do us part."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
