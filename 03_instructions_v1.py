""" Took function from component 03_v1 as the basis for this new function which
incorporates both easy/hard and shows instructions"""


# functions go here...
def easy_hard(question_text):
    while True:

        # ask user if they would like to play easy or hard mode
        answer = input(question_text).lower()

        # if they say easy, output 'display instructions'
        if answer == "easy" or answer == "e":
            answer = "Easy"
            return answer

        # if they say hard, output 'display other instructions'
        elif answer == "hard" or answer == "h":
            answer = "Hard"
            return answer

        # otherwise - show error
        else:
            print("Please answer 'easy' or 'hard'")


# function to display instructions
def easy_instructions():
    print("**** How to play *****")
    print()
    print("the rules of the game will go here")
    print()
    print("program continues")
    print()


# function to display instructions
def hard_instructions():
    print("***** How to play *****")
    print()
    print("the rules of the game will go here")
    print()
    print("program continues")
    print()


# main routine go here...
challenge_level = easy_hard("Would you like to play easy or hard mode? ")

if challenge_level == "easy":
    print(f"You chose '{challenge_level}' mode")
    easy_instructions()

elif challenge_level == "hard":
    print(f"You chose '{challenge_level}' mode")
    hard_instructions()

else:
    print("program continues")
