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
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
turtle = trtl.Turtle()
turtle.shape(shape)
turtle.shapesize(size)
turtle.fillcolor(fill_color)
turtle.penup()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
#-----game functions--------
def change_position():
  (new_xpos) = rand.randint(-200,200)
  (new_ypos) = rand.randint(-200,200)
  turtle.goto(new_xpos,new_ypos)

def turtle_clicked(x,y):
    if timer_up == False:
        score_writer.clear()
        update_score()
        change_position()
    else:
        turtle.goto(1000,1000)
    

def update_score():
  global score
  score = score + 1
  score_writer.write(score, font=font_setup)

def position_score_writer():
  score_writer.penup()
  score_writer.goto(200,200)

def position_counter():
  counter.penup()
  counter.goto(-200,200)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
#-----events----------------
turtle.onclick(turtle_clicked)
position_score_writer()
position_counter()
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()