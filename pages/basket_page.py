from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "basket" in self.browser.current_url, "'basket' substring not found within current URL"
    
    def should_not_be_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Non-empty basket: checkout button is presented, but should not be"
    
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message element not found!"

    def should_be_empty_basket_message_en(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE_EN), "Empty basket message element not found!"
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE_EN).text
        assert "mpty" in empty_message, "'empty' substring not found in EMPTY_BASKET_MESSAGE_EN"
    
    def should_not_be_basket_summary_element(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Found basket contents summary, while we should not!"
        