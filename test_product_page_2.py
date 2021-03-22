import pytest, time, os
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    
    product_price = page.get_product_price()
    product_name = page.get_product_name()
    
    page.add_product_to_basket()
    
    page.should_have_added_product_to_basket()
    page.should_be_basket_total_price()
    
    added_product_name = page.get_added_product_name()
    assert added_product_name == product_name, "Product name is not the same as added product name!"
    print("Checked [added_product_name == product_name]")
    basket_amount = page.get_basket_amount()
    assert basket_amount == product_price, "Product price not equal to basket amount!"
    print("Checked [basket_amount == product_price]")
    time.sleep(30)
