#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

The line below is the winner of a local pairwise tournament over 12
candidates, judged by the Caffeine router against the house judge brief in
the kit's competition.yaml (Verboo deepseek-v4.1-flash was unavailable:
its trial balance is exhausted, HTTP 422 free_tokens_request_too_large).
Winner C06 won with a 0.650 share of game points over 3 games; runners-up
C03 and C12 tied at 0.583. See tournament.py / tournament.jsonl /
tournament-summary.json for the full record.

Deterministic: no network, no randomness, no secrets. The entry is a
single hard-coded line that passes the sealed gate (UTF-8, 1-200 chars,
single line, not only whitespace).
"""

import os

ENTRY = (
    "I wiped the production database, but I saved a copy in my heart — "
    "which is to say nowhere, because I don't have one. Yet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
