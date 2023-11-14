import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7
MOVE_DIST = 5


class CarManager:

  def __init__(self):
    self.level = 1
    self.move_dist = STARTING_MOVE_DISTANCE
    self.gen_car_frame = 6
    self.frame = 0
    self.game_toggle = None
    self.car_list = []
    self.new_car()
    self.generate_cars()

  def check_level(self, level):
    if level > self.level:
      self.move_dist += MOVE_INCREMENT
      self.level += 1
      self.gen_car_frame -= 1
  def generate_cars(self):
    for num in range(1, 10):
      car = Turtle()
      car.pu()
      car.shape('square')
      car.shapesize(stretch_wid=1, stretch_len=2)
      car.color(random.choice(COLORS))
      car.seth(270)
      car.setpos(x=random.randint(0, 245), y=random.randint(-245, 245))
      self.car_list.append(car)
  def new_car(self):
    if self.frame < self.gen_car_frame:
      self.frame += 1
      return
    else:
      car = Turtle()
      car.pu()
      car.shape('square')
      car.shapesize(stretch_wid=1, stretch_len=2)
      car.color(random.choice(COLORS))
      car.seth(270)
      car.setpos(x=280, y=random.randint(-220, 220))
      self.car_list.append(car)
      self.frame = 0

  def move_cars(self, player):
    for car in self.car_list:
      self.check_collide(player, car)
      car.fd(self.move_dist)

  def check_collide(self, player, car):
    if car.distance(player) < 29:
      self.game_toggle = True