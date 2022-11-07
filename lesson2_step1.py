import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # x_element = browser.find_element(By.ID, 'treasure')
    # x = x_element.get_attribute('valuex')
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    y = calc(x)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("window.scrollBy(0, 150);")

    field = browser.find_element(By.ID, 'answer')
    field.send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
