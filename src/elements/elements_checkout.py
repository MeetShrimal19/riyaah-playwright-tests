import time


class Checkout_elements:
    xpath_mobilenumber = "//input[@aria-label='Text input with dropdown button']"
    xpath_proceed = "//button[normalize-space()='Proceed']"
    xpath_OTP1 = "//input[@aria-label='Please enter OTP character 1']"
    xpath_OTP2 = "//input[@aria-label='Please enter OTP character 2']"
    xpath_OTP3 = "//input[@aria-label='Please enter OTP character 3']"
    xpath_OTP4 = "//input[@aria-label='Please enter OTP character 4']"
    xpath_OTP5 = "//input[@aria-label='Please enter OTP character 5']"
    xpath_OTP6 = "//input[@aria-label='Please enter OTP character 6']"
    xpath_next="//button[normalize-space()='Next']"
    xpath_COD="//body//div[@role='dialog']//div//div[2]//div[3]//label[1]//span[1]"
    xpath_confirmandpay="//button[normalize-space()='Confirm & Pay']"
    xpath_Onlinepayment="//body//div[@role='dialog']//div//div[2]//div[2]//label[1]//span[1]"
    xpath_holdername="//input[@id='holderName']"
    xpath_cardnumber="//input[@id='number']"
    xpath_month="//input[@id='expmonth']"
    xpath_year="//input[@id='expyear']"
    xpath_CVV="//input[@id='cvv']"
    xpath_paynow_online="//button[@id='payBtn']"
    xpath_backtohome="//button[normalize-space()='Back to home']"
    xpath_order_processed="//h1[normalize-space()='Order Processed']"