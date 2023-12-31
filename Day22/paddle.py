from turtle import Turtle

START_POSITIONS = [(-575, 0), (575, 0)]

class Paddle:

  def __init__(self):
    self.paddles = []
    self.create_paddles()
    self.user = self.paddles[0]
    self.bot = self.paddles[1]
    self.bot_speed = 1.69

  def create_paddles(self):
    for pos in START_POSITIONS:
      p = Turtle("square")
      p.pu()
      p.color('white')
      p.setpos(pos)
      p.shapesize(stretch_wid=.75, stretch_len=4.25)
      p.setheading(180)
      self.paddles.append(p)

  def movebot(self, ball_y, user_score):
    # for every point user has, increase bot_speed += .02
    if self.bot.ycor() < ball_y:
      self.bot.seth(0)
      self.bot.forward(self.bot_speed)
    if self.bot.ycor() > ball_y:
      self.bot.seth(180)
      self.bot.forward(self.bot_speed)

  def up(self):
    self.paddles[0].setheading(0)
    self.paddles[0].forward(10)
  def down(self):
    self.paddles[0].setheading(180)
    self.paddles[0].forward(10)
