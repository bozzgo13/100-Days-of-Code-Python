from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME ="Ariel"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


# with orient=records we get result as
# [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}, ...]
to_learn = data.to_dict(orient="records")
current_card ={}
def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    # randomly select record
    current_card = random.choice(to_learn)
    current_fr_word = current_card["French"]
    canvas.itemconfig(word_text, text=current_fr_word, fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    # save new modified list of words
    data = pandas.DataFrame(to_learn)
    # index=False Doesn't include index
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    global current_card
    current_em_word = current_card["English"]
    canvas.itemconfig(word_text, text=current_em_word, fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# after 3s
flip_timer = window.after(3000, func=flip_card)


canvas_width = 800
canvas_height = 526
canvas = Canvas(width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(canvas_width/2, canvas_height/2, image=card_front_img )


title_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_text= canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)



right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)


wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)
next_card()

window.mainloop()