
import os
import time
import math
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_guest_should_see_correct_message(browser, link):
    wait = WebDriverWait(browser, 20)

    # Открываем страницу
    browser.get(link)

    # Авторизация
    login = os.environ["STEPIK_LOGIN"]
    password = os.environ["STEPIK_PASSWORD"]

    login_button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Войти') or contains(., 'Log in')]"
            " | //a[contains(., 'Войти') or contains(., 'Log in')]"
        ))
    )
    login_button.click()

    email_input = wait.until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    email_input.send_keys(login)

    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(password)

    browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Ждём завершения авторизации
    wait.until(
        EC.invisibility_of_element_located(
            (By.ID, "id_login_password")
        )
    )

    # Находим поле ответа и очищаем его
    answer_field = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "textarea")
        )
    )
    answer_field.clear()

    # Вычисляем новый ответ для каждой задачи
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))

    # Отправляем ответ
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.submit-submission")
        )
    )
    submit_button.click()

    # Ждём появления обратной связи
    feedback = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".smart-hints__hint")
        )
    )

    # Проверяем текст обратной связи
    assert feedback.text == "Correct!", (
        f"Unexpected feedback: {feedback.text}"
    )
