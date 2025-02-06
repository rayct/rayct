import random
import datetime

# List of scientific quotes with the hyphen and author on a new, tabbed line.
# A zero-width space (\u200b) is inserted right after the hyphen
# to prevent Markdown from turning it into a bullet.
quotes = [
    "Science is a way of thinking much more than it is a body of knowledge.\n\t-\u200b Carl Sagan",
    "The important thing is not to stop questioning. Curiosity has its own reason for existing.\n\t-\u200b Albert Einstein",
    "Equipped with his five senses, man explores the universe around him and calls the adventure Science.\n\t-\u200b Edwin Powell Hubble",
    "Somewhere, something incredible is waiting to be known.\n\t-\u200b Carl Sagan",
    "Science is organized knowledge. Wisdom is organized life.\n\t-\u200b Immanuel Kant",
    "The good thing about science is that it’s true whether or not you believe in it.\n\t-\u200b Neil deGrasse Tyson",
    "If you can't explain it simply, you don't understand it well enough.\n\t-\u200b Albert Einstein",
    "The most incomprehensible thing about the world is that it is comprehensible.\n\t-\u200b Albert Einstein",
    "The universe is under no obligation to make sense to you.\n\t-\u200b Neil deGrasse Tyson",
    "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.\n\t-\u200b Albert Einstein",
    "To confine our attention to terrestrial matters would be to limit the human spirit.\n\t-\u200b Stephen Hawking",
    "We are star stuff, we are the cosmos made conscious and life is the means by which the universe understands itself.\n\t-\u200b Carl Sagan",
    "The universe is not only stranger than we imagine, it is stranger than we can imagine.\n\t-\u200b J.B.S. Haldane",
    "Physics is not about how the world is, it is about what we can say about the world.\n\t-\u200b Niels Bohr",
    "The beauty of a flower is a scientific fact.\n\t-\u200b Richard P. Feynman",
    "Time is an illusion. Lunchtime doubly so.\n\t-\u200b Douglas Adams, *The Hitchhiker's Guide to the Galaxy*",
    "I think we have a great responsibility to understand our role in the universe.\n\t-\u200b Neil deGrasse Tyson",
    "The whole of science is nothing more than a refinement of everyday thinking.\n\t-\u200b Albert Einstein",
    "I do not believe that the universe is in any way different from what it seems to be, but I do believe that we do not know nearly enough to have the right to be sure.\n\t-\u200b J. B. S. Haldane",
    "The laws of physics are the same everywhere in the universe.\n\t-\u200b Stephen Hawking",
    "We are like butterflies who flutter for a day and think it is forever.\n\t-\u200b Carl Sagan",
    "Everything is theoretically impossible, until it is done.\n\t-\u200b Robert A. Heinlein",
    "Astronomy compels the soul to look upwards and leads us from this world to another.\n\t-\u200b Plato",
    "The great discovery of our age is that we can know the structure of the universe, the structure of the atom, and the structure of life.\n\t-\u200b Richard P. Feynman",
    "In science, there are no shortcuts to truth.\n\t-\u200b Karl Popper"
]

# Choose a random quote
quote = random.choice(quotes)

# Get current date
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Update the README.md file
readme_content = f"""# Welcome

{current_date}

### Daily Quote:
> {quote}

Stay Curious and keep Exploring!
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
