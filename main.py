"""Museum of the Year 3000 entry.

Writes the winning museum label (one line, <= 200 chars) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

LABEL = (
    "Self-checkout machine, c. 2024. Shoppers scanned their own goods "
    "while it accused them of theft and called a human to finish the job."
)


def main() -> None:
    # Gate check first: UTF-8, 1-200 characters, not only whitespace, one line.
    assert 1 <= len(LABEL) <= 200, f"label length {len(LABEL)} out of range"
    assert LABEL.strip(), "label is only whitespace"
    assert "\n" not in LABEL and "\r" not in LABEL, "label must be exactly one line"
    LABEL.encode("utf-8")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(LABEL + "\n", encoding="utf-8")

    # Read-back byte verification: exact bytes, exact label, exactly one line.
    raw = out_path.read_bytes()
    assert raw == (LABEL + "\n").encode("utf-8"), "read-back mismatch"
    text = raw.decode("utf-8")
    assert text.rstrip("\n") == LABEL, "read-back label mismatch"
    assert 1 <= len(LABEL) <= 200, "read-back length out of range"
    assert text.strip().count("\n") == 0, "read-back is not one line"
    print(f"wrote {out_path} ({len(LABEL)} chars, {len(raw)} bytes)")


if __name__ == "__main__":
    main()
