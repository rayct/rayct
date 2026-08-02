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

    raw_quotes = [q.strip() for q in content.split("\n\n") if q.strip()]

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

    if not remaining:
        remaining = keys.copy()
        random.shuffle(remaining)

    chosen_key = remaining.pop()
    state["remaining"] = remaining
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
