import random
from turtle import Turtle

STEP = 3

class Ball(Turtle):
    def __init__(self):
        self.angles = [0, 30, 45, 60, 75, 120, 150, 210, 225, 240, 300, 315, 330]
        self.current_angle = 0
        super().__init__()
        self.speed(0)
        self.speed_bonus = 0
        self.showturtle()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.begin_from_start()


    def reflect_across_x(self, angle):
        """
        Reflects an angle across the x-axis.
        Example: 45 degrees becomes 315 degrees.
        """
        return (360 - angle) % 360

    def reflect_across_y(self, angle):
        """
        Reflects an angle across the y-axis.
        Example: 45 degrees becomes 135 degrees.
        """
        return (180 - angle) % 360

    def begin_from_start(self):
        self.goto(0, random.randint(-200, 200))
        self.current_angle = random.choice(self.angles)
        self.setheading(self.current_angle)
        self.speed_bonus = 0

    def move_ball(self, paddle1y,paddle2y):
        self.forward(STEP+self.speed_bonus)
        paddle1_y_min = paddle1y-50
        paddle1_y_max = paddle1y+50

        paddle2_y_min = paddle2y-50
        paddle2_y_max = paddle2y+50

        x = self.xcor()
        y = self.ycor()
        if -380 >= y  or y >= 380:
            self.current_angle = self.reflect_across_x(self.current_angle)
            self.setheading(self.current_angle)

        if x <= -343 and x > -350 and y > paddle1_y_min and y < paddle1_y_max:
            self.current_angle = self.reflect_across_y(self.current_angle)
            self.setheading(self.current_angle)
            self.speed_bonus +=.1

        if x >= 341 and x < 346 and y > paddle2_y_min and y < paddle2_y_max:
            self.current_angle = self.reflect_across_y(self.current_angle)
            self.setheading(self.current_angle)
            self.speed_bonus +=.1
        # print(f"x:{self.xcor()}, y:{self.ycor()} direction: {self.current_angle} p1:({paddle1_y_min}|{paddle1_y_max}) p2:({paddle2_y_min}|{paddle2_y_max})")
