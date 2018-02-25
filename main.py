import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Opening Chrome')
# Download chromedriver from https://chromedriver.storage.googleapis.com/index.html?path=2.35/
# Access the webdriver via its full path
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
