import time

from pages.search import SearchPage

def test_search(browser_page):
    page = browser_page
    search_page = SearchPage(page)

    # open site
    page.goto("https://web-uat.riyaah.com/en")
    page.wait_for_load_state("networkidle")

    # perform search

    search_page.close_clevertap_popup()
    search_page.click_searchbar("Perfume")

    assert "Perfume" in page.content()
