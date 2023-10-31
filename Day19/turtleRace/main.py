import turtle
from turtle import Turtle, Screen
import random

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black']

screen = Screen()
screen.setup(500, 420)

turtles = []

def draw_finish():
  finish_line = Turtle()
  finish_line.pu()
  finish_line.setpos(179, -190)
  finish_line.left(90)
  while finish_line.ycor() < 200:
    finish_line.pd()
    finish_line.forward(10)
    finish_line.pu()
    finish_line.forward(10)
  finish_line.setpos(300, 300)

def start_race():
  y = -190
  winner = False
  draw_finish()
  for color in colors:
    y += 50
    t = Turtle()
    t.pu()
    t.color('black', color)
    t.shape('turtle')
    t.shapesize(2)
    t.setpos(-220, y)
    turtles.append(t)
    print(t.color)
  bet = input("Who do you bet to win the race? Enter a color: ")
  while not winner:
    for t in turtles:
      dist = random.randint(0, 6,)
      t.forward(dist)
      if t.xcor() >= 195:
        champion = str(t.fillcolor())
        winner = True
  print(champion)




start_race()

# random.choice(colors)

screen.exitonclick()