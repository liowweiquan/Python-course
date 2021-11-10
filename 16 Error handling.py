
data_valid = False

while data_valid == False:
    grade_1 = input("Type the grade of the first test: ")

    try:
        grade_1 = float (grade_1)

    except:
        print ("Invalid result")

        continue
        
    if grade_1< 0 or grade_1>10:
        print ("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    grade_2 = input("Type the grade of the second test: ")

    try:
        grade_2 = float(grade_2)

    except:
        print ("Invalid result")

        continue
    
    if grade_2< 0 or grade_2>10:
        print ("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    total_classes= input("Type the total number of classes: ")

    try:
        total_classes = float (total_classes)

    except:
        print ("Invalid result")

        continue
    
    if total_classes <= 0:
        print ("Classes cannot be 0 or less")
        continue
    else:
        data_valid = True
data_valid = False

while data_valid == False:
    absences = input("Type the number of absences:")

    try:
        absences = float (absences)

    except:
        print ("Invalid result")

        continue
    if absences < 0 or absences > total_classes < absences:
        print ("Absesnces can be more than 0")
        
        continue
    else:
        data_valid = True




avg_grade= (grade_1 + grade_2)/2

attendance = (total_classes - absences)/ total_classes

print("Average Grade: ", round(avg_grade, 2)),
print ("Attendance Rate: ", str(round((attendance * 100),2)) +"%")


if (avg_grade >= 6 and attendance >= 0.8):
          print ("The student has been approved.")

      
elif(avg_grade<= 6 and attendance <= 0.8):
      print("The student has failed due to an average grade lowert than 6.0 and attendance rate is lower than 80%")

elif(attendance >= 0.8):
       print("The sudent has failed due to an average grade lower than 6.0.") 

else:
    print("The sudent has failed due to an attendance rate lower than 80%") 


