from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # to test set it to 0.1 for 6 sec cycle
SHORT_BREAK_MIN = 5 # to test set it to 0.1 for 6 sec cycle
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)

    canvas.itemconfig(current_time, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    checkmarks_text.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps in [1,3,5,7]:
        timer_text.config(text="Work", fg=GREEN)
        count_down(int(WORK_MIN*60))
    elif reps == 8:
        timer_text.config(text="Break", fg=RED)
        count_down(int(LONG_BREAK_MIN*60))
    else:
        timer_text.config(text="Break", fg=PINK)
        count_down(int(SHORT_BREAK_MIN*60))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, timer
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(current_time, text=f"{count_min:02d}:{count_sec:02d}")
    # explaining :02d f-string formatting syntax
    # 0 tells Python to pad with zeros
    # 2 sets the minimum width of the string
    # d stands for decimal integer

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = reps//2
        mark = checkmark*work_session
        checkmarks_text.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas_width = 200
canvas_height = 224
canvas = Canvas(width=canvas_width, height=canvas_height, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(canvas_width/2, canvas_height/2, image=tomato_img )
current_time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(row=1, column=1)

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_text.grid(row=0, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = "✔" #U+2714 ✔ HEAVY CHECK MARK, from https://en.wikipedia.org/wiki/Check_mark

checkmarks_text = Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks_text.grid(row=3, column=1)



window.mainloop()