import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.bing.com/')

    time.sleep(5)  # Let the user actually see something!
    signIn = driver.find_element(By.ID, "id_l")
    ActionChains(driver).click(signIn).perform()
    emailInput = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "i0116")))
    next = driver.find_element(By.ID, "idSIButton9")
    emailInput.send_keys('sean.kolczynski@gmail.com')
    ActionChains(driver).click(next).perform()
    passwordInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "passwd")))
    passw = driver.find_element(By.NAME, "passwd")
    # need to get password from file
    passwordInput.send_keys('###########')
    signIn = driver.find_element(By.ID, "idSIButton9")
    ActionChains(driver).click(signIn).perform()
    time.sleep(2)
    staySignedIn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    ActionChains(driver).click(staySignedIn).perform()
    searchBar = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
    searchBar.send_keys("Howard Stern")
    searchBar.send_keys(Keys.RETURN)


    # ActionChains(driver).click(emailInput).perform()
