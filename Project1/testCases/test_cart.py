from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Cart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser()
    lockedUser = ReadConfig.getLockedUser()
    password = ReadConfig.getPassword()

    def loginTotheSwagPortalAndAddTheProductInTheCart(self):
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

    def test_userIsAbleToAddItemsIntoTheCart(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCart()
        self.cp = CartPage(self.driver)
        if self.cp.firstItemsOnCartIsDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS1.png")
            self.driver.close()
            assert False

    def test_userIsAbleToRemoveItemsFromTheCart(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCart()
        self.cp = CartPage(self.driver)
        self.cp.removeFirstItemFromTheCart()
        empty_cart = self.cp.firstItemsOnCartIsDisplayed()
        if empty_cart == False:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS2.png")
            self.driver.close()
            assert False

    def test_productNameIsClickableAndUserNavigatesToProductDetailPageWhenClickingProductNameOnTheCartPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCart()
        self.cp = CartPage(self.driver)
        self.cp.clickOnNameOfTheFirstProduct()
        if self.cp.pdpPageOfFirstItemsIsDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS3.png")
            self.driver.close()
            assert False

    def test_userNavigatesToCheckoutPageWhenClickingCheckoutButtonOnTheCartPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCart()
        self.cp = CartPage(self.driver)
        self.cp.clickOnCheckoutButtonOnCartPage()
        if self.cp.checkoutPageDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS4.png")
            self.driver.close()
            assert False

    def test_userNavigatesToHomepagePageWhenClickingContinueShoppingButtonOnCartPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCart()
        self.cp = CartPage(self.driver)
        self.cp.clickOnContinueShoppingButtonOnCartPage()
        if self.cp.homePlpPageDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS5.png")
            self.driver.close()
            assert False

    def test_ContinueShopingAndCheckoutButtonsAreDisplayedOnEmptyCartPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.checkItemsInCartAndMakeCartPageIsEmpty()
        if self.cp.checkoutButtonIsDisplayed() and self.cp.continueShoppingButtonDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS6.png")
            self.driver.close()
            assert False


    def test_ContinueShopingAndCheckoutButtonsAreDisplayedOnCartPage(self, setup):
        self.driver = setup
        self.loginTotheSwagPortalAndAddTheProductInTheCart()
        self.cp = CartPage(self.driver)
        if self.cp.checkoutButtonIsDisplayed() and self.cp.continueShoppingButtonDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS7.png")
            self.driver.close()
            assert False

    def test_userNavigatesToCheckoutPageWhenClickingCheckoutButtonOnTheEmptyCartPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.checkItemsInCartAndMakeCartPageIsEmpty()
        self.cp.clickOnAddToCartIcon()
        self.cp.clickOnCheckoutButtonOnCartPage()
        if self.cp.checkoutPageDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS8.png")
            self.driver.close()
            assert False

    def test_userNavigatesToHomepagePageWhenClickingContinueShoppingButtonOnEmptyCartPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.checkItemsInCartAndMakeCartPageIsEmpty()
        self.cp.clickOnAddToCartIcon()
        self.cp.clickOnContinueShoppingButtonOnCartPage()
        if self.cp.homePlpPageDisplayed():
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cart_SS9.png")
            self.driver.close()
            assert False
