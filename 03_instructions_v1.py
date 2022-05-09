""" Took function from component 03_v1 as the basis for this new function which
incorporates both easy/hard and shows instructions"""


# functions go here...
def easy_hard(question_text):
    while True:

        # ask user if they've played before
        answer = input(question_text).lower()

        # if they say easy, output 'display instructions'
        if answer == "easy" or answer == "e":
            answer = "Easy"
            return answer

        # if they say hard, output 'display instructions'
        elif answer == "hard" or answer == "h":
            answer = "Hard"
            return answer

        # otherwise - show error
        else:
            print("Please answer 'easy' or 'hard'")


# function to display instructions
def instructions_1():
    print("**** How to play *****")
    print()
    print("the rules of the game will go here")
    print()
    print("program continues")
    print()


# function to display instructions
def instructions_2():
    print("***** How to play *****")
    print()
    print("the rules of the game will go here")
    print()
    print("program continues")
    print()


# main routine go here...
challenge_level = easy_hard("Would you like to play easy or hard mode? ")

if challenge_level == "easy":
    instructions_1()

else:
    print("program continues")
