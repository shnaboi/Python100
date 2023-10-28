import turtle

import colorgram
from turtle import Turtle, Screen
import random
turtle.colormode(255)

colors = colorgram.extract('colors1.jpg', 23)
rgb_colors = []

for color in colors:
  rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
  rgb_colors.append(rgb)

print(rgb_colors)

# SPIROGAPH TESTING

# tim = Turtle()
# tim.pensize(2)
#
# def draw_spirograph(size):
#   for num in range(int(360 / size)):
#     tim.color(random.choice(rgb_colors))
#     tim.speed(0)
#     tim.circle(150)
#     tim.setheading(tim.heading() + size)
#
# draw_spirograph(3)
#
# screen = Screen()
# screen.exitonclick()

# MAIN PROJECT (DOT PAINTING)

t = Turtle()

def draw_hirst(size):
  t.pu()
  t.hideturtle()
  canvas = int(size * size)
  dots = 0
  # t.dot(15, 'black')
  x = int((size * -37) / 2)
  y = int((size * -37) / 2)
  while dots != canvas:
    y += 37
    t.setpos(x, y)
    t.dot(15, random.choice(rgb_colors))
    dots += 1
    t.forward(37)
    for _ in range(1, size):
      t.dot(15, random.choice(rgb_colors))
      dots += 1
      t.forward(37)


draw_hirst(13)

screen = Screen()
screen.exitonclick()