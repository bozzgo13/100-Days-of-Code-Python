# Make a spirograph
from turtle import Turtle
from turtle import Screen
import random
import colors


turtle = Turtle()
turtle.speed(0)  # speed up drawing
screen = Screen()
screen.setup(width=800, height=800)


for i in range(90):
    turtle.left(4)
    turtle.color(random.choice(colors.COLORS_32))
    turtle.circle(150)

screen.exitonclick()