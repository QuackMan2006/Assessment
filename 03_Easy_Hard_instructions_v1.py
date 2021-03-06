""" Took function from component 03_v1 as the basis for this new function which
incorporates both easy/hard and shows instructions for
how to play each game mode"""


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

if challenge_level == "Easy":
    print(f"You chose '{challenge_level}' mode")
    easy_instructions()

elif challenge_level == "Hard":
    print(f"You chose '{challenge_level}' mode")
    hard_instructions()

else:
    print("program continues")
