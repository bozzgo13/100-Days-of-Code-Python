from turtle import  Screen
from myturtle import MyTurtle
from scoreboard import Scoreboard
from traficgenerator import TraficGenerator
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Capstone")
screen.tracer(0)

turtle = MyTurtle()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(turtle.go_forward, "Up")
generator = TraficGenerator()


is_game_on = True
while is_game_on:
    scoreboard.update_scoreboard()
    screen.update()