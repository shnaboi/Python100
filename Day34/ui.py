from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUI:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    self.window = Tk()
    self.window.title("QuizFella")
    self.window.config(bg=THEME_COLOR, padx=20, pady=20)
    self.window.minsize(width=340, height=500)

    # SCORE
    self.score = Label(text=f"Score: 0", bg="#375362", fg="white")
    self.score.grid(row=0, column=1)

    # Question Window
    self.canvas = Canvas(width=300, height=300, bg="white")
    self.question_text = self.canvas.create_text(
      150,
      150,
      text=f"{self.quiz.next_question()}",
      fill=THEME_COLOR,
      font=("Arial", 18, "italic"),
      width=280)
    self.canvas.grid(row=1, column=0, columnspan=2, pady = 20)

    # Buttons
    y_img = PhotoImage(file="./images/true.png")
    self.button_y = Button(image=y_img, highlightthickness=0, command=self.true)
    self.button_y.grid(row=2, column=0)

    n_img = PhotoImage(file="./images/false.png")
    self.button_n = Button(image=n_img, highlightthickness=0, command=self.false)
    self.button_n.grid(row=2, column=1)

    self.window.mainloop()

  def true(self):
    score_int, ans = self.quiz.check_answer('True')
    self.score.config(text=f"Score: {score_int}")
    self.ui_feedback(ans)

  def false(self):
    score_int, ans = self.quiz.check_answer('False')
    self.score.config(text=f"Score: {score_int}")
    self.ui_feedback(ans)

  def ui_feedback(self, bool):
    if bool == True:
      self.canvas.config(bg="green")
      self.canvas.itemconfig(self.question_text, fill="white")
    else:
      self.canvas.config(bg="red")
    self.window.after(1250, self.ui_next_q)
    self.canvas.itemconfig(self.question_text, fill="white")

  def ui_next_q(self):
    try:
      self.canvas.itemconfig(self.question_text, text=f"{self.quiz.next_question()}")
      self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
      self.canvas.config(bg="white")
    except IndexError:
      self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
      self.canvas.config(bg="white")
      self.canvas.itemconfig(self.question_text, text=f"Great job on the quiz!\nFinal Score: {self.quiz.score}")
      self.button_n.config(state=DISABLED)
      self.button_y.config(state=DISABLED)
