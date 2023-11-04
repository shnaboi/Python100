from turtle import Turtle
import turtle
turtle.mode('logo')

class Ball:

  def __init__(self):
    self.y = 1
    self.list = []
    self.user_score = False
    self.heading = 290
    self.speed = 2
    self.create_ball()
    self.ball = self.list[0]
    self.score_toggle = None
    # self.move_ball()

  def create_ball(self):
    b = Turtle('circle')
    b.clear()
    b.pu()
    b.shapesize(stretch_wid=.5, stretch_len=.5)
    b.color('white')
    b.setpos(0, 0)
    b.seth(self.heading)
    self.list.append(b)

  def reset_ball(self):
    self.ball.setpos(0, 0)
    self.speed = 2.5
    if self.user_score == True:
      self.ball.seth(270)
    else:
      self.ball.seth(90)

  def move_ball(self, l, r):
    self.ball.forward(self.speed)
    self.check_collide(l, r)
    self.y = self.ball.ycor()

  def check_collide(self, l_paddle, r_paddle):

    # if ball hits north wall
    if self.ball.ycor() > 399:
      if self.ball.heading() < 180:
        angle = 180 - self.ball.heading()
        self.ball.seth(angle)
      else:
        angle = self.ball.heading() - 270
        new_head = 270 - angle
        self.ball.seth(new_head)

    # if ball hits south wall
    elif self.ball.ycor() < -399:
      if self.ball.heading() < 180:
        angle = self.ball.heading() - 90
        new_head = 90 - angle
        self.ball.seth(new_head)
      else:
        angle = self.ball.heading() - 180
        new_head = 360 - angle
        self.ball.seth(new_head)

    # if ball hits paddle
    if self.ball.distance(l_paddle) < 48 and -580 < self.ball.xcor() < -570:
      self.ball.seth(self.ball.heading() - 180)
      self.speed += .2
      print(self.ball.distance(l_paddle))
      # move ball's xcor so it doesn't get stuck in paddle and then sling shot
      self.ball.setx(self.ball.xcor() + 5)

    if self.ball.distance(r_paddle) < 50 and 570 < self.ball.xcor() < 580:
      self.ball.seth(self.ball.heading() + 180)
      self.speed += .2

    # if ball hits edge of screen (score)
    if self.ball.xcor() < -599:
      self.user_score = False
      self.score_toggle = True
      self.reset_ball()
    elif self.ball.xcor() > 599:
      self.user_score = True
      self.score_toggle = True
      self.reset_ball()






    # have change heading func to determine bounce angle
