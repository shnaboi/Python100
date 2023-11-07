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

level = input("Which mode would you like to play? \n1 - Easy: First to score 7, win by 2 \n2 - Medium: First to score "
              "11, win by 2 \n3 - Hard: First to score 21, win by 2 \n4 - Hardcore: First to be ahead by 15 points \n")

score.check_level(level)

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
      score.check_win()
      ball.reset_ball(score.user_score)
    else:
      score.bot_score += 1
      score.update_scoreboard()
      score.check_win()
      ball.reset_ball(score.user_score)
  ball.score_toggle = False
  if score.win_toggle == True:
    gaming = False

# Easy mode = first to 7 points, win by 2
# Medium mode = first to 11 points, win by 2
# Hard Mode = first to 21 points, win by 2
# Hardcore = first to 15, win by 15

screen.exitonclick()
