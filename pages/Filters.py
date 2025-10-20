import time

from pages.BasePage import Basepage
from src.elements.elements_filters import Filter_elements
from src.elements.elements_search import SearchElements
from src.elements.elements_homepage import homepage

class Filters(Basepage):
    def Searchfilter(self, product_name):
        self.clickButton(homepage.xpath_accept)
        self.clickButton(SearchElements.xpath_searchbar)
        self.page.wait_for_selector(SearchElements.xpath_searchbar, state="visible", timeout=30000)
        self.typevalue(SearchElements.xpath_searchbar, product_name)
        self.press_key(SearchElements.xpath_searchbar, "Enter")
        self.page.wait_for_load_state("networkidle")
        brand_filter = self.page.get_by_text("Brand", exact=True)
        brand_filter.wait_for(state="visible", timeout=5000)
        brand_filter.click()
        self.waitForElementVisible(Filter_elements.xpath_Abercrombiebrand_tick, timeout=6000)
        self.clickButton(Filter_elements.xpath_Abercrombiebrand_tick)
        self.page.wait_for_load_state("networkidle")
        brand_count_locator =   self.page.locator(Filter_elements.xpath_Abercrombiebrand_count)
        brand_count_text = brand_count_locator.inner_text().strip("() ")
        expected_count = int(brand_count_text)
        print(f"🧾 Brand filter shows {expected_count} for Abercrombie brand")

        # Step 6: Wait for visible products to appear
        print(f"⏳ Waiting for {expected_count} product cards to load on the page...")
        self.page.wait_for_selector(
            "//div[contains(@class,'productCard') and .//h6[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'abercrombie')]]",
            state="visible",
            timeout=30000
        )

        product_cards = self.page.locator(
            "//div[contains(@class,'productCard') and .//h6[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'abercrombie')]]"
        )
        actual_count = product_cards.count()
        print(f"✅ Found {actual_count} visible product cards after applying brand filter.")

        # Step 8: Assertion
        assert actual_count == expected_count, (
            f"❌ Mismatch: Expected {expected_count} but found {actual_count} visible products."
        )

        print("🎉 Brand filter validation successful!")

        # Step 9: Optional wait for manual observation (can remove later)
        time.sleep(3)