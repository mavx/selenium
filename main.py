import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Opening Chrome')
browser = webdriver.Chrome('/Users/mavx/Downloads/chromedriver')
print('Accessing Yahoo.com')
browser.get('http://www.yahoo.com')

time.sleep(2)

print('Finding search box')
elem = browser.find_element_by_name('p')  # Find the search box
print('Searching for seleniumhq')
elem.send_keys('seleniumhq' + Keys.RETURN)

time.sleep(2)

print('Quitting browser')
browser.quit()
