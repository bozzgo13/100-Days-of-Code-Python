# Draw dashed line
from turtle import Turtle
from turtle import Screen

turtle = Turtle()
screen = Screen()
screen.setup(width=800, height=800)

for i in range(15):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen.exitonclick()