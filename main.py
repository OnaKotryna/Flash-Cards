from tkinter import *

BG_COLOR="#9bdeac"
IMG_WIDTH=800
IMG_HEIGHT=526

ORIGIN_LANGUAGE="German"
TRANSLATION_LANGUAGE="English"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, highlightthickness=0, bg=BG_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(IMG_WIDTH/2, IMG_HEIGHT/2, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

text_language = canvas.create_text(400, 150, text=ORIGIN_LANGUAGE, font=("Arial", 40, "italic"))
text_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

window.mainloop()