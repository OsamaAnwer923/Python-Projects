from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,210)
        self.score = 0
        self.write(f"Score:{self.score}",False,align='center',font=("Arial", 30, "normal"))
        self.hideturtle()
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score:{self.score}",False,align='center',font=("Arial", 30, "normal"))
    def game_over(self):
        self.clear()
        self.write(f"Game Over Your Score:{self.score}",False,align='center',font=("Arial", 30, "normal"))