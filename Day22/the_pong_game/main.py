from turtle import Screen
from side import Side

from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")


screen.title("The Pong Game")
screen.tracer(0)
paddle1 = Paddle(Side.LEFT)
paddle2 = Paddle(Side.RIGHT)
ball = Ball()

screen.listen()
#right paddle up, down
screen.onkeypress(fun=paddle2.start_up, key="Up")
screen.onkeyrelease(fun=paddle2.stop, key="Up")
screen.onkeypress(fun=paddle2.start_down, key="Down")
screen.onkeyrelease(fun=paddle2.stop, key="Down")

# left paddle (W, S)
screen.onkeypress(fun=paddle1.start_up, key="w")
screen.onkeyrelease(fun=paddle1.stop, key="w")
screen.onkeypress(fun=paddle1.start_down, key="s")
screen.onkeyrelease(fun=paddle1.stop, key="s")


game_is_on = True

while game_is_on:
    paddle1.update_position()
    paddle2.update_position()
    ball.move_ball()
    screen.update()
    time.sleep(0.01)


screen.exitonclick()