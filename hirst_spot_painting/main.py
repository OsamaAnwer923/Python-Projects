import colorgram
import random
from turtle import Turtle,Screen
colors = colorgram.extract('painting2.jpg', 25)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))


tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)

for i in range(1,89):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    
    if i%8==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)


screen.exitonclick()