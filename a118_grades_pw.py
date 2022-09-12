#   a118_grades_pw.py
my_courses = ["English", "Math", "CS"]
x = 0
redo = "y"
while (redo == "y"):
  print(redo)
  for course in my_courses:
    print(course)
    points = int(input("Points -> "))
    if (points >= 90):
      print("A")
    elif (points >= 80):
      print("B")
    elif (points >= 70):
      print("C")
    elif (points >= 60):
      print("D")
    else:
      print("F")

  redo = input("Do you need to re-do these grades? (y/n)")