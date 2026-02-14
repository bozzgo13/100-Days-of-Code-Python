import time

from food import Food
from scoreboard import Socreboard
from snake import Snake
from turtle import Screen
GAME_SLEEP = .05

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0) # Turn turtle animation on/off and set delay for update drawings. I

snake = Snake()
food = Food()
scoreboard = Socreboard()
screen.listen() #for listening keystrokes
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()  # need to update as tracer is off
    time.sleep(GAME_SLEEP)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()
    #detect collision with walls
    if  (snake.head.xcor() >= 280 or snake.head.xcor() <= -280
            or snake.head.ycor() >= 280 or snake.head.ycor() <= -280):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()