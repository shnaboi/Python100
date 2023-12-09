from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


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
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_butt = Button(text="Start", width=5, height=2)
start_butt.grid(row=3, column=0)

reset_butt = Button(text="Reset", width=5, height=2)
reset_butt.grid(row=3, column=2)

checkmarks = Label(text="🗹", font=(FONT_NAME, 25, "normal"), bg=YELLOW)
checkmarks.grid(row=4, column=1)

window.mainloop()

# for hanging
# 20 on and 5 off (2min of 40sec rests(3x) and 3min between sets)