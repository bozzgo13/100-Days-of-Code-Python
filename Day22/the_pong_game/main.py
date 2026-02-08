from turtle import Screen
from side import Side

from ball import Ball
from paddle import Paddle, WINDOW_X_BOUNDS
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")


screen.title("The Pong Game")
screen.tracer(0)
paddle1 = Paddle(Side.LEFT)
paddle2 = Paddle(Side.RIGHT)
ball = Ball()
scoreboard = Scoreboard()

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
# used for testing and controlling ball movement
#screen.onkeypress(fun=lambda: ball.move_ball(paddle1.ycor(), paddle2.ycor()), key="x")

game_is_on = True

while game_is_on:
    paddle1.update_position()
    paddle2.update_position()
    if ball.xcor()< WINDOW_X_BOUNDS[0]-100:
        scoreboard.increase_right_score()
        ball.begin_from_start()
    elif ball.xcor()> WINDOW_X_BOUNDS[1]+100:
        scoreboard.increase_left_score()
        ball.begin_from_start()
    else:
         ball.move_ball(paddle1.ycor(),paddle2.ycor())

    scoreboard.update_scoreboard()
    screen.update()
    time.sleep(0.01)


screen.exitonclick()