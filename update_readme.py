import random
import datetime

# List of scientific quotes
quotes = [
    """```Science is a way of thinking much more than it is a body of knowledge.
- Carl Sagan```""",
    """```The important thing is not to stop questioning. Curiosity has its own reason for existing.
- Albert Einstein```""",
    """```Equipped with his five senses, man explores the universe around him and calls the adventure Science.
- Edwin Powell Hubble```""",
    """```Somewhere, something incredible is waiting to be known.
- Carl Sagan```""",
    """```Science is organized knowledge. Wisdom is organized life.
- Immanuel Kant```""",
    """```The good thing about science is that it’s true whether or not you believe in it.
- Neil deGrasse Tyson```"""
]

# Join all the quotes into a single string with each quote separated by a newline
formatted_quotes = "\n\n".join(quotes)

# Choose a random quote
quote = random.choice(quotes)

# Get current date
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Update the README.md file
readme_content = f"""# Ray's Repository

{current_date}

### Daily Scientific Quote:
> {quote}

Stay curious and keep exploring!
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
