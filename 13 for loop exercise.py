import random

multiple_colours = ["Red", "Green", "Blue", "White", "Orange", "Purple"]

while True:
    colour = multiple_colours[random.randint(0, len(multiple_colours)-1)]
    guess = input ("Can you guess what is the colour I am thinking of:")

    while True:
        if (colour == guess):
            break
        else:
            guess = input("Nope. Try again: ")

    print("You guessed it. I was thinking about: ", colour)

    play_again = input("Let's play again? Type 'no' to quit.")

    if play_again.lower() == "no":
        break

    print("Thank you for playing")

    

    



