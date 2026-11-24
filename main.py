"""One Line of Earned Pride.

Writes a single line of text, a quiet earned moment of pride, to
/output/entry.txt.
"""

from pathlib import Path

ENTRY = "After eleven months of falling, eight-year-old Jun stood on the ice, arms out, and glided the whole length of the rink without once looking down."


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
