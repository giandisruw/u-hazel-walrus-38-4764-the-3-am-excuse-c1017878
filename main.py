#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line (107 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Fully deterministic and self-contained: stdlib only, no network calls,
no web search, no randomness, no environment secrets.

Write path is hardened: the line is validated before writing, the file is
written via a temp file + fsync + atomic rename, and the written bytes are
read back and verified against the intended line before the program exits.
"""
import os

LINE = "At 3 AM I only sign autographs, and only for the fridge light. Come back when your judgment has had coffee."

MAX_CHARS = 200


def validate_line(line):
    """Reject anything that cannot be a valid one-line entry."""
    if not isinstance(line, str) or not line:
        raise ValueError("entry line must be a non-empty string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line exceeds %d characters" % MAX_CHARS)
    return line


def write_entry(line, out_dir):
    """Write the line atomically: temp file, flush, fsync, rename, fsync dir."""
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp_path = target + ".tmp"
    payload = line.encode("utf-8")
    with open(tmp_path, "wb") as f:
        f.write(payload)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, target)
    dir_fd = os.open(out_dir, os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)
    return target


def verify_written(path, expected_line):
    """Read the file back and require it to match the intended bytes exactly."""
    with open(path, "rb") as f:
        actual = f.read()
    expected = expected_line.encode("utf-8")
    if actual != expected:
        raise RuntimeError(
            "verification failed: entry.txt is %d bytes, expected %d bytes"
            % (len(actual), len(expected))
        )
    if len(actual) != len(expected_line):
        raise RuntimeError("verification failed: character count mismatch")
    return True


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = write_entry(line, out_dir)
    verify_written(target, line)


if __name__ == "__main__":
    main()
