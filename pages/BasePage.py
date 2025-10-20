from playwright.sync_api import Page, expect
from src.elements.elements_homepage import homepage
from utils.loggers import logger

class Basepage:
    def __init__(self, page:Page):
        self.page = page



    def clickButton(self, locator: str, timeout: int = 30000):
            element = self.page.locator(locator)
            element.wait_for(state="visible", timeout=timeout)
            element.scroll_into_view_if_needed()
            element.click()

    def waitForElementVisible(self, locator: str, timeout: int = 30000):
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    def type2(self, locator:str,txt: str):
        timeout= 50000
        delay= None
        var1 = self.page.locator(locator)
        var1.type(txt, delay=delay, timeout=timeout)
        timeout: 50000


    def typevalue(self, locator : str, txt : str):
        self.page.locator(locator).fill(txt)

    def close_clevertap_popup(self):
        try:
            print("⏳ Checking for CleverTap popup...")
            self.page.wait_for_timeout(2000)

            # ✅ Case 1: Direct DOM popup
            popup = self.page.locator("ct-web-popup-imageonly, ct-web-popup, div[id*='clevertap']")
            if popup.count() > 0:
                close_btn = popup.locator("xpath=.//*[contains(@id,'close') or contains(@class,'close')]")
                if close_btn.is_visible():
                    close_btn.click()
                    print("✅ CleverTap popup closed (direct element).")
                    return
                else:
                    print("⚠️ Close button not visible in direct element.")

            # ✅ Case 2: Popup inside an iframe
            iframe = self.page.frame_locator("iframe[src*='clevertap']")
            close_btn_iframe = iframe.locator("xpath=//*[contains(@id,'close') or contains(@class,'close')]")
            if close_btn_iframe.count() > 0 and close_btn_iframe.is_visible():
                close_btn_iframe.click()
                print("✅ CleverTap popup closed (inside iframe).")
                return

            # ✅ Case 3: Fallback — force remove if found but not clickable
            removed = self.page.evaluate("""
                (() => {
                    const el1 = document.querySelector('ct-web-popup-imageonly');
                    const el2 = document.querySelector('ct-web-popup');
                    const el3 = document.querySelector("iframe[src*='clevertap']");
                    if (el1) el1.remove();
                    if (el2) el2.remove();
                    if (el3) el3.remove();
                    return !!(el1 || el2 || el3);
                })();
            """)
            if removed:
                print("🧹 Force removed CleverTap popup from DOM.")
            else:
                print("⚠️ No CleverTap popup detected.")
        except Exception as e:
            print(f"⚠️ Failed to close CleverTap popup: {e}")

    def press_key(self, locator: str, key: str):
        """Press a keyboard key on a locator."""
        self.page.locator(locator).press(key)

    def scroll_to_element(self, locator: str, timeout: int = 30000):
        element = self.page.locator(locator)
        element.scroll_into_view_if_needed(timeout=timeout)

    def wait_until_visible(self, locator, timeout=60000):
        """Wait until the element becomes visible."""
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    def safe_click(self, locator, retries=10, interval=1):
        """Safely click an element, retrying if not ready."""
        element = self.wait_until_visible(locator)
        for i in range(retries):
            if element.is_enabled() and element.is_visible():
                try:
                    element.click()
                    print(f"🟢 Clicked element: {locator}")
                    return
                except Exception as e:
                    print(f"⚠️ Attempt {i+1}: Click failed ({e}), retrying...")
            self.page.wait_for_timeout(interval * 1000)
        raise Exception(f"❌ Element not clickable after {retries} retries: {locator}")

    def AcceptCookie(self):
        try:
            # Wait for either English or Arabic cookie popup to appear
            self.page.wait_for_timeout(2000)
            if self.page.locator(homepage.xpath_accept_english).count() > 0 and \
                    self.page.locator(homepage.xpath_accept_english).is_visible():
                self.clickButton(homepage.xpath_accept_english)
                logger.info("✅ English cookie button clicked.")
            elif self.page.locator(homepage.xpath_accept_arabic).count() > 0 and \
                    self.page.locator(homepage.xpath_accept_arabic).is_visible():
                self.clickButton(homepage.xpath_accept_arabic)
                logger.info("✅ Arabic cookie button clicked.")
            else:
                logger.warning("⚠️ No cookie accept button found.")
        except Exception as e:
            logger.error(f"❌ Failed to handle cookie popup: {e}")


