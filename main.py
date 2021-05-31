"""
TATA SKY RECHARGE BOT (If thats even a thing)

Not much to say about me, but anyway -
Author - Sriram Adhithya Gopinathan
Email - sriramgopi.vkl123@gmail.com
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

csv_path = '' #add your path here to the csv file

# opens csv file and turns it into a dictionary
with open(csv_path,'r') as file:
    dict = dict(filter(None, csv.reader(file)))
    file.close()

while True:
    try:
        usr = input('Enter customer number? (ctrl+c to quit)')
        amt = input('Enter recharge amount: ')
        if usr in dict:
            print('Subscriber ID is :' + dict[usr])
            #login part
            SUBID = dict[usr]

            """
            Its a bad idea to directly save passwords into your code, so save it into
            a keyring or use encryption (future goal)
            """
            usrnme = ' '#User name for your account
            pswd = ' '# Password for your account
            start = time.time()
            #feel free to add your options
            chme_opt = Options()
            browser = webdriver.Chrome(options = chme_opt)
            browser.get(('https://msales.tatasky.com/msales/'))
            



            # The login page will throw an "Invalid password error" if you directly login, so loop through the string for each character
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

            #recharge part
            browser.find_element_by_id('recharge').click()
            recharge_id = browser.find_element_by_id('subIDRecharge')
            recharge_id.send_keys(SUBID)
            recharge_amt = browser.find_element_by_id('rechargeAmount')
            recharge_amt.send_keys(amt)
            btn2 = browser.find_element_by_id('rechargeSubmit')
            btn2.click()
            btn3 = browser.find_element_by_id('rechargeConfirm')
            btn3.click()
            time.sleep(0.2)
            # UPDATE - Tata seems to have changed their code on this, so the final text in the modal box doesn't display,
            # and its not on my priority to do list, but I will fix it.
            msg_text = browser.find_element_by_xpath('//*[@id="TSRechargePopup"]/div[2]/p').text
            print(msg_text)
            end = time.time()
            tme = end - start
            print('\nTime elapsed - {}s'.format(tme))
    except KeyboardInterrupt:
        quit()
