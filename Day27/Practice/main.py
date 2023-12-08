# 252 & 253 for Tkinter window and widgets
from tkinter import *

window = Tk()
window.title("My 1st GUI Program")
window.minsize(width=250, height=250)

# Label

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
# Use the two lines below to configure / change a label's text
# my_label["text"] = "Foo"
# my_label.config(text="Bar")

def button_clicked():
  my_label.config(text=f"{input.get()}")
#   ^^^ Func changes the text (label) above the button to change the txt typed into the Entry (input)

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)
# the command arg needs to be set to a function that is called when button is clicked

button2 = Button(text="butt2")
button2.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=2, column=4)

window.mainloop()
# ^^^ This keeps the tkinter window from closing when script is run. It stays at the end of the code

# 249, 250, and 251 are all about default args, *args, and *kwargs

total = 0
def add(*args):
  total = 0
  for n in args:
    total += n
  print(total)

add(7, 2, 5, 8, 2)

# The * in *args puts all of the arguments into a tuple which can be used in the function

def calculate(n, **kwargs):
  # for key, value in kwargs.items():
  #   print(key)
  #   print(value)
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)

calculate(2, add=3, multiply=5)
# **kwargs is a dictionary, where add is a key, and 3 is the value, same with multiply:3
# in the calculate function, you must pass a value for n, and if you want to do any calculations you have to pass +/*

class Car:

  def __init__(self, **kw):
    self.make = kw.get("make")
    self.model = kw.get("model")

# using kw.get() means you can initialize a Car object and it won't be necessary to pass a make or a model attribute
# remember that when defining functions:
# ^^^ you can give default values for arguments, and those arguments don't need to be typed when calling the function
