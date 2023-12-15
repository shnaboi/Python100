from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pw():
  website = website_input.get()
  email= email_input.get()
  password = pw_input.get()

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
pw_button = Button(text="Generate Password", bd=1)
pw_button.grid(row=3, column=2, sticky=E+W)

add_button = Button(text="Add Password to Bank", bd=1, command=save_pw)
add_button.grid(row=4, column=1, columnspan=2, sticky=E+W)

window.mainloop()