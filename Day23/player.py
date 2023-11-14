from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

  def __init__(self):
    self.level = 1
    self.list = []
    self.make_turtle()
    self.t = self.list[0]

  def make_turtle(self):
    t = Turtle()
    t.clear()
    t.pu()
    t.color('black')
    t.shape('turtle')
    t.setpos(STARTING_POSITION)
    t.seth(0)
    self.list.append(t)

  def up(self):
    self.t.fd(MOVE_DISTANCE)

  def down(self):
    self.t.bk(MOVE_DISTANCE)

  def check_finish(self):
    if self.t.ycor() >= FINISH_LINE_Y:
      self.t.sety(-275)
      self.level += 1
