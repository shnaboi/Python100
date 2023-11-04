from turtle import Turtle
import turtle
turtle.mode('logo')

class Ball:

  def __init__(self):
    self.list = []
    self.user_score = False
    self.heading = 315
    self.speed = 2
    self.create_ball()
    self.ball = self.list[0]
    # self.move_ball()

  def create_ball(self):
    b = Turtle('circle')
    b.clear()
    b.pu()
    b.shapesize(stretch_wid=.5, stretch_len=.5)
    b.color('white')
    b.setpos(0, 0)
    b.setheading(self.heading)
    self.speed = 2.5
    self.list.append(b)

  def reset_ball(self):
    self.ball.setpos(0, 0)
    if self.user_score == True:
      self.ball.setheading(180)
    else:
      self.ball.setheading(0)

  def move_ball(self):
    self.ball.forward(self.speed)
    self.check_collide()

  def check_collide(self):
    # if ball hits wall
    if self.ball.ycor() > 399:
      if self.ball.heading() < 180:
        angle = 180 - self.ball.heading()
        self.ball.setheading(angle)
      else:
        angle = self.ball.heading() - 270
        new_head = 270 - angle
        self.ball.setheading(new_head)
    elif self.ball.ycor() < -399:
      if self.ball.heading() < 180:
        angle = self.ball.heading() - 90
        new_head = 90 - angle
        self.ball.setheading(new_head)
      else:
        angle = self.ball.heading() - 180
        new_head = 360 - angle
        self.ball.setheading(new_head)


    # if ball hits paddle

    # self.speed += 2
    # if self.ball[0] and

    # if ball hits edge of screen (score)
    if self.ball.xcor() < -599:
      self.ball.setx(600)
      # self.user_score = False
      # self.reset_ball()
    elif self.ball.xcor() > 599:
      self.ball.setx(-600)
      # self.user_score = True
      # self.reset_ball()




    # have change heading func to determine bounce angle
