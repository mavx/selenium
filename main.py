import logging
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from util.logger import log_setup


def main():
    print('Opening Chrome')
    # Download chromedriver from https://chromedriver.storage.googleapis.com/index.html?path=2.35/
    # Access the webdriver via its full path
    # browser = webdriver.Chrome('/Users/mavx/Downloads/chromedriver')
    browser = webdriver.Chrome()
    print('Accessing Yahoo.com')
    browser.get('http://www.yahoo.com')

    time.sleep(2)

    print('Finding search box')
    elem = browser.find_element_by_name('p')  # Find the search box
    print('Searching for seleniumhq')
    elem.send_keys('seleniumhq' + Keys.RETURN)

    # Randomising wait time to mimic humans!
    time.sleep(random.randint(0, 5))

    print('Quitting browser')
    browser.quit()


if __name__ == '__main__':
    # Global variables
    LOGGER_LEVEL = logging.INFO  # TODO: Set logging level | Options: 'INFO', 'DEBUG', 'ERROR', etc.

    PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
    SCRIPT_NAME = os.path.basename(__file__)[:-3]
    LOG_FILENAME = SCRIPT_NAME
    logger = log_setup(PARENT_DIR, LOG_FILENAME, LOGGER_LEVEL)

    main()
