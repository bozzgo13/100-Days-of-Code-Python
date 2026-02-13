from turtle import Turtle

STEP_SIZE = 24
MAX_STEPS = 22

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.left(90)
        self.current_step = 0
        self.go_to_start()

    def go_to_start(self):
        self.goto(0, -270)
        self.current_step =0

    def go_forward(self):
        self.clear()
        self.forward(STEP_SIZE)
        self.current_step+=1