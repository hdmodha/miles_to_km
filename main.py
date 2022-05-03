from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry


def calculate():
    miles = miles_entry.get()
    kms = float(miles) * 1.609
    ans_label["text"] = round(kms, 2)

# Initializing window screen
window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=300, height=250)
window.config(padx=25, pady=25)

# Entry for getting input as miles
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

#Labels
just_text = Label(text="is equal to")
just_text.grid(column=0, row=1)


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

ans_label = Label(text="")
ans_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calc_button = Button(text="Calculate", font=("Calibri", 10, "normal"), command=calculate)
calc_button.grid(column=1, row=2)

window.mainloop()
