#draw square
from turtle import Turtle
from turtle import Screen



turtle = Turtle()
#turtle.speed(0)  # speed up drawing
screen = Screen()
screen.setup(width=800, height=800)


for i in range(4):
    turtle.forward(100)
    turtle.left(90)


screen.exitonclick()