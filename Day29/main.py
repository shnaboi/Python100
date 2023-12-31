import json
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
# --------------------------- SEARCH PASSWORD ------------------------------ #
def search_pw():
  website = website_input.get().lower()
  try:
    with open("data.json", mode="r") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showinfo(title="Password Manager",
                        message="No data file found. Start by saving a password.")
  else:
    for entry in data:
      saved_website = entry.lower()
      if website == saved_website:
        # print(data.entry)
        messagebox.showinfo(title="Password Manager",
                            message=f"{entry}:\n"
                                    f"Email/Username: {data[entry]['email']}\n"
                                    f"Password: {data[entry]['password']}")
        break
      messagebox.showinfo(title="Password Manager",
                          message=f"No data found for {website}.\n"
                                  f"Make sure your website search is spelled correctly before trying again.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pw():
  website = website_input.get()
  email= email_input.get()
  password = pw_input.get()

  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Password Manager",
                        message="Invalid website/password")

  else:
    user_ok = messagebox.askokcancel(title="Password Manager",
                                     message=f"Details entered:\n"
                                             f"{website}\n{email}\n{password}\n"
                                             f"If this is correct, click 'OK' to save.")
    if user_ok:
      try:
        with open("data.json", mode="r") as file:
          # Read old data
          data = json.load(file)
      except FileNotFoundError:
        with open("data.json", mode="w") as file:
          #   Save updated data
          json.dump(new_data, file, indent=2)
      except json.decoder.JSONDecodeError:
        with open("data.json", mode="w") as file:
          #   Save updated data
          json.dump(new_data, file, indent=2)
      else:
        # Update old data with new data
        data.update(new_data)
        with open("data.json", mode="w") as file:
        #   Save updated data
          json.dump(data, file, indent=2)
      finally:
        website_input.delete(0, END)
        pw_input.delete(0, END)
        messagebox.showinfo(title="Password Manager",
                            message=f"{website} password saved successfully!")

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
website_input = Entry(width=33)
website_input.grid(row=1, column=1, columnspan=2, sticky=W)
website_search = Button(text="Search", bd=1, command=search_pw)
website_search.grid(row=1, column=2, sticky=E+W)

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