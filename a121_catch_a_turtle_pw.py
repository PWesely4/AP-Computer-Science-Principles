# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
fill_color = ("green")
size = 2
shape = ("turtle")
score = 0
font_setup = ("Arial", 20, "normal")
#-----initialize turtle-----
turtle = trtl.Turtle()
turtle.shape(shape)
turtle.shapesize(size)
turtle.fillcolor(fill_color)
turtle.penup()
score_writer = trtl.Turtle()
#-----game functions--------
def change_position():
  (new_xpos) = rand.randint(-200,200)
  (new_ypos) = rand.randint(-200,200)
  turtle.goto(new_xpos,new_ypos)

def turtle_clicked(x,y):
  update_score()
  change_position()

def update_score():
  global score
  score = score + 1
  score_writer.write(score, font=font_setup)

def position_score_writer():
  score_writer.penup()
  score_writer.goto(200,200)

#-----events----------------
turtle.onclick(turtle_clicked)
position_score_writer()

wn = trtl.Screen()
wn.mainloop()