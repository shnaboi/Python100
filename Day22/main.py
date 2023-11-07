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
ball_y = ball.y

screen.onkeypress(fun=paddle.up, key='Left')
screen.onkeypress(fun=paddle.down, key='Right')

gaming = True
while gaming:
  screen.update()
  time.sleep(.01)

  # Update bot's pos based on ball's pos
  ball_y = ball.y
  ball.move_ball(left_paddle, bot)
  paddle.movebot(ball_y, score.user_score)

  # Check if ball was scored
  if ball.score_toggle == True:
    if ball.user_score == True:
      score.user_score += 1
      score.update_scoreboard()
      paddle.bot_speed += .2
      ball.reset_ball(score.user_score)
    else:
      score.bot_score += 1
      score.update_scoreboard()
      ball.reset_ball(score.user_score)
  ball.score_toggle = False

# TODO Add minor ball angle change to bot

screen.exitonclick()
