import random
from tkinter import *
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = {}

try:
    df = read_csv('data/to_learn.csv')
    print(f"loaded data: {df}")
except FileNotFoundError:
    df = read_csv('data/french_words.csv')
    print(f"loaded data: {df}")

french_dict = df.to_dict(orient='records')

def correct_clicked():
    french_dict.remove(current_card)
    DataFrame(french_dict).to_csv('data/to_learn.csv', index=False)
    next_card()

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    to_lang = list(current_card.keys())[1]
    canvas.itemconfig(word_text, text=to_lang, fill="white")
    to_word = current_card[to_lang]
    canvas.itemconfig(language_text, text=to_word, fill="white")

def next_card():
    global flip_timer, current_card

    if flip_timer is not None:
        window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    if len(french_dict) == 0:
        canvas.itemconfig(word_text, text="Done!", fill="black")
        canvas.itemconfig(language_text, text="YOu've learned all words", fill="black")
        return
    current_card = random.choice(french_dict)
    from_lang = list(current_card.keys())[0]
    from_word = current_card[from_lang]

    canvas.itemconfig(language_text, text=from_word, fill="black")
    canvas.itemconfig(word_text, text=from_lang, fill="black")
    flip_timer = window.after(3000, flip_card)
    #canvas.update()
# print(word)

window = Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

#Images
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=900, height=626, background=BACKGROUND_COLOR, bd=0, highlightthickness=0)
canvas_image = canvas.create_image(450,313,image=card_front_image)
language_text = canvas.create_text(440,363, text="", font=("Arial", 60, "bold"))
word_text = canvas.create_text(440, 140, text="", font=("Arial", 40, "italic"))
canvas.grid(row=0,column=0,columnspan=2)



correct_button = Button(image=correct_image, bd=0, highlightthickness=0, command=correct_clicked)
correct_button.grid(row=1,column=1)

incorrect_button = Button(image=incorrect_image, bd=0, highlightthickness=0, command=next_card)
incorrect_button.grid(row=1,column=0)

# language_label = Label(text='French', font=("Arial", 40, "italic"), bg="white")
# language_label.place(x=350,y=140)

# translation_label = Label(text='trouve', font=("Arial", 60, "bold"), bg="white")
# translation_label.place(x=310,y=263)

next_card()
window.mainloop()