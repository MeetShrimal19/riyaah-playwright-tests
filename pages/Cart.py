import time
from venv import logger
from utils.loggers import logger

from playwright.async_api import Page
from src.elements.elements_search import SearchElements

from pages.BasePage import Basepage
from pages.Checkout import Checkout
from src.elements.elements_cart import CartElements
from src.elements.elements_homepage import homepage

class Cart(Checkout):
    def __init__(self, page:Page):
        super().__init__(page)

    def CartWishlist(self):
        self.page.wait_for_load_state("networkidle")
        self.AcceptCookie()
        self.clickButton(homepage.xpath_perfume_segment)
        self.clickButton(SearchElements.xpath_addtocart_jennifer)
        self.clickButton(CartElements.xpath_cart)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector(CartElements.xpath_delete_item)
        self.clickButton(CartElements.xpath_delete_item)
        self.page.wait_for_selector(CartElements.xpath_yes_remove_item)
        self.clickButton(CartElements.xpath_yes_remove_item)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("text=You do not have any item in your cart", timeout=10000)
        if self.page.locator("text=You do not have any item in your cart").is_visible():
            logger.info("Empty cart message shown")
        else:
            logger.error("empty cart message not found")

    def MovetoWishlist(self):
        self.page.wait_for_load_state("networkidle")
        self.AcceptCookie()
        self.clickButton(homepage.xpath_perfume_segment)
        self.clickButton(SearchElements.xpath_addtocart_jennifer)
        self.clickButton(CartElements.xpath_cart)
        self.page.wait_for_load_state("networkidle")
        self.ClickCheckout()
        logger.info("Checkout Clicked")
        self.Login_Otp("8955251538", "1", "5", "5", "1", "5", "5")
        logger.info("Login done")
        self.page.wait_for_selector(CartElements.xpath_delete_item)
        self.clickButton(CartElements.xpath_delete_item)
        logger.info("Delete button clicked")
        self.clickButton(CartElements.xpath_movetowishlist)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("text=You do not have any item in your cart", timeout=10000)
        if self.page.locator("text=You do not have any item in your cart").is_visible():
            logger.info("Empty cart message shown")
        else:
            logger.error("empty cart message not found")
        self.page.wait_for_selector(homepage.xpath_Wishlist, timeout=1000)
        self.clickButton(homepage.xpath_Wishlist)
        self.page.wait_for_load_state("networkidle")
        logger.info("Wishlist homepage clicked")
        self.page.wait_for_selector(homepage.xpath_Wishlist_search)
        self.clickButton(homepage.xpath_Wishlist_search)
        self.typevalue(homepage.xpath_Wishlist_search,"Jennifer Lopez Live Perfume Eau De Parfum For Women 100 ml")
        logger.info("product name typed")
        # ✅ Assertion step
        self.page.wait_for_load_state("networkidle")
        product_locator = self.page.locator("text=Jennifer Lopez Live Perfume Eau De Parfum For Women 100 ml")

        assert product_locator.is_visible(), "❌ Product not visible in wishlist after search!"
        logger.info("✅ Product found in wishlist after search!")
        time.sleep(5)