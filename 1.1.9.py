#1.1.9 AP Exam Practice
import turtle as trtl
painter = trtl.Turtle()
sides_list = []
heading = 270
number_of_sides = int(input("enter a number "))
orginal_number_of_sides = number_of_sides

#set cursor position
painter.penup()
painter.goto(-250,0)
painter.pendown()
painter.pensize(5)

#set up list of numbers
while number_of_sides > 0:
  sides_list.append(number_of_sides)
  number_of_sides = number_of_sides - 1

# set color if odd or even number of sides
if orginal_number_of_sides % 2 == 1:
  painter.pencolor("green")
elif orginal_number_of_sides % 2 == 0:
  painter.pencolor("red")

# draw shape
for number in sides_list:
  heading = heading + (360/orginal_number_of_sides)
  painter.setheading(heading)
  painter.forward(100)

wn = trtl.Screen()
wn.mainloop()