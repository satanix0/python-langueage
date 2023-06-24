from calendar import c
from cgitb import text
from itertools import tee
from pickletools import long1
import re
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = count//60
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔️"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro Clock')
window.geometry('600x400')
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 25, 'bold'))
timer_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='Projects/D28_GUI_Pomodoro/tomato.png')
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 125, text="00:00", fill="white",
                                font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)
reset_butt = Button(text="Reset", command=reset_timer)
reset_butt.grid(row=2, column=3)

check = Label(bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)


window.mainloop()
