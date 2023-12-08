from tkinter import *

window = Tk()
window.title("Converter Program")
window.minsize(width=250, height=250)
window.config(padx=15, pady=15)

def calculate():
  miles = int(input_mi.get())
  km = miles * 1.609334
  input_km.config(text=f"{km}")

input_mi = Entry(width=15)
input_mi.grid(row=0, column=1)
label_mi = Label(text="Miles")
label_mi.grid(row=0, column=2)

input_km = Label(width=15)
input_km.grid(row=1, column=1)
label_km = Label(text="Kilometers")
label_km.grid(row=1, column=2)

is_equal_to = Label(text="is equal to:")
is_equal_to.grid(row=1, column=0)
calc_butt = Button(text="Calculate", command=calculate)
calc_butt.grid(row=2, column=1)

window.mainloop()