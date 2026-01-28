import time
from snake import Snake
from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0) # Turn turtle animation on/off and set delay for update drawings. I

snake = Snake()
screen.listen() #for listening keystrokes
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()  # need to update as tracer is off
    time.sleep(0.1)



screen.exitonclick()