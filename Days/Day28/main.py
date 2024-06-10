import math
from tkinter import *
import datetime
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_click():
    window.after_cancel(timer)
    title_label.config(text="POMODORA TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_click():
    marks = ""
    global reps

    if reps % 2 == 0 and reps != 8:
        title_label.config(text="WORKING TIME", fg=GREEN)
        count_down(WORK_MIN*60)
        reps += 1
    elif reps == 8:
        title_label.config(text="LONG BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="CONGRATULATIONS", fg=RED)
    else:
        title_label.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1

    for i in range(0, math.floor(reps/2)):
        marks += "✔️"
    tick_label.config(text=marks)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    mins = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = "0" + str(seconds)
    if mins < 10:
        mins = "0" + str(mins)
    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")
    # canvas.itemconfig(timer_text, text=str(datetime.timedelta(seconds=count)))
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        start_click()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


title_label = Label(text="POMODORA TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 70))
title_label.grid(row=0, column=1)

start_button = Button(text="START", highlightthickness=0, command=start_click)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", highlightthickness=0, command=reset_click)
reset_button.grid(row=2, column=2)

tick_label = Label(text="", bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=1)


window.mainloop()