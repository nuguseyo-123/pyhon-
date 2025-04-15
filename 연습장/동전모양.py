import random
a=print(random.randint(1,2))
import turtle
screen=turtle.Screen()
screen.addshape("front.gif")
screen.addshape("back.gif")
t=turtle.Turtle()
if a==1:
   t.screen("front.gif")
else:
    t.screen("bakc.gif")

    
