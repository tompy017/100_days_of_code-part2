"""POMODORO APP.
Project for Angela Wu's 100 days of code challenges.
"""
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TIMER_FONT = ("Courier", 35, "bold")
LABEL_FONT = ("Courier", 25, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "\u2705"
BUTTON_FONT = ("System", 10, "bold")

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO APP")
window.config(padx=100, pady=50, background="black")

# Title
Label(
    text="Timer",
    background="black",
    foreground=GREEN,
    font=LABEL_FONT,
).grid(column=1, row=0, pady=10)

# Image
tomato_img = PhotoImage(file="./img/tomato.png")        # PATH to image
# Canvas to place image
canvas = Canvas(
    width=201,                  # Picture width
    height=224,                 # Picture height
    highlightthickness=0,       # No border
    background="black",
)
canvas.create_image(101, 112, image=tomato_img)    # Image x and y coordinates on canvas
# Timer
canvas.create_text(101, 130, text="texto", fill="white", font=TIMER_FONT)
canvas.grid(column=1, row=1)


# Buttons
start_btn = Button(
    window, text="Start",
    command="",
    highlightthickness=0,
    font=BUTTON_FONT,
    background=GREEN)

reset_btn = Button(
    window, text="Reset",
    command="",
    highlightthickness=0,
    font=BUTTON_FONT,
    background="brown1")

start_btn.grid(column=0, row=3)
reset_btn.grid(column=2, row=3)

# Checkmarks
checked = Label(text=CHECK_MARK, background="black", foreground=GREEN, font=LABEL_FONT)
checked.grid(column=1, row=2, pady=50)


window.mainloop()
