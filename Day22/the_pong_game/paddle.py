from turtle import Turtle
MOVE_DISTANCE = 50
PADDLE_X_POSITION = -370
WINDOW_X_BOUNDS = (-370, +370)
WINDOW_Y_BOUNDS = (-370, +370)
PADDLE_SIZE=100
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.goto(PADDLE_X_POSITION,0)
        self.draw_paddle()

    def up(self):
        y = self.ycor()
        x = self.xcor()
        if y < WINDOW_Y_BOUNDS[1]-PADDLE_SIZE/2:
            self.penup()
            self.goto(PADDLE_X_POSITION, y+MOVE_DISTANCE)
        print(f"x:{self.xcor()}, y:{self.ycor()}")
        self.pendown()
        self.draw_paddle()

    def down(self):
        y = self.ycor()
        x = self.xcor()
        if y > WINDOW_Y_BOUNDS[0]+PADDLE_SIZE/2:
            self.penup()
            self.goto(PADDLE_X_POSITION, y - MOVE_DISTANCE)

        print(f"x:{self.xcor()}, y:{self.ycor()}")
        self.pendown()
        self.draw_paddle()

    def draw_paddle(self):
        self.clear()
        with self.fill():
            self.left(90)
            self.forward(PADDLE_SIZE/2)
            self.left(90)
            self.forward(20)
            self.left(90)
            self.forward(PADDLE_SIZE)
            self.left(90)
            self.forward(20)
            self.left(90)
            self.forward(PADDLE_SIZE/2)
            self.right(90)