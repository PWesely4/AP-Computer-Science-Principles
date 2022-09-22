# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
fill_color = ("green")
size = 2
shape = ("turtle")
#-----initialize turtle-----
turtle = trtl.Turtle()
turtle.shape(shape)
turtle.shapesize(size)
turtle.fillcolor(fill_color)
turtle.penup()
#-----game functions--------
def change_position():
  (new_xpos) = rand.randint(-200,200)
  (new_ypos) = rand.randint(-200,200)
  turtle.goto(new_xpos,new_ypos)

def turtle_clicked(x,y):
  change_position()
#-----events----------------
turtle.onclick(turtle_clicked)


wn = trtl.Screen()
wn.mainloop()