from tkinter import *

from data import get_languages, get_word


BG_COLOR="#B1DDC6"
IMG_WIDTH=800
IMG_HEIGHT=526

languages = get_languages()
ORIGIN_LANGUAGE=languages[0]
TRANSLATION_LANGUAGE=languages[1]

# ---------------------- BUTTON ACTIONS ----------------------
def set_card(language, word):
    canvas.itemconfig(text_language, text=language)
    canvas.itemconfig(text_word, text=word)
    

def next_card():
    new_word = get_word()
    set_card(ORIGIN_LANGUAGE, new_word[0][languages[0]])


# ---------------------------- UI ----------------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, highlightthickness=0, bg=BG_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(IMG_WIDTH/2, IMG_HEIGHT/2, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

text_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
text_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

img_wrong = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, bd=0, command=next_card)
btn_wrong.grid(row=1, column=0)

img_right = PhotoImage(file="./images/right.png")
btn_rigth = Button(image=img_right, highlightthickness=0, bd=0, command=next_card)
btn_rigth.grid(row=1, column=1)

next_card()

window.mainloop()