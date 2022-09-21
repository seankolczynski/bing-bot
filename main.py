import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    emailInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "i0116")))
    next = driver.find_element(By.ID, "idSIButton9")
    emailInput.send_keys('sean.kolczynski@gmail.com')
    ActionChains(driver).click(next).perform()
    time.sleep(10)
    passwordInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "passwd")))
    passw = driver.find_element(By.NAME, "passwd")
    passwordInput.send_keys('password')
    signIn = driver.find_element(By.ID, "idSIButton9")
    ActionChains(driver).click(signIn).perform()

    # ActionChains(driver).click(emailInput).perform()
