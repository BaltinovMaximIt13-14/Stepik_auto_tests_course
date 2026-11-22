import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.first"
        ).send_keys("Ivan")

        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.second"
        ).send_keys("Petrov")

        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.third"
        ).send_keys("ivan@example.com")

        self.browser.find_element(
            By.CSS_SELECTOR, "button.btn"
        ).click()

        welcome_text = self.browser.find_element(
            By.TAG_NAME, "h1"
        ).text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.first"
        ).send_keys("Ivan")

        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.second"
        ).send_keys("Petrov")

        self.browser.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.third"
        ).send_keys("ivan@example.com")

        self.browser.find_element(
            By.CSS_SELECTOR, "button.btn"
        ).click()

        welcome_text = self.browser.find_element(
            By.TAG_NAME, "h1"
        ).text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()