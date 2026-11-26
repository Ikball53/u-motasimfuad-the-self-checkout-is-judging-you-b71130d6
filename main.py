"""The Self-Checkout Is Judging You — one-liner entry.

Writes a single smug remark from a judgmental self-checkout machine
to entry.txt. Stdlib only, deterministic.
"""

import hashlib
import os
from pathlib import Path


def build_remark() -> str:
    basket = "One banana, four energy drinks."
    shrug = "Sure."
    sting = "That banana is doing the heavy lifting for your life choices."
    return " ".join([basket, shrug, sting])


def main() -> None:
    remark = build_remark()
    assert 1 <= len(remark) <= 200, f"remark is {len(remark)} chars, must be 1-200"
    assert "\n" not in remark, "remark must contain no newline"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(remark, encoding="utf-8")

    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(remark)
    print(f"chars: {len(remark)}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
