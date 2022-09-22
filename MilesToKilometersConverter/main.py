"""Miles to Kilometers Converter.
Project for Angela Wu's 100 days of code challenges.
"""
from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(
    padx=20,
    pady=20,
    background="white",
)


# Entry (inputs)
entry = Entry()
entry.config(width=10)
entry.focus()
entry.grid(column=1, row=0)


# Labels
mile_label = Label()
mile_label.config(text="Miles", background="white")
mile_label.grid(column=2, row=0)

equal_label = Label()
equal_label.config(text="is equal to:", background="white")
equal_label.grid(column=0, row=1)

km_label = Label()
km_label.config(text="Kms", background="white")
km_label.grid(column=2, row=1)

result_label = Label()
result_label.config(
    width=10,
    fg="red",
    background="white",
    borderwidth=5,
    relief="flat",
)
result_label.grid(column=1, row=1)


# Button
def button_clicked():
    km = float(entry.get()) * 1.60934
    result_label.config(text=km)


button = Button()
button.config(
    text="Calculate",
    background="lightblue",
    command=button_clicked,
)
button.grid(column=1, row=2, pady=10)


window.mainloop()
