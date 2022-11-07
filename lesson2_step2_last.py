import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    browser.find_element(By.NAME, 'firstname').send_keys('Mia')
    browser.find_element(By.NAME, 'lastname').send_keys('Smith')
    browser.find_element(By.NAME, 'email').send_keys('mail@test.com')
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()