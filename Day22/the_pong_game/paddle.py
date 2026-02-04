from side import Side
from turtle import Turtle
MOVE_DISTANCE = 50
PADDLE_X_POSITIONS = (-370, 370)
WINDOW_X_BOUNDS = (-365, +370)
WINDOW_Y_BOUNDS = (-370, +370)
PADDLE_SIZE=100
class Paddle(Turtle):
    def __init__(self, side:Side):
        super().__init__()

        if side == Side.LEFT:
            self.paddle_x_position = PADDLE_X_POSITIONS[0]
        else:
            self.paddle_x_position = PADDLE_X_POSITIONS[1]

        self.speed(0)
        self.penup()
        # self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(self.paddle_x_position,0)
        self.move_state = 0  # 0 = miruje, 1 = gor, -1 = dol
        #self.draw_paddle()

    def start_up(self):
        self.move_state = 1

    def start_down(self):
        self.move_state = -1

    def stop(self):
        self.move_state = 0

    def update_position(self):
        """Ta metoda se kliče v glavni zanki main.py"""
        if self.move_state == 1:
            y = self.ycor()
            if y < WINDOW_Y_BOUNDS[1] - PADDLE_SIZE/2:
                self.sety(y + 10) # Manjši korak za bolj tekoče gibanje
        elif self.move_state == -1:
            y = self.ycor()
            if y > WINDOW_Y_BOUNDS[0] + PADDLE_SIZE/2:
                self.sety(y - 10)
