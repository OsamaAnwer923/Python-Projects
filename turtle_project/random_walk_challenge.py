from turtle import Turtle,Screen
import random
screen = Screen()
screen.colormode(225)


direction = [0,90,180,270]
colors = ['blue','pale green','wheat','light pink','indigo','coral']

tim = Turtle()
tim.pensize(4)

for i in range(100):
    tim.forward(50)
    tim.left(random.choice(direction))
    tim.pencolor(random.choice(colors))

screen.exitonclick()    