import random
from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        self.direction_x = random.choice([True, False])
        self.direction_y = random.choice([True, False])
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(0,random.randint(-200, 200))
        self.draw_ball()

    def draw_ball(self):
        self.clear()
        with self.fill():
            self.circle(10)

    def move_ball(self):
        x = self.xcor()
        y = self.ycor()
        if  self.direction_x == True:
            x += 20
        else:
            x -= 20
        if  self.direction_y == True:
            y += 20
        else:
            y -= 20
        self.goto(x, y)
        self.draw_ball()