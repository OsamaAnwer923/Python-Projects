from turtle import Turtle,Screen

jim = Turtle()
screen = Screen()

screen.colormode(255)

def frwd():
    jim.setheading(0)
    jim.forward(10)
    


def bkwd():
    jim.setheading(180)
    jim.forward(10)
    

def up():
    jim.setheading(90)
    jim.forward(10)
    

def down():
    jim.setheading(270)
    jim.forward(10)

def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()
    
screen.listen()
screen.onkeypress(key='d',fun=frwd)
screen.onkeypress(key='a',fun=bkwd)
screen.onkeypress(key='w',fun=up)
screen.onkeypress(key='s',fun=down)
screen.onkeypress(key='c',fun=clear)

screen.exitonclick()