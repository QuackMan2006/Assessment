"""My final code takes all the pieces and puts the together and adds some code
so that the game flows on and works properly."""
import random


def easy_hard(question_text):
    while True:

        # ask user if they would like to play easy or hard mode
        answer = input(question_text).lower()

        # if they say easy, output 'display instructions'
        if answer == "easy" or answer == "e":
            answer = "Easy"
            return "e"

        # if they say hard, output 'display other instructions'
        elif answer == "hard" or answer == "h":
            answer = "Hard"
            return "h"

        # otherwise - show error
        else:
            print("Please answer 'easy' or 'hard'")


# function to display instructions
def easy_instructions():
    print()
    print("**** How to play easy mode *****")
    print()
    print("The numbers one through")
    print("ten will be given to you")
    print("in Maori at random and you ")
    print("must input the correct")
    print("translation in english ")
    print()
    print("********************************")
    print()


# function to display instructions
def hard_instructions():
    print()
    print("***** How to play hard mode *****")
    print()
    print("You will be given all of the ")
    print("multiples of ten between one")
    print("and one hundred and a few multiples ")
    print("of five in Maori at random and have to ")
    print("input the correct english translation")
    print()
    print("**********************************")
    print()


# main routine go here...
challenge_level = easy_hard("Would you like to play easy or hard mode? ")

if challenge_level == "e":
    print(f"You chose '{challenge_level}' mode")
    easy_instructions()
    # This code puts the maori word and correct translation into lists
    # 1st list (maori word)
    Maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
             "waru", "iwa", "tekau"]
    # 2nd list
    English = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


else:
    print(f"You chose '{challenge_level}' mode")
    hard_instructions()
    # This code puts the maori word and correct translation into lists

    # 1st list (maori word)
    Maori = ["tekau", "rua tekau", "toru tekau", "wha tekau", "rima tekau", "ono tekau", "whitu tekau",
             "waru tekau", "iwa tekau", "kotahi rau"]
    # 2nd list
    English = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]


quiz = Maori.copy()
random.shuffle(quiz)
score = 0

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
        score += 1

    else:
        print(f"Wrong, the correct answer was {answer}")


print(f"Good effort. You scored {score} out of 10")
