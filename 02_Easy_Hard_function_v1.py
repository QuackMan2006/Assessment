""" MN easy/hard
puts code created in v2 into a loop to make testing easier and more
efficient.
"""


# functions go here...
def easy_hard(question_text):
    while True:

        # Would they like to play easy, or hard mode
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


# main routine go here...
show_instructions = easy_hard("Would you like to play easy or hard mode? ")
print(f"You chose '{show_instructions}' mode")
print()

