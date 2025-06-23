import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#create a screen
screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()
#create a snake
snake = Snake()
food = Food()
screen.update()
game=True
snake_speed = 1
screen.listen()
screen.onkeypress(fun=snake.up,key='Up')
screen.onkeypress(fun=snake.down,key='Down')
screen.onkeypress(fun=snake.bkwd,key='Left')
screen.onkeypress(fun=snake.frwd,key='Right')
    
while game:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.snakes[0].distance(food)<15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
    elif snake.snakes[0].xcor()>240 or snake.snakes[0].xcor()<-240 or snake.snakes[0].ycor()>240 or snake.snakes[0].ycor()<-240:
        game=False
        scoreboard.game_over()
    for segment in snake.snakes[1:]:  # Skip the head
        if snake.snakes[0].distance(segment) < 10:
            game = False
            scoreboard.game_over()



screen.exitonclick()