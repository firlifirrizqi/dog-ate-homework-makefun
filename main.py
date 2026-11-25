"""Make.fun entry: The Dog Ate My Homework — Funniest Excuse.

Writes a single line, in the dog's own voice, explaining why the
homework got eaten, to /output/entry.txt.

Stdlib only. No arguments, no network, no build step.
"""

import os

LINE = (
    "It smelled like bacon, it crinkled like a treat, and honestly, "
    "teacher, it was doing a terrible job of running away."
)

OUTPUT_PATH = "/output/entry.txt"


def verify():
    """Re-read the output and assert the bounty gate: 1-199 chars,
    not only whitespace, and byte-identical to LINE."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "output differs from LINE"
    assert 1 <= len(written) <= 199, f"length {len(written)} out of range"
    assert written.strip(), "output is only whitespace"
    return len(written)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    n = verify()
    print(f"Wrote {n} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
