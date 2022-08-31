from run_cards import run_cards
from get_words import get_words


if __name__ == '__main__':
    username = input('[+] Enter VHL username/email >> ')
    password = input('[+] Enter VHL password >> ')
    link = input('[+] Enter link for VHL page >> ')
    # link = 'https://m3a.vhlcentral.com/sections/1276373/activities/238470'  # vhl link to vocab page
    # creds =  tuple([x.strip() for x in open('login.txt', 'r').readlines()]) # saved creds in a local file
    
    words = get_words((username, password), link)

    run_cards(words)
    