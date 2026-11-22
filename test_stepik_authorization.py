import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_stepik_authorization(browser):
    # Открываем урок
    browser.get("https://stepik.org/lesson/236895/step/1")

    wait = WebDriverWait(browser, 20)

    # Получаем логин и пароль из переменных окружения
    login = os.environ["STEPIK_LOGIN"]
    password = os.environ["STEPIK_PASSWORD"]

    # Нажимаем кнопку входа
    login_button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Войти') or contains(., 'Log in')]"
            " | //a[contains(., 'Войти') or contains(., 'Log in')]"
        ))
    )
    login_button.click()

    # Вводим логин
    email_input = wait.until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    email_input.send_keys(login)

    # Вводим пароль
    password_input = browser.find_element(
        By.ID, "id_login_password"
    )
    password_input.send_keys(password)

    # Нажимаем кнопку авторизации
    browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Ждём закрытия окна авторизации
    wait.until(
        EC.invisibility_of_element_located(
            (By.ID, "id_login_password")
        )
    )