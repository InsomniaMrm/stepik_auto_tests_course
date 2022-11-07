import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    # confirm = browser.switch_to.alert
    # confirm.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
