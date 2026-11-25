#!/usr/bin/env python3
"""make.fun entry -- u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Writes one single-sentence childhood memory to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only. Deterministic: identical bytes on every run.
"""

import os

ENTRY = "Every August, Grandma packed twelve rice balls in a tin for my train home, and I ate eleven on the way, saving the last one until the fields were gone, because then the summer was over."

def main():
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "ENTRY harus tepat satu kalimat"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
