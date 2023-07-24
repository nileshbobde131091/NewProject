from docutils.parsers import null

from pageObjects.CartPage import CartPage
from pageObjects.CheckoutPage import Checkout
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Checkout:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser()
    lockedUser = ReadConfig.getLockedUser()
    password = ReadConfig.getPassword()

    def loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.checkItemsInCartAndMakeCartPageIsEmpty()
        self.cp.addItemIntoTheCart()
        self.cp.clickOnAddToCartIcon()
        self.cp.clickOnCheckoutButtonOnCartPage()

    def test_FirstNameLastNameZipCodeCancelButtonAndContinueButtonAreDisplayedOnTheCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        if self.chp.firstNameTextFieldOnCheckoutPageIsDisplayed() and self.chp.lastNameTextFieldOnCheckoutPageIsDisplayed() and self.chp.zipCodeTextFieldOnCheckoutPageIsDisplayed() and self.chp.cancelButtonOnCheckoutPageIsDisplayed() and self.chp.continueButtonOnCheckoutPageIsDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS1.png")
            self.driver.close()
            assert False


    def test_ErrorMessageIsDisplayedWhenUserClickOnContinueButtonWithoutEnteringDataIntoFirstNameLastNameZipCodeOnTheCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.clickOnContinueButtonOnCheckoutPage()
        error_message = self.chp.getErrorMessageOnCheckoutPage()
        if error_message == "Error: First Name is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS2.png")
            self.driver.close()
            assert False

    def test_ErrorMessageIsDisplayedWhenUserClickOnContinueButtonWithoutEnteringDataIntoFirstNameOnTheCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.setLastName("Bobde")
        self.chp.setZipCode("ZP1111")
        self.chp.clickOnContinueButtonOnCheckoutPage()
        error_message = self.chp.getErrorMessageOnCheckoutPage()
        if error_message == "Error: First Name is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS3.png")
            self.driver.close()
            assert False

    def test_ErrorMessageIsDisplayedWhenUserClickOnContinueButtonWithoutEnteringDataIntoLastNameOnTheCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.setFirstName("Nilesh")
        self.chp.setZipCode("ZP1111")
        self.chp.clickOnContinueButtonOnCheckoutPage()
        error_message = self.chp.getErrorMessageOnCheckoutPage()
        if error_message == "Error: Last Name is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS4.png")
            self.driver.close()
            assert False

    def test_ErrorMessageIsDisplayedWhenUserClickOnContinueButtonWithoutEnteringDataIntoZipCodeOnTheCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.setFirstName("Nilesh")
        self.chp.setLastName("Bobde")
        self.chp.clickOnContinueButtonOnCheckoutPage()
        error_message = self.chp.getErrorMessageOnCheckoutPage()
        if error_message == "Error: Postal Code is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS5.png")
            self.driver.close()
            assert False

    def test_ErrorMessageIsRemovedWhenClickingCrossSignXOfErrorMessageOnCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.clickOnContinueButtonOnCheckoutPage()
        error_message = self.chp.getErrorMessageOnCheckoutPage()
        if error_message == "Error: First Name is required":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_for_error_message_SS6.png")
            assert False
        self.chp.clickOnCloseButtonOfErrorMessageOnCheckoutPage()
        try:
            error_message_2 = self.lp.getErrorMessage()
            assert (error_message_2 == null )
            self.driver.close()
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS6.png")
            self.driver.close()
            raise (Exception("Additional info. %s" % e))

    def test_userNavigatesToCartPageWhenClickingOnCancelButtonOnTheCheckoutPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.clickOnCancelButtonOnCheckoutPage()
        if self.cp.firstItemsOnCartIsDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS7.png")
            self.driver.close()
            assert False



    def test_userNavigatesToCheckoutOverviewPageWhenClickingOnContinueButtonOnTheCheckoutPageWithAddDataOnAllTheTextFields(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        self.chp.setFirstName("Nilesh")
        self.chp.setLastName("Bobde")
        self.chp.setZipCode("ZP1111")
        self.chp.clickOnContinueButtonOnCheckoutPage()
        if self.chp.checkoutOverviewPageIsDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS8.png")
            self.driver.close()
            assert False

    def test_RespectivePlaceholderNamesAsFirstNameLastNameAndZipCodeAreDisplayedForFirstNameLastNameAndZipCodeRespectively(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCartAndNavigateToCheckoutPage()
        self.chp = Checkout(self.driver)
        place_holder_first_name = self.chp.placeHolderValueForFirstName()
        place_holder_last_name = self.chp.placeHolderValueForLastName()
        place_holder_zip_code = self.chp.placeHolderValueForZipCode()
        if place_holder_first_name == "First Name" and place_holder_last_name == "Last Name" and place_holder_zip_code == "Zip/Postal Code":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_checkout_SS9.png")
            self.driver.close()
            assert False