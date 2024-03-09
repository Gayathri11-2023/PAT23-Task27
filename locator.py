from selenium.webdriver.common.by import By

class WebLocators:
    """
      This class is used to contain all the elements locating data present in the Html of OrangeHRM
    """
    def __init__(self):
        self.usernameLocator = "//input[@name='username']"
        self.passwordLocator = '//input[@name="password"]'
        self.buttonLocator = "//button[@type='submit']"
        self.dropdownLocator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i'
        self.logoutLocator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def enter_text(self, driver, locator, textValue):
        element = driver.find_element(by=By.XPATH, value=locator)
        element.clear()
        element.send_keys(textValue)

    def click_button(self, driver, locator):
        driver.find_element(by=By.XPATH, value=locator).click()


