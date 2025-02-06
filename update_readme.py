import random
import datetime
import pyperclip

# List of scientific quotes
quotes = [
    """Science is a way of thinking much more than it is a body of knowledge.
- Carl Sagan""",
    """The important thing is not to stop questioning. Curiosity has its own reason for existing.
- Albert Einstein""",
    """Equipped with his five senses, man explores the universe around him and calls the adventure Science.
- Edwin Powell Hubble""",
    """Somewhere, something incredible is waiting to be known.
- Carl Sagan""",
    """Science is organized knowledge. Wisdom is organized life.
- Immanuel Kant""",
    """The good thing about science is that it’s true whether or not you believe in it.
- Neil deGrasse Tyson"""
]
def copy_quote_to_clipboard(quote):
    pyperclip.copy(quote)
    print("Quote copied to clipboard!")

# Choose a random quote
quote = random.choice(quotes)

# Offer the user the option to copy the quote to clipboard
user_input = input("Would you like to copy the quote to clipboard? (yes/no): ").strip().lower()
if user_input == 'yes':
    copy_quote_to_clipboard(quote)

# Get current date
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Update the README.md file
readme_content = f"""# Ray's Repository

**Date:** {current_date}

### Daily Scientific Quote:
> {quote}

Stay curious and keep exploring!
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
