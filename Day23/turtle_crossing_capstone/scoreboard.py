from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def increase_score(self):
        self.score+=1
    def update_scoreboard(self):
        self.clear()
        self.goto(x=250, y=270)
        self.write(f"Score: {self.score}", align="right", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=("Arial", 18, "normal"))
        pass