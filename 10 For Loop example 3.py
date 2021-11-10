import random

number = random.randint(0,10) 

guess = int(input("I have been thinking about a number between 1 to 10. Can you guess it?"))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope, try again."))

print("You guess the number. I am thinking of ",number)
