grade_1 = float(input("Type the grade of the first test: "))
grade_2 = float(input("Type the grade of the second test: "))

absences = int(input("Type the number of absences:"))

total_classes= int(input("Type the total number of classes: "))

avg_grade= (grade_1 + grade_2)/2

attendance = (total_classes - absences)/ total_classes

print("Average Grade: ", round(avg_grade, 2)),
print ("Attendance Rate: ", str(round((attendance * 100),2)) +"%")


if (avg_grade >= 6):
      if (attendance >=0.8):
          print ("The student has been approved.")

      else:
          print ("the sudent has failed due to attenance rate is lower than 80%.")
elif(attendance >= 0.8):
    print("The sudent has failed due to an average grade lower than 6.0.")


else:
    print("The student has failed due to an average grade lowert than 6.0 and attendance rate is lower than 80%") 


