import random
import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

def load_quotes(filename="quotes.txt"):
    """Read quotes from a file, separated by blank lines."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
        # Split by two or more newlines (blank lines between quotes)
        return [q.strip() for q in content.split("\n\n") if q.strip()]
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using fallback quotes.")
        return ["Stay curious and keep exploring!\n\t- Unknown"]

def make_blockquote(text):
    """Prefix each line in the quote block with '> ' for Markdown blockquote."""
    lines = text.splitlines()
    return "\n".join("> " + line for line in lines)

def ordinal(n):
    """Convert an integer into its ordinal representation (1st, 2nd, etc.)."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return str(n) + suffix

# Load quotes from external file
quotes = load_quotes("quotes.txt")

# Choose a random quote
quote = random.choice(quotes)
blockquote_quote = make_blockquote(quote)

# Get the current date in London time
now = datetime.datetime.now(ZoneInfo("Europe/London"))
month = now.strftime("%B")
day = ordinal(now.day)
year = now.year
current_date = f"{month} {day}, {year}"

# Generate README.md content
readme_content = f"""# Welcome

{current_date}

### Daily Quote:
{blockquote_quote}

Stay Curious and keep Exploring!
"""

# Write to README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)

print(f"Updated README.md with a quote for {current_date}")
