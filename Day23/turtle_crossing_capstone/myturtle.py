from turtle import Turtle

STEP_SIZE = 20
MAX_STEPS = 27

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.left(90)
        self.go_to_start()
        self.current_step = 0

    def go_to_start(self):
        self.goto(0, -270)

    def go_forward(self):
        self.forward(STEP_SIZE)
        self.current_step+=1;
        print(f"{self.ycor()} {self.current_step}")
