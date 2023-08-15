

# from pageObject.AddtoCart import Add_Cart
# from pageObject.LoginPage import SauceDemo_Login
# from utilities.Logger import LogGenerator
# from utilities.ReadConfig import Readconfig


# class Test_Login:
#     Username = Readconfig.GetUserName()
#     Password = Readconfig.GetPassword()

#     log = LogGenerator.loggen()

#     def test_AddtoCart_004(self,setup):
#         self.log.info("Test Case test_AddtoCart_004 is started")
#         self.log.info("opening browser")
#         self.driver = setup
#         self.lp = SauceDemo_Login(self.driver)
#         self.log.info("Entering Username" + self.Username)
#         self.lp.Enter_Username(self.Username)
#         self.log.info("Entering Password :" + self.Password)
#         self.lp.Enter_Password(self.Password)
#         self.driver.implicitly_wait(4)
#         self.log.info("clicking in login button")
#         self.lp.Click_Login()
#         # self.ac = Add_Cart(self.driver)
#         # self.log.info("Click on add to cart")
#         # self.ac.Click_AddtoCart()
#         # self.log.info("add jacket")
#         # self.ac.Click_AddJacket()
#         # self.log.info("go to cart")
#         # self.ac.Click_Cart()
#         # self.log.info("click on checkout")
#         # self.ac.Click_Final()
#         # if self.ac.Checkout_status() == True:
#         #     self.log.info("Taking screenshot")
#         #     self.driver.save_screenshot("D:\\Python Project\\sauceDemo\\Screenshots\\test_AddtoCart_004_pass.png")
#         #     assert True
#         #     self.log.info("test is passed")
#         #
#         # else:
#         #     self.driver.save_screenshot("D:\\Python Project\\sauceDemo\\Screenshots\\test_AddtoCart_004_fail.png")
#         #     self.log.info("test is failed")
#         #     assert False
#         # self.log.info("test is completed")




