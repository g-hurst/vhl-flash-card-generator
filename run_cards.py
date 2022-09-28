from tkinter import *
from random import randint, shuffle
from copy import copy


def run_cards_terminal(cards):
    shuffle(cards)
    cards = [(c.replace('\n', ''), v.replace('\n', '')) for c, v in cards]
    cards_master_set = copy(cards)
    def pop_random(c):
        return c.pop(randint(0, len(c) - 1))
    def get_random(c):
        return c[randint(0, len(c) - 1)]
        
    def get_int(msg):
        is_valid = False
        while not is_valid:
            try:
                int_gotten = input(msg).strip().lower()[0]
                if int_gotten == 'q' or int_gotten == 'e':
                    return -1
                int_gotten = int(int_gotten)
                is_valid = True
            except:
                pass
        return int_gotten
        
    run = True
    while(run and len(cards) > 0):
        answer = pop_random(cards)
        choices = [answer[1]]
        for _ in range(3):
            choices.append(get_random(cards_master_set)[1])
        shuffle(choices)
        print(f'Translate: {answer[0]}')
        for i, choice in enumerate(choices):
            print(f'[{i}] {choice}')
        
        # sentinal value of -1 to exit
        choice = get_int('Enter choice (quit or exit to leave)>> ')
        if choice == -1:
            run = False
        while( run and choices[choice] != answer[1]):
            print('Incorrect')
            choice = get_int('Enter choice (quit or exit to leave)>> ')
            if choice == -1:
                run = False

            
    

    


'''
Citation:
This code was largly adapted from: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/language.py

Note:
currently changed to a terminal based card running apprach because I liked it a  little better for now.
Working on making the gui a little more coustomized for this spesific task. 
'''

def run_cards(words):
        
    root = Tk()
    root.title('Flashcards GUI')
    root.geometry("550x450")

    # get a count of our word list
    count = len(words)

    def next():
        global hinter, hint_count
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