"""
TATA SKY REFRESH BOT (If thats even a thing)

Not much to say about me, but anyway -
Author - Sriram Adhithya Gopinathan
Email - sriramgopi.vkl123@gmail.com

This is to do a heavy refresh of the account so that the recharge works. Same process.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

csv_path = '' # add your path here

# opens csv file and turns it into a dictionary
with open(csv_path,'r') as file:
    dict = dict(filter(None, csv.reader(file)))
    file.close()
while True:
    usr = input('Enter customer number? (q to quit)')
    if usr in dict:
        print('Subscriber ID is :' + dict[usr])
        #login part
        """
            Its a bad idea to directly save passwords into your code, so save it into
            a keyring or use encryption (future goal)
        """
        SUBID = dict[usr]
        usrnme = ' ' # add your username
        pswd = ' ' # add your password
        start = time.time()
        chme_opt = Options()
        chme_opt.add_argument("--headless")
        browser = webdriver.Chrome(options = chme_opt)
        browser.get(('https://msales.tatasky.com/msales/'))

        username = browser.find_element_by_id('userName')
        for character in usrnme:    #need to type slowly or will detect
            username.send_keys(character)
            time.sleep(0.1)
            password = browser.find_element_by_id('password')
        for character in pswd:
                password.send_keys(character)
                time.sleep(0.1)
        button = browser.find_element_by_id('loginBtn')
        button.click()
        time.sleep(2.1)

            #refresh part
        browser.find_element_by_id('heavyRefresh').click()
        refresh_id = browser.find_element_by_id('subIdRefresh')

        refresh_id.send_keys(SUBID)
        time.sleep(0.1)
        refresh_button = browser.find_element_by_id('refreshViewSubmit')
        refresh_button.click()
        time.sleep(1)
            #read modal dialog part

            # UPDATE - Tata seems to have changed their code on this, so the final text in the modal box doesn't display,
            # and its not on my priority to do list, but I will fix it.
        msg_text = browser.find_element_by_xpath('//*[@id="TSRefreshPopup"]/div[2]')
        print(msg_text.get_attribute('title'))
        time.sleep(2)
        browser.quit()
        end = time.time()
        tme = end - start
        print('\nTime elapsed - {}s'.format(tme))
    else:
        print("No such room exits")
