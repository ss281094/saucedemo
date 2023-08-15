import time

import allure
from allure_commons.types import AttachmentType

from pageObject.LoginPage import SauceDemo_Login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()

    log = LogGenerator.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://www.saucedemo.com/")
    @allure.title("Page Title Test Case")

    def test_page_title_001(self,setup):
        self.log.info("Test Case test_page_title_001 is started ")
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Page title is " + self.driver.title)
        if self.driver.title == "Swag Labs":
            self.log.info("Taking Screenshot")
            time.sleep((2))
            self.driver.save_screenshot("D:\\Python Project\\sauceDemo\\Screenshots\\test_page_title_001_pass.png")
            self.log.info("Test Case test_page_title_001 is Passed ")
            assert True

        else:
            self.driver.save_screenshot("D:\\Python Project\\sauceDemo\\Screenshots\\test_page_title_001_fail.png")
            self.log.info("Test Case test_page_title_001 is Failed")
            assert False
        self.log.info("Test Case test_page_title_001 is commpleted")

    def test_login_002(self,setup):
        self.log.info("Test Case test_login_002 is started")
        self.log.info("opening browser")
        self.driver = setup
        self.lp = SauceDemo_Login(self.driver)
        self.log.info("Entering Username" + self.Username)
        self.lp.Enter_Username(self.Username)
        self.log.info("Entering Password :" + self.Password)
        self.lp.Enter_Password(self.Password)
        self.driver.implicitly_wait(4)
        self.log.info("clicking in login button")
        self.lp.Click_Login()
        self.log.info("checking login status")
        if self.lp.Login_status() == True:
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("D:\\Python Project\\sauceDemo\\Screenshots\\test_login_002_pass.png")
            self.log.info("click on menu")
            self.lp.Click_Menu()
            self.log.info("click on logout button")
            self.lp.Click_Logout()
            self.log.info("Test Case test_login_002 is passed")
            assert True

        else:
            self.driver.save_screenshot("D:\\Python Project\\sauceDemo\\Screenshots\\test_login_002_fail.png")
            self.log.info("Test Case test_login_002 is Failed")
            assert False

        self.log.info("Test Case test_login_002 is completed")


        # -v -s --html = Reports\report.html --alluredir = "D:\Python Project\sauceDemo\Allure-result"