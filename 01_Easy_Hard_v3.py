""" MN easy/hard
puts code created in v2 into a loop to make testing easier and more
efficient.
"""

show_instructions = ""
while show_instructions != "x":

    # ask user if they would like to play easy or hard mode
    show_instructions = input("Would you like to play easy or hard mode? : ")

    # if they say easy, output 'program continues'
    if show_instructions == "easy" or show_instructions == "e":
        print("Display instructions")

    # if they say hard, output 'display instructions'
    elif show_instructions == "hard" or show_instructions == "h":
        print("Display instructions")

    # otherwise - show error
    else:
        print("Please answer 'easy' or 'hard'")

    print(f"You entered '{show_instructions}'")
