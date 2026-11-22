
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, (
            "Login is not in current URL"
        )

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"
