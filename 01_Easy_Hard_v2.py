"""MN Easy / Hard
simplifies the input by converting it to lower case. also, accepts 'e' or 'h' as
abbreviations. print results of user choice as well as input - for testing.
"""

# ask user if they would like to play easy or hard mode
show_instructions = input("Would you like to play easy or hard mode?: ").lower()

# if they say easy, output 'display instructions'
if show_instructions == "easy" or show_instructions == "e":
    print("display instructions")

# if they say hard, output 'display instructions'
elif show_instructions == "hard" or show_instructions == "h":
    print("Display instructions")


# otherwise - show error
else:
    print("Please answer 'easy' or 'hard'")

print(f"You entered '{show_instructions}'")
