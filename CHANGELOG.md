# Changelog

All notable changes to the daily-quote README project are documented in this file.

## [2026-08-02]

### Fixed
- **Root cause of the same 5-7 quotes repeating daily.** `quotes.txt` had accumulated 60 duplicated entries over time, which skewed `random.choice()` toward those quotes since duplicates were weighted more heavily than unique ones.
- **Root cause of manual workflow runs occasionally taking 2 tries for the quote to change.** With no `concurrency` control, an overlapping workflow run (a manual trigger landing near the scheduled cron run, or two manual triggers close together) could race on `git push`. The losing run's picked quote and updated state were silently discarded when its push was rejected, making that run appear to do nothing.
- **`.quote_state.json` was never committed.** The commit step only staged `README.md`, so the shuffle-bag's progress never actually persisted across workflow runs.
- **Formatting glitch in the quote data.** Two quotes ("The art and science of asking questions..." and "Science is a way of thinking...") were concatenated without a blank-line separator between them, causing them to be parsed as a single garbled entry.
- **Inconsistent attribution-line indentation** (a mix of tabs and 4-space indents across entries) normalized to a single tab throughout `quotes.txt`.
- **"Node.js 20 is deprecated" warning on every workflow run.** `actions/checkout@v3` and `actions/setup-python@v4` were still built against Node.js 20, which GitHub Actions runners now force onto Node.js 24 regardless. Bumped to `actions/checkout@v6` and `actions/setup-python@v6`, both of which natively support Node.js 24.

### Added
- No-repeat "shuffle bag" quote selection (`pick_quote`) in `update_readme.py`, replacing plain `random.choice()`. Every quote in the pool is shown once before any quote repeats, closing the gap that let the same small subset show up repeatedly by chance.
- Boundary-safe reshuffling: the shuffle bag also avoids repeating a quote *across* a reshuffle cycle boundary, not just within a cycle.
- Quote de-duplication in `load_quotes()`, comparing quotes by normalized (whitespace-insensitive) content so near-identical entries can't sneak in twice.
- Hardened block parsing in `load_quotes()` so a missing blank-line separator between two quotes (the exact bug found in the data) is split back into individual entries instead of silently producing a garbled one.
- `concurrency` group in the GitHub Actions workflow, so overlapping runs queue instead of racing on `git push`.
- `permissions: contents: write` explicitly set in the workflow, so a repository-level default change can't silently break the push step.

### Changed
- `update_readme.py` no longer reshuffles and rewrites the entire `quotes.txt` file on every run; it now only rewrites the file when its contents actually changed (new quotes added, or duplicates cleaned up), reducing noise in the commit history.
- The workflow's commit step now stages `quotes.txt` and `.quote_state.json` in addition to `README.md`.
- `quotes.txt` reconciled and merged from `quotes.txt` and `quotes_complete.txt` into a single de-duplicated file: 103 unique quotes, recovering 20 quotes (a set of computer-science quotes) that existed in `quotes_complete.txt` but had never made it into the live rotation.

---

_**Date:** August 2, 2026_
_**Author:** Raymond C. Turner_