from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "https://suninjuly.github.io/registration2.html" # замените первую ссылку на эту для проверки падения
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля с уникальными селекторами
    input_first_name = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    input_first_name.send_keys("Иван")

    input_last_name = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    input_last_name.send_keys("Иванов")

    input_email = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    input_email.send_keys("ivanov@example.com")

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
