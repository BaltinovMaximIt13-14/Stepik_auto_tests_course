from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        button.click()

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def should_be_success_message(self, product_name):
        message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert product_name in message, (
            f"Expected product name '{product_name}' "
            f"not found in message: '{message}'"
        )

    def should_be_basket_total_equal_to_product_price(self, product_price):
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text

        actual_total = basket_total.split("Basket total:")[1].split("\n")[0].strip()

        assert product_price == actual_total
    def debug_basket(self):
        print("\nBASKET HTML:")
        print(self.browser.find_element(
            By.CSS_SELECTOR, ".basket-mini"
        ).get_attribute("innerHTML"))
