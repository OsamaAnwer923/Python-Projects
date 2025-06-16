from turtle import Turtle,Screen
import random
timy_the_turtle = Turtle()
timy_the_turtle.shape('turtle')
timy_the_turtle.shapesize(1,1,1)
timy_the_turtle.color('red')

colors = ['red','green','yellow','blue'] 
for j in range(3,10):
    for i in range(j):
        timy_the_turtle.right(360/j)
        timy_the_turtle.forward(100)
    timy_the_turtle.pencolor(random.choice(colors))


screen = Screen()
screen.exitonclick()
