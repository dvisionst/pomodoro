from tkinter import *
import math

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
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_title.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = 6
    short_break = 5
    long_break = 3
    if reps % 8 == 0:
        count_down(long_break)
        timer_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_title.config(text="Timer", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global timer
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks = ""
            work_sessions= math.floor(reps/2)
            for _ in range(work_sessions):
                checks += "✓"
            checkmark.config(text=f"{checks}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# timer label creation
timer_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "italic"))
timer_title.grid(column=1, row=0)

# start button creation
start = Button(text="Start", bg='#FFFFFF', font=(FONT_NAME, 12), command=start_timer)
start.grid(column=0, row=2)

# reset button creation
reset = Button(text="Reset", bg='#FFFFFF', font=(FONT_NAME, 12), command=reset_timer)
reset.grid(column=2, row=2)

# checkmark label creation
checkmark = Label(bg=YELLOW, fg=GREEN, font="bold")
checkmark.grid(column=1, row=3)

window.mainloop()
