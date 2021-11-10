print ("This program is to calculate your BMI")

height = float(input("Key in your height in metres: "))
weight = float(input("Key in your weight in kilograms: "))

BMI = weight /(height * height) 

print ("Your BMI is: ", round(BMI, 1))

if (BMI >=18.5 and BMI<=24.9):
    print("You are normal weight.")

elif (BMI >24.9 and BMI <= 29.9):
    print("You are overweight")

elif (BMI <= 18.5):
    print ("You are underweight")

else:
    print ("You are obese")
