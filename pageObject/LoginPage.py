from selenium.webdriver.common.by import By


class SauceDemo_Login:
    Text_Username_XPATH = (By.XPATH,"//input[@id='user-name']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='password']")
    Click_Login_XPATH = (By.XPATH,"//input[@id='login-button']")
    Click_Menu_XPATH = (By.XPATH,"//button[@id='react-burger-menu-btn']")
    Click_Logout_XPATH = (By.XPATH,"//a[@id='logout_sidebar_link']")


    def __init__(self,driver):
        self.driver = driver


    def Enter_Username(self,username):
        self.driver.find_element(*SauceDemo_Login.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*SauceDemo_Login.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*SauceDemo_Login.Click_Login_XPATH).click()

    def Click_Menu(self):
        self.driver.find_element(*SauceDemo_Login.Click_Menu_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*SauceDemo_Login.Click_Logout_XPATH).click()

    def Login_status(self):
        try:
            self.driver.find_element(*SauceDemo_Login.Click_Menu_XPATH)
            return True
        except:
            return False
