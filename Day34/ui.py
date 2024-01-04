from tkinter import *
THEME_COLOR = "#375362"

class QuizUI:
  def __init__(self):
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
      text="This is what the hubbub is all about",
      fill=THEME_COLOR,
      font=("Arial", 18, "italic"))
    self.canvas.grid(row=1, column=0, columnspan=2, pady = 20)

    # Buttons
    y_img = PhotoImage(file="./images/true.png")
    n_img = PhotoImage(file="./images/false.png")
    self.button_y = Button(image=y_img, highlightthickness=0)
    self.button_y.grid(row=2, column=0)
    self.button_n = Button(image=n_img, highlightthickness=0)
    self.button_n.grid(row=2, column=1)

    self.window.mainloop()

poo = QuizUI()