from turtle import Turtle
import random



class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.pu()
    self.shapesize(.5, .5)
    self.color('white')
    self.speed(0)
    self.generate()

  def generate(self):
    x = (random.randint(-14, 14) * 20)
    y = (random.randint(-14, 14) * 20)
    self.goto(x, y)