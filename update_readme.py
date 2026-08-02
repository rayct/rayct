"""
update_readme.py

Picks a quote for the day from quotes.txt and writes it into README.md
along with today's date. Meant to be run on a schedule (e.g. a daily
GitHub Actions cron job).
"""

import json
import random
import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

QUOTES_FILE = Path("quotes.txt")
STATE_FILE = Path(".quote_state.json")
README_FILE = Path("README.md")

# Quotes that should always be present in quotes.txt, even on a fresh checkout.
SEED_QUOTES = [
    "The art and science of asking questions is the source of all knowledge.\n\t- Thomas Berger",
    "Every brilliant experiment, like every great work of art, starts with an act of imagination.\n\t- Jonah Lehrer",
]


def normalize(quote):
    """Collapse whitespace/line-ending differences so two copies of the same
    quote (e.g. one with trailing spaces or \\r\\n) are recognized as identical
    rather than counted as two separate quotes."""
    return "\n".join(line.strip() for line in quote.strip().splitlines())


def load_quotes(filename=QUOTES_FILE):
    """Load quotes from a text file, separated by blank lines.

    De-duplicates by normalized content, so near-identical entries can't
    sneak in twice and skew random selection toward them.
    """
    path = Path(filename)
    if not path.exists():
        return []
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return []

    raw_blocks = [b for b in content.split("\n\n") if b.strip()]

    # Each block is normally exactly one (quote line, attribution line)
    # pair. If a block has extra lines -- e.g. someone pasted in a new
    # quote without leaving a blank line before it -- split it back into
    # individual pairs instead of silently treating it as one garbled
    # entry (this is the exact bug that was found in quotes.txt).
    raw_quotes = []
    for block in raw_blocks:
        lines = block.splitlines()
        for i in range(0, len(lines) - 1, 2):
            raw_quotes.append(f"{lines[i]}\n{lines[i + 1]}")
        if len(lines) % 2:
            raw_quotes.append(lines[-1])

    deduped = {}
    for q in raw_quotes:
        deduped.setdefault(normalize(q), q)
    return list(deduped.values())


def save_quotes(quotes, filename=QUOTES_FILE):
    """Save quotes to file, ensuring blank lines between each quote."""
    Path(filename).write_text("\n\n".join(quotes) + "\n", encoding="utf-8")


def load_state(filename=STATE_FILE):
    """Load the 'quotes not yet shown this round' queue from disk."""
    path = Path(filename)
    if not path.exists():
        return {"remaining": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"remaining": []}


def save_state(state, filename=STATE_FILE):
    Path(filename).write_text(json.dumps(state, indent=2), encoding="utf-8")


def pick_quote(quotes, state):
    """Pick a quote without repeating any quote until every quote in the
    pool has been shown once (a 'shuffle bag', same idea music apps use
    for shuffle mode). This is what stops the same handful of quotes
    from showing up over and over.
    """
    keys = [normalize(q) for q in quotes]
    lookup = dict(zip(keys, quotes))

    # Drop any leftover keys that no longer correspond to a real quote
    # (e.g. a quote was removed from quotes.txt since the last run).
    remaining = [k for k in state.get("remaining", []) if k in lookup]
    last_shown = state.get("last_shown")

    if not remaining:
        remaining = keys.copy()
        random.shuffle(remaining)
        # Without this, the last quote of one cycle and the first quote of
        # the next cycle can coincidentally be the same quote. Swap it out
        # if so, so a repeat never happens even across a reshuffle.
        if len(remaining) > 1 and remaining[-1] == last_shown:
            swap_with = random.randrange(len(remaining) - 1)
            remaining[-1], remaining[swap_with] = remaining[swap_with], remaining[-1]

    chosen_key = remaining.pop()
    state["remaining"] = remaining
    state["last_shown"] = chosen_key
    return lookup[chosen_key], state


def make_blockquote(text):
    """Prefix each line in the quote block with '> ' for Markdown blockquote."""
    return "\n".join("> " + line for line in text.splitlines())


def ordinal(n):
    """Convert an integer into its ordinal representation (1st, 2nd, etc.)."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def main():
    # Load quotes, adding any seed quotes that aren't already present.
    quotes = load_quotes()
    existing = {normalize(q) for q in quotes}
    changed = False
    for q in SEED_QUOTES:
        if normalize(q) not in existing:
            quotes.append(q)
            existing.add(normalize(q))
            changed = True

    # Only rewrite quotes.txt if something actually changed (new quotes
    # added, or duplicates removed by the load_quotes dedup step) --
    # no more reshuffling and rewriting the whole file on every run.
    original_content = QUOTES_FILE.read_text(encoding="utf-8") if QUOTES_FILE.exists() else ""
    new_content = "\n\n".join(quotes) + "\n"
    if changed or new_content != original_content:
        save_quotes(quotes)

    # Pick today's quote using the no-repeat shuffle bag.
    state = load_state()
    quote, state = pick_quote(quotes, state)
    save_state(state)
    blockquote_quote = make_blockquote(quote)

    # Get current date
    now = datetime.datetime.now(ZoneInfo("Europe/London"))
    current_date = f"{now.strftime('%B')} {ordinal(now.day)}, {now.year}"

    readme_content = f"""# Welcome

{current_date}

### Daily Quote:
{blockquote_quote}

Stay Curious and keep Exploring!
"""
    README_FILE.write_text(readme_content, encoding="utf-8")

    print("✅ README updated successfully with a random quote!")
    print(f"📚 Total quotes available: {len(quotes)}")
    print(f"🔀 Quotes left before next reshuffle: {len(state['remaining'])}")


if __name__ == "__main__":
    main()