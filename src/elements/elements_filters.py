class Filter_elements:
    xpath_Brand_perfumes="(//div[@class='col-md-12'])[1]"
    xpath_Abercrombiebrand_tick="//label[contains(@for,'brand_nameAbercrombie & Fitch')]"
    xpath_Abercrombiebrand_count="//div[@data-orientation='vertical']//div[2]//div[1]//p[1]"
    # xpath_productcard_Abercrombie="//body/div[contains(@data-overlay-container,'true')]/div/main/div/div/div/div[3]/div[1]/div[1]"
    xpath_productcard_Abercrombie = "//div[contains(@class, 'productCard')]:visible"
