import os
from run_cards import run_cards_terminal
from get_words import get_words


save_directory = 'card_sets'
splitting_sequence = '~|~'


def save_cards(cards, fname):
    if save_directory not in os.listdir('./'): os.mkdir(save_directory)
    fname = save_directory + '/' + fname
    with open(fname, 'w') as f:
        for word, translation in cards:
            f.write(f'{word}{splitting_sequence}{translation}\n')

if __name__ == '__main__':
    choice_keys = {
        'scrape new': 1,
        'run cards': 2,
        'remove cards': 3,
        'exit': 4
    }

    message =  'Select from the following options: \n'
    message += '[{}] Scrape a new set of words\n'.format(choice_keys['scrape new'])
    message += '[{}] Run flashcards from an existing set\n'.format(choice_keys['run cards'])
    message += '[{}] Remove an existing set\n'.format(choice_keys['remove cards'])
    message += '[{}] Close the program\n\n'.format(choice_keys['exit'])
    message += 'What would you like to do >> '

    

    run_program = True
    while run_program:
        try:
            choice = int(input(message).strip())
        except:
            print('Invalid input')
            continue
        
        # TODO: get_words does not strip the newline characters from the words when they are scrapred
        if choice == choice_keys['scrape new']:
            username = input('[+] Enter VHL username/email >> ')
            password = input('[+] Enter VHL password >> ')
            link     = input('[+] Enter link for VHL page >> ')
            
            words = get_words((username, password), link)
            fname = input('[+] Enter name to save cards under >> ')
            save_cards(words, fname)

        elif choice == choice_keys['run cards']:
            options = os.listdir('./' + save_directory)
            print('Files avalable: ')
            for i, o in enumerate(options):
                print(f'\t[{i+1}] {o}')
            set_selected = int(input('\tSelect a file to run >> '))
            path = save_directory + '/' + options[set_selected-1]
            data = [line.split(splitting_sequence) for line in open(path, 'r')]
            run_cards_terminal(data)
                    
        elif choice == choice_keys['remove cards']:
            pass

        elif choice == choice_keys['exit']:
            run_program = False
        
        else:
            print('\nInvalid Option Detected: {}'.format(choice))


        
        