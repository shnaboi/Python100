from turtle import Turtle
FONT = ("Courier", 12, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.scoreboard_lvl = 1
    self.update_board(self.scoreboard_lvl)

  def update_board(self, level):
    if level != self.scoreboard_lvl:
      self.clear()
      self.hideturtle()
      self.pu()
      self.color('black')
      self.setpos(0, 270)
      self.write(f"LEVEL: {level}", align=ALIGNMENT, font=FONT)
    else:
      self.clear()
      self.hideturtle()
      self.pu()
      self.color('black')
      self.setpos(0, 270)
      self.write(f"LEVEL: {level}", align=ALIGNMENT, font=FONT)
