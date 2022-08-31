from tkinter import *
from random import randint

'''
Citation:
This code was largly adapted from: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/language.py
'''


def run_cards(words):
        
    root = Tk()
    root.title('German Flashcard GUI')
    root.geometry("550x450")

    # get a count of our word list
    count = len(words)

    def next():
        nonlocal hinter, hint_count
        # Clear the screen
        answer_label.config(text="")
        my_entry.delete(0, END)
        hint_label.config(text="")
        # Reset Hint stuff
        hinter = ""
        hint_count = 0

        # Create random selection
        global random_word
        random_word = randint(0, count-1)
        # update label with foreign Word
        foreign_word.config(text=words[random_word][0])

    def answer():
        if my_entry.get().capitalize() == words[random_word][1].capitalize():
            answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
        else:
            answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

    # Keep Track Of the Hints
    hinter = ""
    hint_count = 0
    def hint():
        nonlocal hint_count
        nonlocal hinter

        if hint_count < len(words[random_word][1]):
            hinter = hinter + words[random_word][1][hint_count]
            hint_label.config(text=hinter)
            hint_count +=1

    # Labels
    foreign_word = Label(root, text="", font=("Helvetica", 36))
    foreign_word.pack(pady=50)

    answer_label = Label(root, text="")
    answer_label.pack(pady=20)

    my_entry = Entry(root, font=("Helvetica", 18))
    my_entry.pack(pady=20)

    # Create Buttons
    button_frame = Frame(root)
    button_frame.pack(pady=20)

    answer_button = Button(button_frame, text="Answer", command=answer)
    answer_button.grid(row=0, column=0, padx=20)

    next_button = Button(button_frame, text="Next", command=next)
    next_button.grid(row=0, column=1,)

    hint_button = Button(button_frame, text="Hint", command=hint)
    hint_button.grid(row=0, column=2, padx=20)

    # Create Hint Label
    hint_label = Label(root, text="")
    hint_label.pack(pady=20)

    # Run next function when program starts
    next()

    root.mainloop()