from turtle import Screen


from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")


screen.title("The Pong Game")
screen.tracer(0)
paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(fun=paddle.up, key="Up")
screen.onkey(fun=paddle.down, key="Down")


game_is_on = True

while game_is_on:
    ball.move_ball()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()