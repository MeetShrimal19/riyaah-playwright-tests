from pages.Cart import Cart
def test_cart_wishlist(browser_page):
    cart_wishlit = Cart(browser_page)
    cart_wishlit.close_clevertap_popup()
    cart_wishlit.MovetoWishlist()

    # cart_wishlit.CartWishlist()

