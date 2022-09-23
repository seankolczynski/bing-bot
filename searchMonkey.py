import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from searchGenerator import searchGenerator


def searchMonkey(driver):
    searchBar = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
    searchCount = 0
    searchGoal = 30
    options = 1
    with open("Genie.txt") as genie:
        options = len(genie.readlines())
    while searchCount < searchGoal:
        currentUrl = driver.current_url
        searchBar.send_keys(searchGenerator(options))
        searchBar.send_keys(Keys.RETURN)
        time.sleep(5)
        searchBar = WebDriverWait(driver, 5).until(EC.url_changes(currentUrl));
