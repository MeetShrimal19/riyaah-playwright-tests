class CartElements:
    xpath_cart="//div[@class='relative']//img[@alt='cart']"
    xpath_checkout="//button[text()='Secure Checkout']"
    # xpath_securecheckout = "(//button[normalize-space()='Secure Checkout' and not(@disabled)])[last()]"
    # xpath_delete_item="//*[name()='path' and contains(@d,'M19 6v14c0')]"
    xpath_delete_item = "//*[name()='svg' and contains(@class, 'lucide-trash')]/ancestor::*[self::div or self::span][1]"
    xpath_movetowishlist="//button[normalize-space()='Move to wishlist']"
    xpath_yes_remove_item="//button[normalize-space()='Yes, remove']"
    xpath_empty_cart_text="//p[normalize-space()='You do not have any item']"
