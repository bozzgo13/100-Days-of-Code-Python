from turtle import Turtle
class Socreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =  0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))
    def write_gane_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over!", align="center", font=("Arial", 30, "bold"))