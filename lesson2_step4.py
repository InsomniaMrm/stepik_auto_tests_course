import math
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
