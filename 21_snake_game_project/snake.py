from turtle import Turtle,Screen
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    def extend(self):
        self.add_segment(self.snakes[-1].position())
    def move_snake(self):
        for snake_number in range(len(self.snakes)-1,0,-1):
            self.snakes[snake_number].goto(self.snakes[snake_number-1].xcor(),self.snakes[snake_number-1].ycor())
        self.snakes[0].forward(10)
    def frwd(self):
        if self.snakes[0].heading()!=180:
            self.snakes[0].setheading(0)
    def bkwd(self):
        if self.snakes[0].heading()!=0:
            self.snakes[0].setheading(180)
    def up(self):
        if self.snakes[0].heading()!=270:
            self.snakes[0].setheading(90)
    def down(self):
        if self.snakes[0].heading()!=90:
            self.snakes[0].setheading(270)  