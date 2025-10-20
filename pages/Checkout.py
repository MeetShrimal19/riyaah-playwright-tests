import time

from pages.BasePage import Basepage
from src.elements.elements_checkout import Checkout_elements
from src.elements.elements_cart import CartElements
from playwright.sync_api import Page, expect


class Checkout(Basepage):
    def __init__(self, page:Page):
        super().__init__(page)

    def ClickCheckout(self):
        checkout_btn = self.page.locator(CartElements.xpath_checkout).first
        checkout_btn.scroll_into_view_if_needed()
        checkout_btn.wait_for(state="visible", timeout=30000)
        checkout_btn.click()

    def ClickCOD(self):
        print("⏳ Waiting for COD option to load after Checkout...")
        self.page.wait_for_load_state("networkidle", timeout=90000)
        cod_btn = self.page.locator(Checkout_elements.xpath_COD).first
        cod_btn.wait_for(state="visible", timeout=60000)
        for i in range(5):
            if cod_btn.is_enabled() and cod_btn.is_visible():
                try:
                    cod_btn.click()
                    print("🟢 COD button clicked successfully.")
                    return
                except Exception as e:
                    print(f"⚠️ Attempt {i + 1}: Click failed ({e}). Retrying...")
            self.page.wait_for_timeout(1000)
        raise Exception("❌ COD button was never clickable even after retries.")

    def ClickOnlinepayment(self, name, cardnumber, month, year, CVV):

        checkout_btn = self.page.locator(Checkout_elements.xpath_Onlinepayment).first
        checkout_btn.scroll_into_view_if_needed()
        checkout_btn.wait_for(state="visible", timeout=30000)
        checkout_btn.click()
        self.clickButton(Checkout_elements.xpath_confirmandpay)
        self.page.locator(Checkout_elements.xpath_holdername).clear()
        self.typevalue(Checkout_elements.xpath_holdername, name)
        self.waitForElementVisible(Checkout_elements.xpath_cardnumber, timeout=60000)
        self.typevalue(Checkout_elements.xpath_cardnumber, cardnumber)
        self.waitForElementVisible(Checkout_elements.xpath_month, timeout=60000)
        self.typevalue(Checkout_elements.xpath_month, month)
        self.waitForElementVisible(Checkout_elements.xpath_year)
        self.typevalue(Checkout_elements.xpath_year, year)
        self.waitForElementVisible(Checkout_elements.xpath_CVV)
        self.typevalue(Checkout_elements.xpath_CVV, CVV)
        # self.clickButton(Checkout_elements.xpath_paynow_online)
        pay_now_btn = self.page.locator(Checkout_elements.xpath_paynow_online)
        pay_now_btn.wait_for(state="visible", timeout=60000)
        btn_handle = pay_now_btn.element_handle()
        self.page.wait_for_function(
            "el => el && !el.disabled",
            arg=btn_handle,
            timeout=90000
        )
        print("✅ Pay Now button is now enabled, clicking...")
        with self.page.expect_navigation(wait_until="load", timeout=120000):
            pay_now_btn.click()

    def Login_Otp(self, mobile_number, OTP1, OTP2, OTP3, OTP4, OTP5, OTP6 ):
        self.typevalue(Checkout_elements.xpath_mobilenumber, mobile_number)
        self.clickButton(Checkout_elements.xpath_proceed)
        self.typevalue(Checkout_elements.xpath_OTP1, OTP1)
        self.typevalue(Checkout_elements.xpath_OTP2, OTP2)
        self.typevalue(Checkout_elements.xpath_OTP3, OTP3)
        self.typevalue(Checkout_elements.xpath_OTP4, OTP4)
        self.typevalue(Checkout_elements.xpath_OTP5, OTP5)
        self.typevalue(Checkout_elements.xpath_OTP6, OTP6)
        self.clickButton(Checkout_elements.xpath_next)
        self.page.wait_for_load_state("networkidle")

    def Registered_checkout_paytabs(self):
        self.Login_Otp("8955251538", "1", "5", "5", "1", "5", "5")
        self.ClickCheckout()
        self.ClickOnlinepayment("Meet Shrimal", "4111111111111111", "08","26", "123")
        self.clickButton(Checkout_elements.xpath_confirmandpay)

    def Registered_checkout_COD(self):
        self.Login_Otp("8955251538", "1", "5", "5", "1", "5", "5")
        self.ClickCheckout()
        self.ClickCOD()
        self.clickButton(Checkout_elements.xpath_confirmandpay)
        self.clickButton(Checkout_elements.xpath_backtohome)






