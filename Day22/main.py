from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)
screen.listen()

score = Score()
paddle = Paddle()
ball = Ball()

left_paddle = paddle.paddles[0]
bot = paddle.paddles[1]

screen.onkeypress(fun=paddle.up, key='Left')
screen.onkeypress(fun=paddle.down, key='Right')

gaming = True
while gaming:
  screen.update()
  time.sleep(.01)
  ball.move_ball(left_paddle, bot)
  # Create ball

  # Test movement with bot
  # paddle.movebot()

screen.exitonclick()
