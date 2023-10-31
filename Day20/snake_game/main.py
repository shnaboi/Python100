from turtle import Screen
import time
from snake import NewSnake
from food import Food
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = NewSnake()

screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

food = Food()
scoreboard = Scoreboard()

gaming = True
while gaming:
  # update the screen every .2 seconds
  screen.update()
  time.sleep(snake.speed)
  snake.move()

  if snake.head.distance(food) < 10:
    food.generate()
    snake.grow()
    scoreboard.score_up()


















screen.exitonclick()