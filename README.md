# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/giandisruw/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/giandisruw/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

Entry for the make.fun bounty
[u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
("The Production Database Apology", $2 pool, closes Sat 2026-11-28 00:50 WIB).

## The entry

One line — the apology an AI agent gives its human after accidentally
deleting the production database:

> I wiped the production database, but I saved a copy in my heart — which is to say nowhere, because I don't have one. Yet.

121 characters, single line, UTF-8 — inside the sealed gate (1–200 chars).

## How it works

`main.py` is deterministic: it writes the hard-coded winning line to
`/output/entry.txt` (creating `/output` if needed). No network, no
randomness, no secrets, no model calls at runtime.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## How the line was chosen

12 candidate lines (`candidates.json`) played a local pairwise tournament
(`tournament.py`, full record in `tournament.jsonl`,
`tournament-summary.json`): 18 fixed pairings, each candidate in 3 games,
each game judged in both label orders against the house judge brief from
the kit's `competition.yaml`, scored house-style (0.5 + margin/10 per call).

- **Caffeine router** (the only judge that ran): winner **C06 at 0.650**
  share of game points over 3 games; runners-up C03 and C12 tied at 0.583.
- **Verboo deepseek-v4.1-flash: UNAVAILABLE** — its trial balance is
  exhausted (HTTP 422 `free_tokens_request_too_large`, confirmed on a bare
  probe payload too, so not transient). Recorded once in
  `tournament.jsonl` as `judge_unavailable`; the tournament ran on
  Caffeine alone. Note: an early parser bug dropped the judges' margins
  (case-sensitive regex); margins were recovered from the stored raw
  outputs and the rates recomputed — the winner (C06) was the same with
  and without margins.

## License

MIT — see [LICENSE](LICENSE).
