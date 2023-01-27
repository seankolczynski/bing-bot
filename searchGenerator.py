import linecache
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def searchGenerator():
    dailySearchLimit = 30
    searchCount = 0
    MaxLine = len(open("TheMasterList.txt").readlines())
    with open("lists/ThawList.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    print(lines)
    thawList = open("lists/ThawList.txt", "w")

    # MaxLine = 60

    with open("lists/TodaysSearches.txt", "w") as shortlist:
        dart = random.randint(0, MaxLine - 1)
        straws = list()
        while searchCount <= dailySearchLimit:
            while dart in straws:
                dart = random.randint(0, MaxLine - 1)
            searchTerm = linecache.getline("TheMasterList.txt", dart)
            # searchTerm = linecache.getline("testList.txt", dart)
            searchTerm = searchTerm.replace('\n', '')
            straws.append(dart)
            if searchTerm not in lines:
                shortlist.write(searchTerm + '\n')
                thawList.write(searchTerm + '\n')
                searchCount = searchCount + 1


def searchMonkey(driver):
    searchBar = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
    with open("lists/TodaysSearches.txt") as shortlist:
        searchTerms = shortlist.readlines()
        for term in searchTerms:
            print(searchBar)
            searchBar.send_keys(term, Keys.RETURN)
            time.sleep(5)
            searchBar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
            searchBar.clear()
            searchBar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
    return driver

def searchMobile(driver):
    time.sleep(2)
    driver = webdriver.Chrome()
    driver.get('http://www.bing.com/')
    page = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "html")))
    ActionChains(page).send_keys(Keys.COMMAND, "f")



# def searchChiller(term):
#
#

    # create action chain object
    # action = ActionChains(driver)

    # perform the operation
    # action.key_down(Keys.CONTROL).key_down('F').perform()
    # action.key_down(Keys.CONTROL, 'F').perform()

    # action = ActionChains(driver)
    # action.key_down(Keys.COMMAND).send_keys('F').perform()
    # # action.key_down(Keys.COMMAND).key_down(Keys.LEFT_ALT).send_keys('I').perform()
    # # action.send_keys(Keys.ENTER).perform()
    # # action.key_down(Keys.COMMAND).key_down(Keys.LEFT_ALT).send_keys('I').perform()
