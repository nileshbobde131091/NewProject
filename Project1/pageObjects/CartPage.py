class CartPage:
    button_add_to_cart_for_product_one_id = "add-to-cart-sauce-labs-backpack"
    button_add_to_cart_for_product_two_id = "add-to-cart-sauce-labs-bolt-t-shirt"
    cart_icon_xpath = "//*[@class='shopping_cart_link']"
    items_in_cart_number_on_plp_page_xpath = "//*[@class='shopping_cart_badge']"
    first_item_on_cart_page_xpath = "(//*[@class='cart_item'])[1]"
    button_remove_first_item_on_cart_page_id = "remove-sauce-labs-backpack"
    button_remove_second_item_on_cart_page_id = "remove-sauce-labs-bolt-t-shirt"
    name_link_of_first_product_xpath = "//*[text()='Sauce Labs Backpack']"
    item_on_the_pdp_page_id = "inventory_item_container"
    checkout_button_on_cart_page_id = "checkout"
    continue_shopping_button_on_cart_page_id = "continue-shopping"
    checkout_page_id = "checkout_info_container"
    plp_page_id = "inventory_container"

    def __init__(self, driver):
        self.driver = driver

    def addItemIntoTheCart(self):
        self.driver.find_element_by_id(self.button_add_to_cart_for_product_one_id).click()

    # def addTwoItemsIntoTheCart(self):
    #     self.driver.find_element_by_id(self.button_add_to_cart_for_product_one_id).click()
    #     self.driver.find_element_by_id(self.button_add_to_cart_for_product_two_id).click()

    def clickOnAddToCartIcon(self):
        self.driver.find_element_by_xpath(self.cart_icon_xpath).click()

    def firstItemsOnCartIsDisplayed(self):
        return self.driver.find_element_by_xpath(self.first_item_on_cart_page_xpath).is_displayed()

    def removeFirstItemFromTheCart(self):
        self.driver.find_element_by_id(self.button_remove_first_item_on_cart_page_id).click()

    def removeSecondItemFromTheCart(self):
        self.driver.find_element_by_id(self.button_remove_second_item_on_cart_page_id).click()

    def checkItemsInCartAndMakeCartPageIsEmpty(self):
        try:
            items_in_cart_page = self.driver.find_element_by_xpath(self.items_in_cart_number_on_plp_page_xpath).text
            if items_in_cart_page == 0:
                self.clickOnAddToCartIcon()
            else:
                self.clickOnAddToCartIcon()
                self.removeFirstItemFromTheCart()
                self.removeSecondItemFromTheCart()
                self.clickOnContinueShoppingButtonOnCartPage()
        except Exception as e:
            print(e)

    def clickOnNameOfTheFirstProduct(self):
        self.driver.find_element_by_xpath(self.name_link_of_first_product_xpath).click()

    def pdpPageOfFirstItemsIsDisplayed(self):
        return self.driver.find_element_by_id(self.item_on_the_pdp_page_id).is_displayed()

    def clickOnCheckoutButtonOnCartPage(self):
        try:
            if self.driver.find_element_by_id(self.checkout_button_on_cart_page_id).is_displayed():
                self.driver.find_element_by_id(self.checkout_button_on_cart_page_id).click()
        except Exception as e:
            print(e)

    def checkoutPageDisplayed(self):
        return self.driver.find_element_by_id(self.checkout_page_id).is_displayed()

    def clickOnContinueShoppingButtonOnCartPage(self):
        try:
            if self.driver.find_element_by_id(self.continue_shopping_button_on_cart_page_id).is_displayed():
                self.driver.find_element_by_id(self.continue_shopping_button_on_cart_page_id).click()
        except Exception as e:
            print(e)

    def homePlpPageDisplayed(self):
        return self.driver.find_element_by_id(self.plp_page_id).is_displayed()

    def checkoutButtonIsDisplayed(self):
        return self.driver.find_element_by_id(self.checkout_button_on_cart_page_id).is_displayed()

    def continueShoppingButtonDisplayed(self):
        return self.driver.find_element_by_id(self.continue_shopping_button_on_cart_page_id).is_displayed()