from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class NewSnake:
  def __init__(self):
    self.snake_segs = []
    self.create_snake()
    self.head = self.snake_segs[0]
    self.neck = self.snake_segs[1]
    self.speed = .15

  def create_snake(self):
    for pos in STARTING_POSITIONS:
      t = Turtle('square')
      t.pu()
      t.color('white')
      t.setpos(pos)
      self.snake_segs.append(t)

  def move(self):
    for seg in range(len(self.snake_segs) - 1, 0, -1):
      # range numbers are (start, stop, step)
      move_to = self.snake_segs[seg - 1].pos()
      self.snake_segs[seg].goto(move_to)
    self.snake_segs[0].forward(MOVE_DIST)
    self.neck.setheading(self.head.heading())

  def right(self):
    if self.head.heading() != self.neck.heading():
      pass
    else:
      self.head.right(90)

  def left(self):
    if self.head.heading() != self.neck.heading():
      pass
    else:
      self.head.left(90)

  def grow(self):
    t = Turtle('square')
    t.pu()
    t.color('white')
    grow_pos = self.snake_segs[len(self.snake_segs) - 1].pos()
    t.setpos(grow_pos)
    self.snake_segs.append(t)
    # if score % 2 == 0: THEN change speed
    if self.speed > .069:
      self.speed -= .005