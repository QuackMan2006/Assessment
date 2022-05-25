"""Version one of hard gameplay works using the base code from easy gameplay
version one, but modified to include different numbers."""

import random

# This code puts the maori word and correct translation into lists

# 1st list (maori word)
Maori = ["tekau", "rua tekau", "toru tekau", "wha tekau", "rima tekau", "ono tekau", "whitu tekau",
         "waru tekau", "iwa tekau", "kotahi rau"]
# 2nd list
English = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]

question = random.choice(Maori)
attempt = input(f"What number is this: {question}? ")

# This uses indexing to find the corresponding number for Maori word
# index position of answer
answer_index = Maori.index(question)
answer = English[answer_index]

# this part tells you if you got the question correct or not
if attempt == answer:
    print("##### CORRECT! #####\n")

else:
    print(f"Wrong, the correct answer was {answer}")
