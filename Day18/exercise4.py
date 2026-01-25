# random walk
from turtle import Turtle
from turtle import Screen
import random
import colors


def walk_forward(steps):
    print("walk forward")
    turtle.forward(steps)
def walk_left(steps):
    print("walk left")
    turtle.left(90)
    turtle.forward(steps)
def walk_right(steps):
    print("walk right")
    turtle.right(90)
    turtle.forward(steps)

def walk_random_direction(steps):
    directions = [0, 90, 180, 270]
    random_direction = random.choice(directions)
    print(f"walk random direction {random_direction}")
    turtle.setheading(random_direction)
    turtle.forward(steps)

possible_walk =[walk_forward, walk_left, walk_right]


turtle = Turtle()
turtle.speed(0)  # speed up drawing
turtle.pensize(15)  # speed up drawing
screen = Screen()
screen.setup(width=800, height=800)

number_of_steps = 100
for i in range(number_of_steps):
    turtle.color(random.choice(colors.COLORS_32))
    # one option
    # random.choice(possible_walk)(20)
    # another option
    walk_random_direction(20)
screen.exitonclick()