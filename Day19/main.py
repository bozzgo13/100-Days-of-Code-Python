from turtle import Turtle, Screen
import random
def setup_timmy():
    timmy.shape("turtle")
    timmy.color("red2")
    timmy.penup()
    timmy.goto(-220, 0)
    #timmy.pendown()
def setup_tolly():
    tolly.shape("turtle")
    tolly.color("green")
    tolly.penup()
    tolly.goto(-220, -50)
    #tolly.pendown()
def setup_teddy():
    teddy.shape("turtle")
    teddy.color("blue")
    teddy.penup()
    teddy.goto(-220, -100)
    #teddy.pendown()
def setup_tiffy():
    tiffy.shape("turtle")
    tiffy.color("deeppink")
    tiffy.penup()
    tiffy.goto(-220, 50)
    #tiffy.pendown()
def setup_tasha():
    tasha.shape("turtle")
    tasha.color("magenta4")
    tasha.penup()
    tasha.goto(-220, 100)
    #tasha.pendown()

def hide_all():
    timmy.hideturtle()
    tasha.hideturtle()
    tiffy.hideturtle()
    teddy.hideturtle()
    tolly.hideturtle()

def show_all():
    timmy.showturtle()
    tasha.showturtle()
    tiffy.showturtle()
    teddy.showturtle()
    tolly.showturtle()

def add_extra():
    constructor = Turtle()
    constructor.hideturtle()
    constructor.speed(0)
    constructor.penup()
    constructor.goto(-220, -150)
    constructor.pendown()
    constructor.left(90)
    constructor.forward(300)
    constructor.penup()
    constructor.goto(200, -150)
    constructor.pendown()
    constructor.forward(300)
    constructor.penup()
    constructor.goto(205, -150)
    constructor.pendown()
    constructor.forward(300)


screen = Screen()
screen.setup(width=500, height=400)
add_extra()
user_bet = screen.numinput(title="Make your bet", prompt="Which turtle will win the race? Type\n1 for Timmy (red)\n2 for Tolly (green)\n3 for Teddy (blue)\n4 for Tiffy (pink)\n5 for Tasha (magenta): ")

timmy = Turtle()
tolly  = Turtle()
teddy = Turtle()
tiffy = Turtle()
tasha  = Turtle()

hide_all()
setup_timmy()
setup_tolly()
setup_teddy()
setup_tiffy()
setup_tasha()
show_all()

max_x_position = 0
winning_number=0
winning_turtle_name=""
turtle_number=0
# log_message =""

while max_x_position < 180:
    # log_message = ""
    for turtle in [tasha, tiffy, timmy, tolly, teddy]:
        turtle.forward(random.randint(0,10))
        turtle_name=""
        x = turtle.xcor()  # For x-coordinate
        if turtle is tasha:
            turtle_name = "Tasha"
            turtle_number = 5
        elif turtle is tiffy:
            turtle_name = "Tiffy"
            turtle_number = 4
        elif turtle is timmy:
            turtle_name = "Timmy"
            turtle_number = 1
        elif turtle is tolly:
            turtle_name = "Tolly"
            turtle_number = 2
        else:
            turtle_name = "Teddy"
            turtle_number = 3


        # log_message += f" {turtle_name} : {x}"

        if max_x_position < x:
            max_x_position = x
            winning_number = turtle_number
            winning_turtle_name = turtle_name

    # print(log_message)

if winning_number == user_bet:
    print(f"Congratulations! You've won! Winning turtle is {winning_turtle_name} (number {winning_number})")
else:
    print(f"Unfortunately, You've lost! Winning turtle is {winning_turtle_name} (number {winning_number})")


screen.exitonclick()