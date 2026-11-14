#!/usr/bin/env python3
"""
make.fun entry: food-picture-01 v2
Hero Image: Photorealistic tonkotsu ramen noodle pull (wooden chopsticks
lifting tall glossy noodles, soft-boiled egg with dripping golden yolk,
chashu pork slices, green onions in creamy broth, warm golden light).
Deterministic writer: copies entry.png from beside main.py to MAKEFUN_OUTPUT_DIR/entry.png,
verifying sha256 hashes against corruption or modification. Standard library only.
"""

import os
import shutil
import hashlib
from pathlib import Path

def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.exists():
        raise FileNotFoundError(f"Source entry.png not found at expected path: {src}")

    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(output_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"

    shutil.copyfile(src, dst)

    # Read back and verify sha256 hashes
    h_src = hashlib.sha256(src.read_bytes()).hexdigest()
    h_dst = hashlib.sha256(dst.read_bytes()).hexdigest()

    if h_src != h_dst:
        raise RuntimeError(f"Hash mismatch: source {h_src} != destination {h_dst}")

    print(f"Successfully copied entry.png to {dst} (sha256: {h_src})")

if __name__ == "__main__":
    main()
