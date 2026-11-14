#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
make.fun entry: food-picture-01
Steaming cheeseburger with sesame seed bun, juicy beef patty, melting cheddar, lettuce, tomato.
Deterministic entry writer script.
"""

import os
import sys
import hashlib
from pathlib import Path

def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        print(f"Error: source image not found at {src}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"

    # Compute expected sha256 from source
    with open(src, "rb") as f:
        src_data = f.read()
    expected_hash = hashlib.sha256(src_data).hexdigest()

    # Write destination atomically / directly
    with open(dst, "wb") as f:
        f.write(src_data)

    # Verify destination sha256
    with open(dst, "rb") as f:
        dst_data = f.read()
    actual_hash = hashlib.sha256(dst_data).hexdigest()

    if actual_hash != expected_hash:
        print(f"Error: SHA256 hash mismatch! Expected {expected_hash}, got {actual_hash}", file=sys.stderr)
        return 1

    print(f"Successfully copied entry.png to {dst} (sha256: {actual_hash})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
