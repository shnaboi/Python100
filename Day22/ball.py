from turtle import Turtle
import turtle

turtle.mode('logo')
import random

class Ball:

  def __init__(self):
    self.y = 1
    self.list = []
    self.user_score = False
    self.p_angle = 0
    self.speed = 2.5
    self.create_ball()
    self.ball = self.list[0]
    self.score_toggle = None

  def create_ball(self):
    b = Turtle('circle')
    b.clear()
    b.pu()
    b.shapesize(stretch_wid=.5, stretch_len=.5)
    b.color('white')
    b.setpos(0, 0)
    b.seth(270)
    self.list.append(b)

  def reset_ball(self, user_score):
    self.speed = 2.5 + (user_score * .2)
    bot_head = random.randint(80, 100)
    user_head = random.randint(260, 280)
    if self.user_score:
      self.ball.setpos(100, 0)
      self.ball.seth(user_head)
    else:
      self.ball.setpos(0, 0)
      self.ball.seth(bot_head)
    print(f"Ball speed = {self.speed}")

  def move_ball(self, l, r):
    self.ball.forward(self.speed)
    self.check_collide(l, r)
    self.y = self.ball.ycor()

  def change_p_angle(self, l_paddle):
    cur_angle = self.ball.heading()
    if self.ball.ycor() > l_paddle.ycor():
      a = cur_angle - 180
      b = a - 90
      c = 90 - b
      # c == new angle without dist from center effecting angle
      d = self.ball.distance(l_paddle) * (.69)
      e = c - d
      if e < 10:
        e = 11
      # e == new angle after effect by dist from center
      self.ball.seth(e)
      print(f"User spin = {e - c}")
    else:
      a = cur_angle - 180
      b = a - 90
      c = 90 - b
      # c == new angle without dist from center effecting angle
      d = self.ball.distance(l_paddle) * (.69)
      e = c + d
      if e > 170:
        e = 169
      self.ball.seth(e)
      print(f"User spin = {e - c}")

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

    # if user hits ball
    if self.ball.distance(l_paddle) < 48 and -580 < self.ball.xcor() < -570:
      self.change_p_angle(l_paddle)
      self.speed += .2
      # move ball's xcor so it doesn't get stuck in paddle and then sling shot
      self.ball.setx(self.ball.xcor() + 10)

    # if bot hits ball
    if self.ball.distance(r_paddle) < 48 and 570 < self.ball.xcor() < 580:
      a = self.ball.heading()
      b = 360 + a
      c = b - (a * 2)
      # if bot slices
      if r_paddle.ycor() < self.ball.ycor() and self.ball.heading() > 90 and r_paddle.distance(self.ball) > 10:
        slice = r_paddle.distance(self.ball) * (.69)
        bot_slice = c - slice
        self.ball.seth(bot_slice)
        self.ball.setx(self.ball.xcor() - 10)
        self.speed += (r_paddle.distance(self.ball) * .05)
        print(f"Bot SLICE! Spin = {slice}")
      elif r_paddle.ycor() > self.ball.ycor() and self.ball.heading() < 90 and r_paddle.distance(self.ball) > 10:
        slice = r_paddle.distance(self.ball) * (.69)
        bot_slice = c + slice
        self.ball.seth(bot_slice)
        self.ball.setx(self.ball.xcor() - 10)
        self.speed += (r_paddle.distance(self.ball) * .05)
        print(f"Bot SLICE! Spin = {slice}")
      else:
        self.ball.seth(c)
        self.speed += .2
        self.ball.setx(self.ball.xcor() - 2.5)

    # if ball hits edge of screen (score)
    if self.ball.xcor() < -599:
      self.user_score = False
      self.score_toggle = True
    elif self.ball.xcor() > 599:
      self.user_score = True
      self.score_toggle = True

    # have change heading func to determine bounce angle
