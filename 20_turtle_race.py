from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=500)
user_color_bet=screen.textinput('Turtle Race Bet',"select a turtle for bet among the colors 'green','blue','orange','yellow','purple','red' ").lower()
colors = ['green','blue','orange','yellow','purple','red']
all_turtles = []
for turtles in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(-225,-50+30*turtles)
    all_turtles.append(new_turtle)
    
game=True
while game:
    for turtle in all_turtles:
        if turtle.xcor()>=220:
            wining_color=turtle.color()[0]
            game=False
            if wining_color==user_color_bet:
                print("you won the bet")
            else:
                print(f"you loose the bet. {wining_color} won the race")
        turtle.forward(random.randint(0,10))

screen.exitonclick()