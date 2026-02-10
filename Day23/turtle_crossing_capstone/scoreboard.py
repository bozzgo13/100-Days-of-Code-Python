from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=250, y=270)
        self.write(f"Score: {self.score}", align="right", font=("Arial", 18, "normal"))