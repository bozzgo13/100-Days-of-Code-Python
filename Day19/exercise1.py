from turtle import Turtle, Screen

# Make a Etch-a-Sketch with pyton and turtle library
# key W - go forwards
# key S - go backwards
# key A - go counter-clockwise
# key D - go clockwise
# key C - clear drawing and move turtle back to the center


turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)
def move_backwards():
    turtle.backward(10)
def rotate_left():
    turtle.left(10)
def rotate_right():
    turtle.right(10)
def reset_drawing():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=reset_drawing)
screen.exitonclick()


