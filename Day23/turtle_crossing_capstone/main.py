import time
from turtle import  Screen
from myturtle import MyTurtle, MAX_STEPS
from scoreboard import Scoreboard
from traficgenerator import TraficGenerator

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Capstone")
screen.tracer(0)

turtle = MyTurtle()
scoreboard = Scoreboard()
generator = TraficGenerator()
screen.listen()

screen.onkeypress(turtle.go_forward, "Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_scoreboard()
    generator.update()
    if generator.colision_detection(turtle.current_step):
        is_game_on = False
        scoreboard.game_over()
    else:
        if turtle.current_step >= MAX_STEPS:
            turtle.go_to_start()
            scoreboard.increase_score()

screen.exitonclick()