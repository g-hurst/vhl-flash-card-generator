from run_cards import run_cards
from get_words import get_words


if __name__ == '__main__':
    link = 'https://m3a.vhlcentral.com/sections/1276373/activities/238470'  # vhl link to vocab page
    creds =  tuple([x.strip() for x in open('login.txt', 'r').readlines()]) # saved creds in a local file
    
    words = get_words(creds, link)

    run_cards(words)
    