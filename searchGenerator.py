import linecache
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def searchGenerator():
    dailySearchLimit = 30
    searchCount = 0
    MaxLine = len(open("TheList.txt").readlines())
    with open("TodaysSearches.txt", "w") as shortlist:
        while searchCount <= dailySearchLimit:
            dart = random.randint(0, MaxLine - 1)
            searchTerm = linecache.getline("TheList.txt", dart)
            shortlist.write(searchTerm)
            searchCount = searchCount + 1


def searchMonkey(driver):
    searchBar = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
    with open("TodaysSearches.txt") as shortlist:
        searchTerms = shortlist.readlines()
        for term in searchTerms:
            print(searchBar)
            searchBar.send_keys(term, Keys.RETURN)
            time.sleep(5)
            searchBar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
            searchBar.clear()
            searchBar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
