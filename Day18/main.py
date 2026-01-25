# Turtle documentation: https://docs.python.org/3/library/turtle.html

from turtle import Turtle
from turtle import Screen
import random
import colors



turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)  # speed up drawing
screen = Screen()
screen.setup(width=800, height=800)

start_x = -350
start_y = -350
distance_between = 50
circle_radius = 10
turtle.penup()

for row in range(15):
    # Set turtle to the start of a new row
    turtle.goto(start_x, start_y + (row * distance_between))

    for column in range(15):
        # pen_color = random.choice(colors.COLORS)
        fill_color = random.choice(colors.COLORS)
        turtle.color(fill_color)

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(circle_radius)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(distance_between)

screen.exitonclick()