import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")

    # Путь к файлу рядом со скриптом
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "bio.txt")

    # Создаём файл, если его нет
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("test")

    print("Путь к файлу:", file_path)
    print("Файл существует:", os.path.exists(file_path))

    # Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)

    # Проверяем, что путь подставился
    print("Значение в поле:", repr(file_input.get_attribute("value")))

    # Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

except Exception as e:
    print("ОШИБКА:", type(e).__name__, ":", e)

finally:
    time.sleep(30)
    browser.quit()