from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import sys

'''
portions of this code was adapted from: https://github.com/peterje/auto-vhl
'''

def get_words(credentials:tuple, link:str) -> list[tuple]:
    def __get_page__(url):
        browser.get(url)

    def __logout__():
        browser.get("https://www.vhlcentral.com/logout")
    def __login__(usr, pwd):
        # enter in username
        user = browser.find_element(By.ID, 'user_session_username')
        user.send_keys(usr)
        # enter in password
        user_password = browser.find_element(By.ID, 'user_session_password')
        user_password.send_keys(pwd)
        # click login
        login_button = browser.find_element(By.NAME, 'commit')
        login_button.click()

    # start browser
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    
    # go to vhl home
    __get_page__("https://www.vhlcentral.com/home")

    # log in
    username, password = credentials
    __login__(username, password)

    # go to vocab page
    __get_page__(link)

    data = browser.page_source.encode('utf-8')
    data = BeautifulSoup(data, 'html.parser').find_all('tr', {'class':'c-row'})

    # parses the vocab words from the page
    results = []
    exp = re.compile(r'([^\n]*)(?:\s|\\n|\n)*([^\n]*)')
    for d in data:
        d = d.get_text().strip()
        if exp.match(d):
            results.append(exp.search(d).groups())
    
    # cleanup the session
    __logout__()
    browser.close()
    
    return results

if __name__ == '__main__': 
    link = 'https://m3a.vhlcentral.com/sections/1276373/activities/238470'  # vhl link to vocab page
    creds =  tuple([x.strip() for x in open('login.txt', 'r').readlines()]) # saved creds in a local file
    
    results = get_words(creds, link)
    
    # writes the words to a file
    with open('words.txt', 'w') as f:
        for target, translation in results:
            f.write(f'{target},{translation}\n')

    sys.exit()