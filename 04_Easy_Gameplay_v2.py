"""Version two of easy gameplay makes sure that the program keeps
asking you questions until each maori number is done once.
it uses 'pop' to do this."""

import random

# This code puts the maori word and correct translation into lists

# 1st list (maori word)
Maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
         "waru", "iwa", "tekau"]
# 2nd list
English = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


quiz = Maori.copy()
random.shuffle(quiz)


while len(quiz) > 0:

    question = quiz.pop()
    attempt = input(f"What number is this: {question}? ")
    # This uses indexing to find the corresponding number for Maori word
    # index position of answer
    if question in Maori:
        answer_index = Maori.index(question)
        answer = English[answer_index]

    if attempt == answer:
        print("##### CORRECT! #####\n")

    else:
        print(f"Wrong, the correct answer was {answer}")
