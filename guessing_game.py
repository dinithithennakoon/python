#guessing game
from random import randint
from IPython.display import clear_output
guessed = False
number = randint(0,100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number I am thinking of!")
    # use tab to indent
    guesses += 1
    clear_output()
    if int(ans) == number:
        print("Congrats! You guesses it correctly.")
        # use tab twice to indent twice
        print("It took you { } guesses!" .format(guesses))
        break
    elif int(ans) > number:
        print("The number is lower then what you geussed.")
    elif int(ans) < number:
        print("The number is greater than what you geussed")