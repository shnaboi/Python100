from turtle import Screen
import time
from snake import NewSnake
from food import Food
from scoreboard import Scoreboard

gaming = True

# def replay():
#   global gaming
#   if not gaming:
#     gaming = True
#     screen.clear()
#     screen.bgcolor("black")
#     screen.title("Snake")
#     snake = NewSnake()
#     scoreboard.score = 0
#     game()
#     print('p')

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = NewSnake()

screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
# screen.onkey(fun=replay, key='p')

food = Food()
scoreboard = Scoreboard()

def game():
  global gaming
  while gaming:
    # update the screen every (snake.speed) seconds
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    # If snake eats food
    if snake.head.distance(food) < 10:
      food.generate()
      snake.grow()
      scoreboard.score_up()

    # If snake has a collision
    if snake.check_collision():
      gaming = False
      scoreboard.game_over()

game()


















screen.exitonclick()