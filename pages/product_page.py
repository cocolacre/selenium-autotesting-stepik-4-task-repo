from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET)
        button.click()
        #self.solve_quiz_and_get_code()
    def get_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.product_name = product_name_element.text.strip()
        return product_name_element.text.strip()
        
    def get_product_price(self):
        price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = price_element.text.split("&")[0].strip()
        #self.price = price
        return price
    
    def get_added_product_name(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        return added_product_name.text.strip()
        
    def get_basket_amount(self):
        amount_element = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT)
        amount = amount_element.text.split("&")[0].strip()
        return amount
        
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_TO_BASKET), "ADD TO BASKET button not found!"
        
        
    def should_have_added_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Added product name not found!"
    
    def should_be_basket_total_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_AMOUNT), "Basket total amount not found!"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is present, but should have dissapeared"
        