birthday = input("Please provide your birthday in DD-MM-YYYY: ")

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

x = int(birthday[3:5])

print("Your Birthday month is: ", month[x-1])
