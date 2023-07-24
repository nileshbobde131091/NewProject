import pytest
from docutils.parsers import null
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser()
    lockedUser = ReadConfig.getLockedUser()
    password = ReadConfig.getPassword()

    def test_UserAbleToLoginWithAValidUsernameAndValidPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Swag Labs":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS1.png")
            self.driver.close()
            assert False

    def test_ErorMessageIsDisplayedForLockedUser(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setLockedUserName(self.lockedUser)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        if error_message=="Epic sadface: Sorry, this user has been locked out.":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS2.png")
            self.driver.close()
            assert False


    def test_ErorMessageIsDisplayedWhenClickingTheEnterButtonWithoutAddingTheUsernameAndPassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        if error_message=="Epic sadface: Username is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS3.png")
            self.driver.close()
            assert False

    def test_ErorMessageIsRemovedWhenclickingtheCrossSignXOftheErrorMessageOnTheLoginPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        try:
            assert (error_message == "Epic sadface: Username is required")
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_homePageTitle.png")
            raise (Exception("Additional info. %s" % e))

        self.lp.clickOnCloseButtonOfErrorMessage()
        try:
            error_message_2 = self.lp.getErrorMessage()
            assert (error_message_2 == null )
            self.driver.close()
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS4.png")
            self.driver.close()
            raise (Exception("Additional info. %s" % e))


    def test_ErorMessageEpicsadfacePasswordisrequiredIsDisplayedAfterClickingTheEnterButtonWithoutAddingThePassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        if error_message=="Epic sadface: Password is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS5.png")
            self.driver.close()
            assert False


    def test_ErorMessageEpicsadfaceUsernameisrequiredIsDisplayedAfterClickingTheEnterButtonWithoutAddingTheUsername(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        if error_message=="Epic sadface: Username is required":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_SS6.png")
            self.driver.close()
            assert False



