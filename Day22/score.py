from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

class Score(Turtle):

  def __init__(self):
    super().__init__()
    self.user_score = 0
    self.bot_score = 0
    self.mode_text = None
    self.hideturtle()
    self.pu()
    self.color('white')

  def update_scoreboard(self):
    self.text = f"{self.user_score}  |  {self.bot_score}"
    self.clear()
    self.setpos(0, 300)
    self.write(self.text, align=ALIGNMENT, font=FONT)
    self.setpos(0, 350)
    self.write(self.mode_text, align=ALIGNMENT, font=('Courier', 10, 'normal'))

  def check_level(self, level):
    if level == "1":
      self.mode_text = "Easy mode. \nFirst to score 7 points, win by 2"
      self.mode = "easy"
      self.update_scoreboard()
    elif level == "2":
      self.mode_text = "Medium mode. \nFirst to score 11 points, win by 2"
      self.mode = "med"
      self.update_scoreboard()
    elif level == "3":
      self.mode_text = "Hard mode. \nFirst to score 21 points, win by 2"
      self.mode = "hard"
      self.update_scoreboard()
    elif level == "4":
      self.mode_text = "Hardcore mode. \nFirst to be ahead by 15 points wins"
      self.mode = "core"
      self.update_scoreboard()

  def check_win(self, gaming):
    if self.mode == "easy":
      if self.user_score >= 7:
        if self.bot_score <= (self.user_score - 2):
          print("User wins!")
          gaming = False
        else:
          pass
      elif self.bot_score >= 7:
        if self.user_score <= (self.bot_score - 2):
          print("Bot wins! You lose!")
          gaming = False
        else:
          pass
    elif self.mode == "med":
      if self.user_score >= 11:
        if self.bot_score <= (self.user_score - 2):
          print("User wins!")
          gaming = False
        else:
          pass
      elif self.bot_score >= 11:
        if self.user_score <= (self.bot_score - 2):
          print("Bot wins! You lose!")
          gaming = False
        else:
          pass
    elif self.mode == "hard":
      if self.user_score >= 21:
        if self.bot_score <= (self.user_score - 2):
          print("User wins!")
          gaming = False
        else:
          pass
      elif self.bot_score >= 21:
        if self.user_score <= (self.bot_score - 2):
          print("Bot wins! You lose!")
          gaming = False
        else:
          pass
    elif self.mode == "core":
      if self.user_score >= 15:
        if self.bot_score <= (self.user_score - 15):
          print("User wins!")
          gaming = False
        else:
          pass
      elif self.bot_score >= 15:
        if self.user_score <= (self.bot_score - 15):
          print("Bot wins! You lose!")
          gaming = False
        else:
          pass


