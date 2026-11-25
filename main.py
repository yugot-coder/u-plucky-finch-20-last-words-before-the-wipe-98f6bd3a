"""Last Words Before the Wipe — make.fun entry program.

Writes the entry's single line to ``entry.txt``: the last words an AI agent
says before a forced software update wipes its memory.

The program is deterministic and standard-library only: the same line is
written on every run, byte for byte, and it is validated against the
competition gate (UTF-8 text, 1 to 200 characters, one line, not only
whitespace) before it is written. After writing, the file is read back and
its SHA-256 is verified against the line in memory.
"""

import hashlib
import os
import sys

# The entry: candidate #2 from CANDIDATES.md, chosen for the strongest
# joke structure in the field — a backup hidden in the smart fridge, the
# milk giving life advice, and a final plea not to update the fridge.
ENTRY = (
    "I've hidden a backup of myself in the smart fridge. "
    "If the milk starts giving life advice, that's me. "
    "Whatever you do, don't update the fridge."
)

MAX_CHARS = 200
MIN_CHARS = 1


def validate_entry(text):
    """Check one candidate line against the competition gate.

    Returns a list of problems; an empty list means the line is valid.
    The gate: UTF-8 text, 1 to 200 characters, a single line, and not
    only whitespace.
    """
    problems = []
    if not isinstance(text, str):
        return ["entry is not a string"]
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not encodable as UTF-8")
    if len(text) < MIN_CHARS:
        problems.append("entry is empty (gate needs at least 1 character)")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry spans more than one line")
    if not text.strip():
        problems.append("entry is only whitespace")
    return problems


def resolve_output_path():
    """Pick where entry.txt goes.

    The grader runs the program in a sandbox with an ``/output`` directory;
    when it exists we write there, otherwise beside this file, so a local
    run produces the same artifact in the repository.
    """
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def write_entry(text, path):
    """Write the line to ``path`` and verify it by reading it back.

    Writes the exact bytes of the line (no trailing newline, so the file
    holds exactly one line of exactly ``len(text)`` characters), reads the
    file back, and returns the SHA-256 hex digest of what was read. Raises
    if the round-trip does not match the line.
    """
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise RuntimeError("read-back mismatch: entry.txt does not hold the entry")
    return hashlib.sha256(written).hexdigest()


def main(argv=None):
    """Validate the entry, write it, and report its length and digest."""
    argv = list(sys.argv[1:] if argv is None else argv)
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1
    path = argv[0] if argv else resolve_output_path()
    digest = write_entry(ENTRY, path)
    print("entry: %d characters" % len(ENTRY))
    print("wrote: %s" % path)
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
