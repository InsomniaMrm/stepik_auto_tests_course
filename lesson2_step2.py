import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x) + int(y))


link = 'http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    summa = calc(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(summa)  # ищем элемент
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()