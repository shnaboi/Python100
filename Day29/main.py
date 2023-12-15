from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

def generate_pw():
  pw_letters = [random.choice(letters) for _ in range(random.randint(1,3), random.randint(11, 13))]
  pw_numbers = [random.choice(numbers) for _ in range(random.randint(1,3), random.randint(9, 11))]
  pw_symbols = [random.choice(symbols) for _ in range(random.randint(1,3), random.randint(7, 9))]

  pw_char = pw_letters + pw_numbers + pw_symbols
  random.shuffle(pw_char)
  password = ''.join(pw_char)
  pw_input.delete(0, 99)
  pw_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pw():
  website = website_input.get()
  email= email_input.get()
  password = pw_input.get()

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Password Manager", message="Invalid website/password")

  else:
    user_ok = messagebox.askokcancel(title="Password Manager", message=f"Details entered:\n"
                                                             f"{website}\n{email}\n{password}\n"
                                                             f"If this is correct, click 'OK' to save.")
    if user_ok:
      with open("data.txt", mode="a") as file:
        file.write(f"{website} || {email} || {password}\n")
      website_input.delete(0, END)
      pw_input.delete(0, END)
      messagebox.showinfo(title="Password Manager", message=f"{website} password saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=465, height=375)
window.config(pady=30, padx=30)
window.rowconfigure(4, pad=7)
window.rowconfigure(3, pad=2)
window.rowconfigure(2, pad=2)
window.rowconfigure(1, pad=2)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2, sticky=W)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2, sticky=W)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)
pw_input = Entry(width=33)
pw_input.grid(row=3, column=1, sticky=W)
pw_button = Button(text="Generate Password", bd=1, command=generate_pw)
pw_button.grid(row=3, column=2, sticky=E+W)

add_button = Button(text="Add Password to Bank", bd=1, command=save_pw)
add_button.grid(row=4, column=1, columnspan=2, sticky=E+W)

window.mainloop()