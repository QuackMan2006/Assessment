"""Version two of hard gameplay makes sure that the program keeps
asking you questions until each maori number is done once.
it uses 'pop' to do this."""

import random

# This code puts the maori word and correct translation into lists

# 1st list (maori word)
Maori = ["tekau", "rua tekau", "toru tekau", "wha tekau", "rima tekau", "ono tekau", "whitu tekau",
         "waru tekau", "iwa tekau", "kotahi rau"]
# 2nd list
English = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]


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
