from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    with open("data.txt") as data:
      self.highscore = int(data.read())
    self.pu()
    self.text = f"Score: {self.score}"
    self.color('gainsboro')
    self.update_scoreboard()
    self.hideturtle()

  def update_scoreboard(self):
    self.clear()
    self.setpos(0, 275)
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    self.setpos(0, -275)
    self.write(f"High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

  def score_up(self):
    self.score += 1
    self.update_scoreboard()

  def game_over(self):
    if self.highscore < self.score:
      self.highscore = self.score
      with open("data.txt", mode='w') as data:
        data.write(f"{self.highscore}")
    self.update_scoreboard()
    self.setpos(0, 0)
    self.color('gainsboro')
    self.write("GAME OVER", align=ALIGNMENT, font=('Courier', 15, 'normal'))
    # self.setpos(0, -25)
    # self.write("Press 'p' to play again", align=ALIGNMENT, font=('Courier', 15, 'normal'))