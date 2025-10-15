import random
import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

# List of scientific quotes with a newline and tab before the hyphen and author
quotes = [
    """Science is a way of thinking much more than it is a body of knowledge.
\t- Carl Sagan""",
    """The important thing is not to stop questioning. Curiosity has its own reason for existing.
\t- Albert Einstein""",
    """Equipped with his five senses, man explores the universe around him and calls the adventure Science.
\t- Edwin Powell Hubble""",
    """Somewhere, something incredible is waiting to be known.
\t- Carl Sagan""",
    """Science is organized knowledge. Wisdom is organized life.
\t- Immanuel Kant""",
    """The good thing about science is that it’s true whether or not you believe in it.
\t- Neil deGrasse Tyson""",
    """If you can't explain it simply, you don't understand it well enough.
\t- Albert Einstein""",
    """The most incomprehensible thing about the world is that it is comprehensible.
\t- Albert Einstein""",
    """The universe is under no obligation to make sense to you.
\t- Neil deGrasse Tyson""",
    """There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
\t- Albert Einstein""",
    """To confine our attention to terrestrial matters would be to limit the human spirit.
\t- Stephen Hawking""",
    """We are star stuff, we are the cosmos made conscious and life is the means by which the universe understands itself.
\t- Carl Sagan""",
    """The universe is not only stranger than we imagine, it is stranger than we can imagine.
\t- J.B.S. Haldane""",
    """Physics is not about how the world is, it is about what we can say about the world.
\t- Niels Bohr""",
    """The beauty of a flower is a scientific fact.
\t- Richard P. Feynman""",
    """Time is an illusion. Lunchtime doubly so.
\t- Douglas Adams, *The Hitchhiker's Guide to the Galaxy*""",
    """I think we have a great responsibility to understand our role in the universe.
\t- Neil deGrasse Tyson""",
    """The whole of science is nothing more than a refinement of everyday thinking.
\t- Albert Einstein""",
    """I do not believe that the universe is in any way different from what it seems to be, but I do believe that we do not know nearly enough to have the right to be sure.
\t- J. B. S. Haldane""",
    """The laws of physics are the same everywhere in the universe.
\t- Stephen Hawking""",
    """We are like butterflies who flutter for a day and think it is forever.
\t- Carl Sagan""",
    """Everything is theoretically impossible, until it is done.
\t- Robert A. Heinlein""",
    """Astronomy compels the soul to look upwards and leads us from this world to another.
\t- Plato""",
    """The great discovery of our age is that we can know the structure of the universe, the structure of the atom, and the structure of life.
\t- Richard P. Feynman""",
    """In science, there are no shortcuts to truth.
\t- Karl Popper""",
    """Science is a way of trying not to fool yourself. The first principle is that you must not fool yourself.
\t- Richard Feynman""",
    """I would rather have questions that can't be answered than answers that can't be questioned.
\t- Richard Feynman""",
    """If I have seen further it is by standing on the shoulders of giants.
\t- Isaac Newton""",
    """The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom.
\t- Isaac Asimov""",
    """Mathematics is the language with which God has written the universe.
\t- Galileo Galilei""",
    """Research is what I'm doing when I don't know what I'm doing.
\t- Wernher von Braun""",
    """It is the tension between creativity and skepticism that has produced the stunning and unexpected findings of science.
\t- Carl Sagan""",
    """The important thing in science is not so much to obtain new facts as to discover new ways of thinking about them.
\t- William Lawrence Bragg""",
    """Science is the great antidote to the poison of enthusiasm and superstition.
\t- Adam Smith""",
    """The universe is full of magical things patiently waiting for our wits to grow sharper.
\t- Eden Phillpotts""",
    """Science, my lad, is made up of mistakes, but they are mistakes which it is useful to make, because they lead little by little to the truth.
\t- Jules Verne""",
    """Exploration is in our nature. We began as wanderers, and we are wanderers still.
\t- Carl Sagan""",
    """For me, it is far better to grasp the Universe as it really is than to persist in delusion, however satisfying and reassuring.
\t- Carl Sagan""",
    """I don't know anything, but I do know that everything is interesting if you go into it deeply enough.
\t- Richard Feynman""",
    """The universe seems neither benign nor hostile, merely indifferent.
\t- Carl Sagan"""
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
# current_date = datetime.datetime.now().strftime("%d-%m-%Y")
def ordinal(n):
    """Convert an integer into its ordinal representation."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return str(n) + suffix

now = datetime.datetime.now(ZoneInfo("Europe/London"))
month = now.strftime("%B")  # Full month name, e.g., "February"
day = ordinal(now.day)      # Day of the month with ordinal, e.g., "7th"
year = now.year             # Year, e.g., 2025


current_date = f"{month} {day}, {year}"
print(current_date)  # For example: February 7th, 2025

# Update the README.md file
readme_content = f"""# Welcome

{current_date}

### Daily Quote:
{blockquote_quote}

Stay Curious and keep Exploring!
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
