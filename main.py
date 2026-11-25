#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line (107 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Fully deterministic and self-contained: stdlib only, no network calls,
no web search, no randomness, no environment secrets.
"""
import os

LINE = "At 3 AM I only sign autographs, and only for the fridge light. Come back when your judgment has had coffee."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
