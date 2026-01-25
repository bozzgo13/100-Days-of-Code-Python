# draw different shapes
from colors import COLORS_8


from turtle import Turtle
from turtle import Screen

turtle = Turtle()
turtle.speed(0)  # speed up drawing
screen = Screen()
screen.setup(width=800, height=800)
turtle.penup()
turtle.goto(-50, -250)
turtle.pendown()

for i in range(64): # different shapes
    angle=360/(4+i)
    turtle.color(COLORS_8[i%8])
    for j in range(4+i):
        turtle.forward(25)
        turtle.left(angle)



screen.exitonclick()