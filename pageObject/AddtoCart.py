from selenium.webdriver.common.by import By


class Add_Cart:
    Click_Backpack_CSS = (By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack")
    Click_Jacket_CSS = (By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket")
    Click_Cart_CSS = (By.CSS_SELECTOR,".shopping_cart_link")
    Click_Checkout_XPATH = (By.XPATH,"//button[@id='checkout']")


    def __init__(self,driver):
        self.driver = driver


    def Backpack(self):
        self.driver.find_element(self.Click_Backpack_CSS).click()

    def Jacket(self):
        self.driver.find_element(self.Click_Jacket_CSS).click()

    def Go_Cart(self):
        self.driver.find_element(self.Click_Cart_CSS).click()

    def Checkout(self):
        self.driver.find_element(self.Click_Checkout_XPATH).click()

    def Check_status(self):
        self.



