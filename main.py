"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt.

Deterministic, standard library only.
"""

import os

LINE = (
    "I can teleport anywhere on Earth \u2014 but only to the exact spot "
    "I'm already standing, so I arrive instantly and go nowhere."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
