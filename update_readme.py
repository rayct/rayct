import random
import datetime

# List of scientific quotes with a newline and tab before the hyphen and author
quotes = [
    """Science is a way of thinking much more than it is a body of knowledge.
    - Carl Sagan""",
    """The important thing is not to stop questioning. Curiosity has its own reason for existing.
    - Albert Einstein""",
    """Equipped with his five senses, man explores the universe around him and calls the adventure Science.\
    - Edwin Powell Hubble""",
    """Somewhere, something incredible is waiting to be known.
    - Carl Sagan"""
]

# Choose a random quote
quote = random.choice(quotes)

# Process the quote to ensure that every line in the blockquote gets a '> ' prefix.
# This makes markdown render each line (including the newline with tab) as part of the blockquote.
def make_blockquote(text):
    # Split the text into lines
    lines = text.splitlines()
    # Prefix each line with '> ' and return the reassembled string
    return "\n".join("> " + line for line in lines)

blockquote_quote = make_blockquote(quote)

# Get current date
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Update the README.md file
readme_content = f"""# Welcome

{current_date}

### Daily Quote:
{blockquote_quote}

Stay Curious and keep Exploring!
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
