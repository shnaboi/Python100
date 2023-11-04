from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

class Score(Turtle):

  def __init__(self):
    super().__init__()
    self.user_score = 0
    self.bot_score = 0
    self.hideturtle()
    self.pu()
    self.color('white')
    self.update_scoreboard()

  def update_scoreboard(self):
    self.text = f"{self.user_score}  |  {self.bot_score}"
    self.clear()
    self.setpos(0, 300)
    self.write(self.text, align=ALIGNMENT, font=FONT)