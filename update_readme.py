import random
import datetime

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
- Neil deGrasse Tyson""",
    """If you can't explain it simply, you don't understand it well enough.
- Albert Einstein""",
    """The most incomprehensible thing about the world is that it is comprehensible.
- Albert Einstein""",
    """The universe is under no obligation to make sense to you.
- Neil deGrasse Tyson""",
    """There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
- Albert Einstein""",
    """To confine our attention to terrestrial matters would be to limit the human spirit.
- Stephen Hawking""",
    """We are star stuff, we are the cosmos made conscious and life is the means by which the universe understands itself.
- Carl Sagan""",
    """The universe is not only stranger than we imagine, it is stranger than we can imagine.
- J.B.S. Haldane""",
    """Physics is not about how the world is, it is about what we can say about the world.
- Niels Bohr""",
    """The beauty of a flower is a scientific fact.
- Richard P. Feynman""",
    """Time is an illusion. Lunchtime doubly so.
- Douglas Adams, *The Hitchhiker's Guide to the Galaxy*""",
    """I think we have a great responsibility to understand our role in the universe.
- Neil deGrasse Tyson""",
    """The whole of science is nothing more than a refinement of everyday thinking.
- Albert Einstein""",
    """I do not believe that the universe is in any way different from what it seems to be, but I do believe that we do not know nearly enough to have the right to be sure.
- J. B. S. Haldane""",
    """The laws of physics are the same everywhere in the universe.
- Stephen Hawking""",
    """We are like butterflies who flutter for a day and think it is forever.
- Carl Sagan""",
    """Everything is theoretically impossible, until it is done.
- Robert A. Heinlein""",
    """Astronomy compels the soul to look upwards and leads us from this world to another.
- Plato""",
    """The great discovery of our age is that we can know the structure of the universe, the structure of the atom, and the structure of life.
- Richard P. Feynman""",
    """In science, there are no shortcuts to truth.
- Karl Popper"""
]


# Join all the quotes into a single string with each quote separated by a newline
formatted_quotes = "\n\n".join(quotes)

# Choose a random quote
quote = random.choice(quotes)

# Get current date
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Update the README.md file
readme_content = f"""# Welcome


{current_date}

### Daily Quote:
> {quote}

Stay curious and keep Exploring!
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
