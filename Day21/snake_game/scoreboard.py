from turtle import Turtle
class Socreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =  0

        file = open("highscore.txt", "r")
        content = file.read()
        file.close()
        self.highscore = int(content)
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
        self.write(f"Score: {self.score} High sore: {self.highscore}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("highscore.txt", "w")
            file.write(f"{self.highscore}")
            file.close()



        self.score = 0
        self.update_scoreboard()
#    def write_gane_over(self):
#        self.goto(x=0, y=0)
#        self.write("Game Over!", align="center", font=("Arial", 30, "bold"))