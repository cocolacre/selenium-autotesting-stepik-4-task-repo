import pytest, time, os
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    
    product_price = page.get_product_price()
    product_name = page.get_product_name()
    
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_have_added_product_to_basket()
    page.should_be_basket_total_price()
    
    added_product_name = page.get_added_product_name()
    assert added_product_name == product_name, "Product name is not the same as added product name!"
    print("Checked [added_product_name == product_name]")
    basket_amount = page.get_basket_amount()
    assert basket_amount == product_price, "Product price not equal to basket amount!"
    print("Checked [basket_amount == product_price]")
    #time.sleep(10)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
    #time.sleep(10)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    #time.sleep(10)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_success_message()
    #time.sleep(10)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке 
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста 
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_url()
    page.should_not_be_checkout_button()
    page.should_be_empty_basket_message()
    page.should_not_be_basket_summary_element()
    