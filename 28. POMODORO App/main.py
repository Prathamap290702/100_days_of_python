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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg = PINK)



text = "✔"

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg = PINK, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = Label(text = text, bg=PINK, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

bg_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=202,height=224, bg = PINK, highlightthickness=0)
canvas.create_image(102,112,image = bg_img)
canvas.create_text(103,130, text=str(min) + ":" + str(sec),fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()