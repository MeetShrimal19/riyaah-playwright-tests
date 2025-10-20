from pages.Filters import Filters

def test_search_filter(browser_page):
    testfilter = Filters(browser_page)
    testfilter.Searchfilter("perfumes")