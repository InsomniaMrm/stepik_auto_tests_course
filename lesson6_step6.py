from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     letters = string.ascii_lowercase
#     random_word = ''.join(random.choice(letters) for _ in range(8))
#     for element in elements:
#         element.send_keys(random_word)
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# Уникальность селекторов: часть 2
try:
    link = "http://suninjuly.github.io/registration1.html"
    new_link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(new_link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, 'form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
    input3.send_keys("mail@mail.ru")
    input4 = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
    input3.send_keys("88005553535")
    input5 = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
    input3.send_keys("USA")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()