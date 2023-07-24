class Checkout:
    textbox_first_name_id = "first-name"
    textbox_last_name_id = "last-name"
    textbox_postal_code_id = "postal-code"
    continue_button_on_checkout_page_id = "continue"
    cancel_button_on_checkout_page_id = "cancel"
    error_message_on_checkout_page_xpath = "//*[@data-test='error']"
    close_button_of_error_message_checkout_page_xpath = "//*[@class='error-button']"
    checkout_overview_page_title_xpath = "//*[text()='Checkout: Overview']"


    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstname):
        self.driver.find_element_by_id(self.textbox_first_name_id).clear()
        self.driver.find_element_by_id(self.textbox_first_name_id).send_keys(firstname)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.textbox_last_name_id).clear()
        self.driver.find_element_by_id(self.textbox_last_name_id).send_keys(lastName)

    def setZipCode(self , zipCode):
        self.driver.find_element_by_id(self.textbox_postal_code_id).clear()
        self.driver.find_element_by_id(self.textbox_postal_code_id).send_keys(zipCode)

    def firstNameTextFieldOnCheckoutPageIsDisplayed(self):
        return self.driver.find_element_by_id(self.textbox_first_name_id).is_displayed()

    def lastNameTextFieldOnCheckoutPageIsDisplayed(self):
        return self.driver.find_element_by_id(self.textbox_last_name_id).is_displayed()

    def zipCodeTextFieldOnCheckoutPageIsDisplayed(self):
        return self.driver.find_element_by_id(self.textbox_postal_code_id).is_displayed()

    def continueButtonOnCheckoutPageIsDisplayed(self):
        return self.driver.find_element_by_id(self.continue_button_on_checkout_page_id).is_displayed()

    def cancelButtonOnCheckoutPageIsDisplayed(self):
        return self.driver.find_element_by_id(self.cancel_button_on_checkout_page_id).is_displayed()

    def clickOnContinueButtonOnCheckoutPage(self):
        self.driver.find_element_by_id(self.cancel_button_on_checkout_page_id).click()

    def getErrorMessageOnCheckoutPage(self):
        errorMessage=self.driver.find_element_by_xpath(self.error_message_on_checkout_page_xpath).getText()
        return errorMessage

    def clickOnCloseButtonOfErrorMessageOnCheckoutPage(self):
        self.driver.find_element_by_xpath(self.close_button_of_error_message_checkout_page_xpath).click()

    def clickOnCancelButtonOnCheckoutPage(self):
        self.driver.find_element_by_id(self.cancel_button_on_checkout_page_id).click()

    def checkoutOverviewPageIsDisplayed(self):
        return self.driver.find_element_by_xpath(self.checkout_overview_page_title_xpath).is_displayed()

    def placeHolderValueForFirstName(self):
        first_name = self.driver.find_element_by_id(self.textbox_first_name_id)
        first_name_placeholder_value = first_name.getAttribute("placeholder")
        return first_name_placeholder_value

    def placeHolderValueForLastName(self):
        last_name = self.driver.find_element_by_id(self.textbox_last_name_id)
        last_name_placeholder_value = last_name.getAttribute("placeholder")
        return last_name_placeholder_value

    def placeHolderValueForZipCode(self):
        postal_code = self.driver.find_element_by_id(self.textbox_postal_code_id)
        postal_code_placeholder_value = postal_code.getAttribute("placeholder")
        return postal_code_placeholder_value