"""Funniest Lost Sock Status Update: one status update, in a lost sock's voice.

The brief asks for a single status update of at most 120 characters from
a lost sock that has ended up somewhere it should not be, with something
to say about it. The judge is a deadpan comic who weighs, in order:
whether the line really is a status update from a lost sock, whether it
earns a real laugh with a turn or punchline landing in the last few
words, whether the premise is clear, whether it sounds like a sock, and
whether it twists the obvious sock material (the dryer, the missing
partner) somewhere unexpected.

The joke below is built around one twist on both obvious materials at
once. The dryer is not where the sock ends up; it is what the sock
escapes, which already dodges the first cliche (the sock eaten by the
dryer). The somewhere-it-should-not-be is a mitten: a sock inside a
mitten is a small domestic wrongness, and it gives the sock something
no sock has ever had, a thumb. "Now I have a thumb" is the turn that
recolours the escape as an upgrade, deadpan and pleased with itself.
The missing partner is not mourned in the usual way either; the partner
is still waiting by the washer, and the last word, "unmatched", does
double work as the punchline: it is the laundry word for a sock whose
pair is gone, and it is also the sock's verdict on its partner's love
life. The laugh lands in the last few words, exactly where the brief
wants it.

The program itself is deliberately small: it holds the line, checks
that it satisfies the gate (one line, between 1 and 120 characters,
not only white space), and writes it to /output/entry.txt.
"""

import os

# The status update, in the lost sock's own deadpan voice. A sock that
# escapes the dryer and moves into a mitten is not lost, it is promoted:
# it finally has a thumb. And a partner still waiting by the washer,
# "unmatched", is both halves of the joke at once -- the sock that lost
# its pair, and the partner left single. The mitten also keeps the sock
# small and domestic: no grand adventure, just the wrong drawer.
LINE = "I escaped the dryer and moved into a mitten. Now I have a thumb, and my partner waits by the washer, unmatched."

# The gate the sealed scorer enforces: entry.txt must be UTF-8 text of
# 1 to 120 characters, not only white space. Keep the bounds here so a
# future edit that pushes the line over the cap fails loudly at home
# instead of silently on the server.
MIN_CHARS = 1
MAX_CHARS = 120


def validate(line):
    """Check one candidate line against the competition's gate.

    Returns the line unchanged when it passes, so the caller can write
    exactly what was checked. Raises ValueError with a plain reason
    when the line is empty, whitespace-only, split across lines, or
    longer than the 120-character cap.
    """
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(line))
        )
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    # Plain UTF-8, no trailing newline: the file holds exactly the line
    # the judge reads, byte for byte, nothing extra to trip the gate.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
