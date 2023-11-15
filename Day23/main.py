import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle.mode('logo')
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.up, key='Up')
screen.onkeypress(fun=player.down, key='Down')

game_is_on = True
while game_is_on:
  cars.move_cars(player.t)
  cars.new_car()
  player.check_finish()
  cars.check_level(player.level)
  scoreboard.update_board(player.level)
  time.sleep(0.1)
  screen.update()
  if cars.game_toggle == True:
    scoreboard.game_over()
    game_is_on = False

screen.exitonclick()