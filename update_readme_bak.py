import os
import random

# --- Master list of quotes (original + new ones) ---
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
	- Karl Popper""",
    """Science is a way of trying not to fool yourself. The first principle is that you must not fool yourself.
	- Richard Feynman""",
    """I would rather have questions that can't be answered than answers that can't be questioned.
	- Richard Feynman""",
    """If I have seen further it is by standing on the shoulders of giants.
	- Isaac Newton""",
    """The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom.
	- Isaac Asimov""",
    """Mathematics is the language with which God has written the universe.
	- Galileo Galilei""",
    """Research is what I'm doing when I don't know what I'm doing.
	- Wernher von Braun""",
    """It is the tension between creativity and skepticism that has produced the stunning and unexpected findings of science.
	- Carl Sagan""",
    """The important thing in science is not so much to obtain new facts as to discover new ways of thinking about them.
	- William Lawrence Bragg""",
    """Science is the great antidote to the poison of enthusiasm and superstition.
	- Adam Smith""",
    """The universe is full of magical things patiently waiting for our wits to grow sharper.
	- Eden Phillpotts""",
    """Science, my lad, is made up of mistakes, but they are mistakes which it is useful to make, because they lead little by little to the truth.
	- Jules Verne""",
    """Exploration is in our nature. We began as wanderers, and we are wanderers still.
	- Carl Sagan""",
    """For me, it is far better to grasp the Universe as it really is than to persist in delusion, however satisfying and reassuring.
	- Carl Sagan""",
    """I don't know anything, but I do know that everything is interesting if you go into it deeply enough.
	- Richard Feynman""",
    """The universe seems neither benign nor hostile, merely indifferent.
	- Carl Sagan""",
    """Nothing in life is to be feared, it is only to be understood.
	- Marie Curie""",
    """An experiment is a question which science poses to Nature, and a measurement is the recording of Nature’s answer.
	- Max Planck""",
    """The task is not so much to see what no one yet has seen, but to think what nobody yet has thought about that which everybody sees.
	- Erwin Schrödinger""",
    """The day science begins to study non-physical phenomena, it will make more progress in one decade than in all the previous centuries of its existence.
	- Nikola Tesla""",
    """Look deep into nature, and then you will understand everything better.
	- Albert Einstein""",
    """The scientist is not a person who gives the right answers, he’s one who asks the right questions.
	- Claude Lévi-Strauss""",
    """What we observe is not nature itself, but nature exposed to our method of questioning.
	- Werner Heisenberg""",
    """Intelligence is the ability to adapt to change.
	- Stephen Hawking""",
    """The cure for boredom is curiosity. There is no cure for curiosity.
	- Dorothy Parker""",
    """He who is fixed to a star does not change his mind.
	- Leonardo da Vinci""",
    """We are an impossibility in an impossible universe.
	- Ray Bradbury""",
    """We can only see a short distance ahead, but we can see plenty there that needs to be done.
	- Alan Turing""",
    """We still do not know one thousandth of one percent of what nature has revealed to us.
	- Albert Einstein""",
    """I am among those who think that science has great beauty.
	- Marie Curie""",
    """Only those who attempt the absurd can achieve the impossible.
	- Albert Einstein""",
    """Science knows no country, because knowledge belongs to humanity, and is the torch which illuminates the world.
	- Louis Pasteur""",
    """It is not knowledge, but the act of learning, not possession but the act of getting there, which grants the greatest enjoyment.
	- Carl Friedrich Gauss""",
    """The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge.
	- Stephen Hawking""",
    """The more I study science, the more I believe in God.
	- Albert Einstein""",
    """Chimpanzees, gorillas, orangutans have been living for hundreds of thousands of years in their forest, living fantastic lives, never overpopulating, never destroying the forest.
	- Jane Goodall"""
]

# --- Read existing quotes if file exists ---
existing_quotes = set()
if os.path.exists("quotes.txt"):
    with open("quotes.txt", "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content:
            for block in content.split("\n\n"):
                q = block.strip()
                if q:
                    existing_quotes.add(q)

# --- Add new quotes that are not duplicates ---
new_quotes = []
for q in quotes:
    q_clean = q.strip()
    if q_clean not in existing_quotes:
        new_quotes.append(q_clean)
        existing_quotes.add(q_clean)

# --- Preserve random order (no sorting) ---
final_quotes = list(existing_quotes)
random.shuffle(final_quotes)

# --- Write back to quotes.txt ---
with open("quotes.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(final_quotes) + "\n")

print(f"✅ quotes.txt updated with {len(new_quotes)} new quotes. Total now: {len(final_quotes)}.")
