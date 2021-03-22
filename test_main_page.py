import pytest, time, os
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу 
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста 
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_url()
    page.should_not_be_checkout_button()
    page.should_be_empty_basket_message()
    page.should_not_be_basket_summary_element()
    #time.sleep(30)


infos = """
languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}

language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
"""

