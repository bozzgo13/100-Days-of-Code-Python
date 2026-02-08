from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score =  0
        self.right_score =  0
        self.penup()
        self.color("white")
        self.hideturtle()

        self.update_scoreboard()

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=330)
        self.write(f"Score", align="center", font=("Arial", 20, "normal"))
        self.goto(x=0, y=300)
        self.write(f"{self.left_score} - {self.right_score}", align="center", font=("Arial", 20, "normal"))
    #def write_gane_over(self):
    #    self.goto(x=0, y=0)
    #    self.write("Game Over!", align="center", font=("Arial", 30, "bold"))