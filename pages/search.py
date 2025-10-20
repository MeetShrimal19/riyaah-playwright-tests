import time

from pages.BasePage import Basepage
from playwright.sync_api import Page
from src.elements.elements_homepage import homepage
from src.elements.elements_search import SearchElements
from src.elements.elements_cart import CartElements
from pages.Checkout import Checkout

class SearchPage(Checkout):
    def __init__(self, page : Page):
        super().__init__(page)

    def click_searchbar(self, product_name :str):
        self.clickButton(SearchElements.xpath_searchbar)
        self.page.wait_for_selector(SearchElements.xpath_searchbar, state="visible", timeout=30000)
        self.typevalue(SearchElements.xpath_searchbar, product_name)
        self.press_key(SearchElements.xpath_searchbar, "Enter")
        self.page.wait_for_load_state("networkidle")
        self.AcceptCookie()
        self.clickButton(SearchElements.xpath_addtocart_jennifer)
        self.clickButton(CartElements.xpath_cart)
        self.page.wait_for_selector(CartElements.xpath_checkout, state="attached", timeout=30000)
        self.ClickCheckout()
        self.Registered_checkout_paytabs()
        self.Registered_checkout_COD()


