import time
import pandas
from tkinter import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
french_dict = {}
#---------------Data-----------------#
try:
    french_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    french_dict = original_data.to_dict(orient="records")
else:
    french_dict = french_data.to_dict(orient="records")


#---------------Functions-----------------#
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg_img, image=card_front_img)
    current_card = choice(french_dict)
    canvas.itemconfig(lang_text, text = "French", fill = "black")
    canvas.itemconfig(question_text, text = current_card["French"], fill = "black")
    flip_timer = canvas.after(3000,flip_card)


def flip_card():
    canvas.itemconfig(bg_img, image = card_back_img)
    canvas.itemconfig(lang_text, text="English", fill = "white")
    canvas.itemconfig(question_text, text=current_card["English"], fill ="white")

def is_known():
    french_dict.remove(current_card)
    next_card()
    data = pandas.DataFrame(french_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)


#---------------UI-----------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Canvas
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
known_img = PhotoImage(file="images/right.png")
unknown_img = PhotoImage(file="images/wrong.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = canvas.create_image(400, 263, image=card_front_img)

#text
lang_text = canvas.create_text(400,150, text="", font=("Ariel",40,"italic"))
question_text = canvas.create_text(400,263,text ="", font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)


#button
known_button = Button(image=known_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

unknown_button = Button(image=unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)


next_card()

window.mainloop()