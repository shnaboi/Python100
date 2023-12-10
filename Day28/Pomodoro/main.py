from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .2
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = .2
reset = False
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
  global reset
  reset = True


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
  global reps
  reps += 1

  work_sec = int(WORK_MIN * 60)
  short_break_sec = int(SHORT_BREAK_MIN * 60)
  long_break_sec = int(LONG_BREAK_MIN * 60)
  # Take break if on specified rep (1w, 2r, 3w, 4r, 5w, 6r, 7w, 8lr)
  if reps % 8 == 0:
    countdown(long_break_sec)
  elif reps % 2 == 0:
    countdown(short_break_sec)
  else:
    countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time_left_sec):
  # Get the format of time to be 00:00
  min = math.floor(time_left_sec / 60)
  sec = (time_left_sec % 60)
  if sec < 10:
    canvas.itemconfig(timer_text, text=f"{min}:0{sec}")
  else:
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
  if time_left_sec > 0:
    window.after(1000, countdown, time_left_sec - 1)
  else:
    start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Productive Timer")
window.minsize(350, 400)
window.config(padx=27, pady=15, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_butt = Button(text="Start", width=5, height=2)
start_butt.config(command=start_timer)
start_butt.grid(row=3, column=0)

reset_butt = Button(text="Reset", width=5, height=2)
reset_butt.config(command=reset_timer)
reset_butt.grid(row=3, column=2)

checkmarks = Label(text="🗹", font=(FONT_NAME, 25, "normal"), bg=YELLOW)
checkmarks.grid(row=4, column=1)

window.mainloop()

# for hanging
# 20 on and 5 off (2min of 40sec rests(3x) and 3min between sets)
