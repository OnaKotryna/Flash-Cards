from tkinter import *

from data import get_languages, get_word, remove_word


BG_COLOR="#B1DDC6"
IMG_WIDTH=800
IMG_HEIGHT=526

languages = get_languages()
ORIGIN_LANGUAGE=languages[0]
TRANSLATION_LANGUAGE=languages[1]
current_word = {}
timer_id = None

# ---------------------- BUTTON ACTIONS ----------------------
def set_card(type, language, word):
    match type:
        case "front":
            text_fill = "black"
            card_image = CARD_FRONT
        case "back":
            text_fill = "white"
            card_image = CARD_BACK
        case _:
            pass
    canvas.itemconfig(text_language, text=language, fill=text_fill)
    canvas.itemconfig(text_word, text=word, fill=text_fill)
    canvas.itemconfig(img_card, image=card_image)
    

def next_card():
    global timer_id, current_word
    if timer_id:
        window.after_cancel(timer_id)
    current_word = get_word()
    if current_word:
        set_card("front", ORIGIN_LANGUAGE, current_word[ORIGIN_LANGUAGE])
        timer_id = window.after(3000, flip_card, current_word[TRANSLATION_LANGUAGE])
    else:
        window.quit()

def flip_card(word):
    set_card("back", TRANSLATION_LANGUAGE, word)


def remove_known_word():
    remove_word(current_word)
    next_card()

# ---------------------------- UI ----------------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, highlightthickness=0, bg=BG_COLOR)
CARD_FRONT = PhotoImage(file="./images/card_front.png")
CARD_BACK = PhotoImage(file="./images/card_back.png")
img_card = canvas.create_image(IMG_WIDTH/2, IMG_HEIGHT/2, image=CARD_FRONT)
canvas.grid(row=0, column=0, columnspan=2)

text_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
text_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

img_wrong = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, bd=0, command=next_card)
btn_wrong.grid(row=1, column=0)

img_right = PhotoImage(file="./images/right.png")
btn_rigth = Button(image=img_right, highlightthickness=0, bd=0, command=remove_known_word)
btn_rigth.grid(row=1, column=1)

next_card()

window.mainloop()