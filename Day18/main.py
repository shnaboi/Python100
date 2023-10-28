from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('classic')
tim.color('green')
tim.pensize(1)

colors = ["blue", "red", "green", "wheat", "SlateGrey", "SeaGreen", "black", "purple", "DarkOrchid", "orange"]

# CREATE SHAPES ALL WITH DIFFERENT COLORS

# for shape in range(3, 11):
#   sides = 360 / shape
#   tim.color(random.choice(colors))
#   for _ in range(1, shape + 1):
#     for num in range(1, 10):
#       if tim.isdown():
#         tim.pu()
#         tim.forward(10)
#       else:
#         tim.pd()
#         tim.forward(10)
#
#     tim.right(sides)

# CREATE RANDOM WALK WITH RANDOM COLRS
# degrees = [0, 90, 180, 270]
# tim.speed(0)
# for num in range(1, 250):
#   tim.right(random.choice(degrees))
#   tim.color(random.choice(colors))
#   tim.forward(25)

def draw_spirograph(size):
  for num in range(int(360 / size)):
    tim.color(random.choice(colors))
    tim.speed(0)
    tim.circle(100)
    tim.setheading(tim.heading() + size)

draw_spirograph(3)



screen = Screen()
screen.exitonclick()
