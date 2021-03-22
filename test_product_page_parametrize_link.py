import pytest, time, os
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

urls = [url_base + str(i) for i in range(10)]
#pytest.param(7,marks=pytest.mark.xfail)
promo_codes = [0,1,2,3,4,5,6,pytest.param(7,marks=pytest.mark.xfail),8,9]

@pytest.mark.parametrize('promo_code',promo_codes)
def test_guest_can_add_product_to_basket(browser, promo_code):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    url_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    link = url_base+str(promo_code)
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
    time.sleep(10)
