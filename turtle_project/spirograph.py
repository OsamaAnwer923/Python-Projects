from turtle import Turtle,Screen
import random
screen = Screen()
tim = Turtle()
tim.speed(0)
for j in range(90):
    tim.right(4)
    for i in range(361):
        tim.forward(2)
        tim.right(1)