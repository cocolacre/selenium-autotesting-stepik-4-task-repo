import pytest, time, os
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
    time.sleep(10)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    time.sleep(10)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_success_message()
    time.sleep(10)
    