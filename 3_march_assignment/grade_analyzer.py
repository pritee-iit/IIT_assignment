# Task 1
def process_scores(students):
  avgs = {}
  for name, scores in students.items():
    if scores:
      cal_avg = round(sum(scores)/len(scores),2)
    else:
      cal_avg = 0.00
    avgs[name] = cal_avg
  return avgs

# Task 2
def classify_grades(averages):
  threshold_grades_A = 90
  threshold_grades_B = 75
  threshold_grades_C = 60

  classified_grade = {}
  for name, avg in averages.items():
    if avg >= threshold_grades_A:
      grade = 'A'
    elif avg >= threshold_grades_B:
      grade = 'B'
    elif avg >= threshold_grades_C:
      grade = 'C'
    else:
      grade = 'F'
    classified_grade[name] = (avg, grade)
  return classified_grade

# Task 3
def generate_report(classified_grades,passing_avg=70):
  print("Student Report:")
  passed = 0
  total = len(classified_grades)
  for name, (avg,grade) in classified_grades.items():
    status = "Pass" if avg >= passing_avg else "Fail"
    if status == "Pass":
      passed += 1
    print(f"{name}: Average={avg}, Grade={grade}, Status={status}")

  failed = total-passed

  print(f"Total students: {total}")
  print(f"Number of students who passed: {passed}")
  print(f"Number of students who failed: {failed}")
  return passed

# called main function
if __name__ == "__main__":
  students = {
    "Alice":[85,90,88,82],
    "Bob":[67,90,65,59],
    "Clara":[90,99,97,89]
  }

  averages = process_scores(students)
  classified_grades = classify_grades(averages)
  generate_report(classified_grades)