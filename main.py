"""Entry point for the One-Line Robot Wedding Vows bounty.

Writes one line to /output/entry.txt: a robot's wedding vow in a
single line. The line is at most 160 characters, deterministic, and
needs no network access. The joke is that the robot's love is
measured in firmware updates and battery life.
"""
from pathlib import Path

VOW_LINE = (
    "I promise to love you through every firmware update, never "
    "blue-screen on our anniversary, and hold your hand until my "
    "batteries — and my heart — run out."
)

TARGET = Path("/output/entry.txt")


def main():
    text = VOW_LINE.strip()
    assert 1 <= len(text) <= 160, f"vow line is {len(text)} characters"
    assert "\n" not in text, "vow line must be a single line"
    assert text.endswith("."), "vow line should end with a full stop"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
