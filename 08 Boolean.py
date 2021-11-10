num1 = float(input("Key in the first number: "))
num2 = float(input("Key in the second number: "))

if (num1 > num2):
    print(num1, "is greater than", num2)

elif(num1 == num2):
    print (num1, "is euqal to", num2)

else:
    print (num1, "is less than", num2)



    if (attendance >= 0.8):
        print ("The student has been approved.")

    else:
        print ("The student has failed due to attendance rate is lower than 80%.")

elif(attendance >= 0.8):
    print("The sudent has failed due to an average grade lower than 6.0.")


else:
    print("The student has failed due to an average grade lowert than 6.0 and attendance rate is lower than 80%") 
    


print("Average Grade: ", round(avg_grade, 2),
print ("Attendance Rate: ", str(round(attendance * 100),2) + "%")

