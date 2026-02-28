# step 3 : Grade calculation
name = input("Enter student name: ")
subject1 = float(input("Enter marks for subject1: "))
subject2 = float(input("Enter marks for subject2: "))
subject3 = float(input("Enter marks for subject3: "))

subject_total = subject1 + subject2 + subject3
percetage = (subject_total/300) *100

# check grade for student
if percetage >= 75:
  grade = "A"
elif percetage >= 60:
  grade = "B"
elif percetage >= 40:
  grade = "C"
else:
  grade = "A"

print("\n", name)
print("Total marks: ",subject_total,"/300")
print("Percentage: ",percetage)
print("Grade: ",grade)