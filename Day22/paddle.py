from turtle import Turtle

START_POSITIONS = [(-575, 0), (575, 0)]

class Paddle:

  def __init__(self):
    self.paddles = []
    self.user = self.new_paddle(START_POSITIONS[0])
    self.bot = self.new_paddle(START_POSITIONS[1])
    self.speed = .01

  def new_paddle(self, pos):
    p = Turtle("square")
    p.pu()
    p.color('white')
    p.setpos(pos)
    p.shapesize(stretch_wid=.75, stretch_len=5)
    p.setheading(180)
    # self.test = p.getcanvas()
    self.paddles.append(p)

  def movebot(self):
    self.paddles[1].setheading(90)
    self.paddles[1].forward(7)

  def up(self):
    self.paddles[0].setheading(0)
    self.paddles[0].forward(10)


  def down(self):
    self.paddles[0].setheading(180)
    self.paddles[0].forward(10)

  # def move(self):
