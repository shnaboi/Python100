from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.pu()
    self.text = f"Score: {self.score}"
    self.color('white')
    self.setpos(0, 275)
    self.update_scoreboard()
    self.hideturtle()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
  def score_up(self):
    self.score += 1
    self.update_scoreboard()

  def game_over(self):
    self.setpos(0, 0)
    self.color('azure')
    self.write("GAME OVER", align=ALIGNMENT, font=('Courier', 15, 'normal'))