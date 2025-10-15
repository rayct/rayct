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
\t- Jonah Lehrer""",
    """The first principle is that you must not fool yourself—and you are the easiest person to fool.
\t- Richard Feynman""",
    """In the long run, curiosity-driven research just works better. Real breakthroughs come from people focusing on what they’re excited about.
\t- Geoffrey Hinton""",
    """We live in a society exquisitely dependent on science and technology, in which hardly anyone knows anything about science and technology.
\t- Carl Sagan""",
    """Progress is made by trial and failure; the failures are generally a hundred times more numerous than the successes; yet they are usually left unchronicled.
\t- William Ramsay""",
    """It is strange that only extraordinary men make the discoveries, which later appear so easy and simple.
\t- Georg C. Lichtenberg""",
    """It is not the strongest of the species that survives, nor the most intelligent, but the one most responsive to change.
\t- Charles Darwin""",
    """The greatest scientists are artists as well.
\t- Albert Einstein""",
    """Science is nothing but perception.
\t- Plato""",
    """The scientist is motivated primarily by curiosity and a desire for truth.
\t- Irving Langmuir""",
    """The good thing about science is that it’s self-correcting.
\t- Neil deGrasse Tyson""",
    """All science is either physics or stamp collecting.
\t- Ernest Rutherford""",
    """The purpose of computing is insight, not numbers.
\t- Richard Hamming""",
    """Somewhere, something incredible is waiting to be discovered.
\t- Carl Sagan""",
    """A scientist lives with all reality. There is nothing better. To know reality is to accept it, and even to love it.
\t- George Wald""",
    """Science without religion is lame, religion without science is blind.
\t- Albert Einstein""",
    """In science, we must be interested in things, not in persons.
\t- Marie Curie""",
    """The future belongs to those who believe in the beauty of their dreams.
\t- Eleanor Roosevelt""",
    """Science is the acceptance of what works and the rejection of what does not. That needs more courage than we might think.
\t- Jacob Bronowski"""
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
