import random
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def register_new_user(self, email=None, password=None):
        def get_random_string(length = 10):
            return ''.join(["ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[random.randint(0,35)] for x in range(length)])
        if email == None:
            email = get_random_string() + "@gmail.com"
        if password == None:
            password = get_random_string(length=12)
        
        field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        field.send_keys(email)
        field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT_1)
        field.send_keys(password)
        field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT_2)
        field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' substring not found within current URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found!"

    