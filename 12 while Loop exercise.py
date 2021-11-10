import random

x = 0
people = []

while x < 8:
    person = input("Type the name of a person: ")
    people.append(person)
    x += 1

print (people)

index = random.randint(0,7)
random_person = people[index]

print ("Picking a random person: ", random_person)
