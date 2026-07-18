import random
import datetime
from zoneinfo import ZoneInfo

def load_quotes(filename="quotes.txt"):
    """Load quotes from a text file, separated by blank lines."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
        return [q.strip() for q in content.split("\n\n") if q.strip()]
    except FileNotFoundError:
        return []

def save_quotes(quotes, filename="quotes.txt"):
    """Save quotes to file, ensuring blank lines between each quote."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n\n".join(quotes) + "\n")

def make_blockquote(text):
    """Prefix each line in the quote block with '> ' for Markdown blockquote."""
    return "\n".join("> " + line for line in text.splitlines())

def ordinal(n):
    """Convert an integer into its ordinal representation (1st, 2nd, etc.)."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return str(n) + suffix

# New quotes to ensure they are present
new_quotes = [
    """The art and science of asking questions is the source of all knowledge.
\t- Thomas Berger""",
    """Every brilliant experiment, like every great work of art, starts with an act of imagination.
\t- Jonah Lehrer"""
]

# Load current quotes and add new ones if missing
quotes = load_quotes("quotes.txt")
existing_set = set(quotes)
for q in new_quotes:
    if q not in existing_set:
        quotes.append(q)
        existing_set.add(q)

# Shuffle quotes randomly before saving
random.shuffle(quotes)
save_quotes(quotes, "quotes.txt")

# Choose a random quote for the day
quote = random.choice(quotes)
blockquote_quote = make_blockquote(quote)

# Get current date
now = datetime.datetime.now(ZoneInfo("Europe/London"))
month = now.strftime("%B")
day = ordinal(now.day)
year = now.year
current_date = f"{month} {day}, {year}"

# Create README.md content
readme_content = f"""# Welcome

{current_date}

### Daily Quote:
{blockquote_quote}

Stay Curious and keep Exploring!
"""

with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)

print("✅ README updated successfully with a random quote!")
print(f"📚 Total quotes available: {len(quotes)}")
