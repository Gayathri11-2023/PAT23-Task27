import pytest

from Data import data
from Locators import locator

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class TestLogin:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        yield
        self.driver.quit()

    def test_login(self, boot):

        try:
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()
            for row in range(2, data.WebData().row_count()+1):
                username = data.WebData().read_data(row, 2)
                password = data.WebData().read_data(row, 3)
                locator.WebLocators().enter_text(self.driver, locator.WebLocators().usernameLocator, username)
                locator.WebLocators().enter_text(self.driver, locator.WebLocators().passwordLocator, password)
                locator.WebLocators().click_button(self.driver, locator.WebLocators().buttonLocator)
                if self.driver.current_url == data.WebData().dashboardURL:
                    print("successfully logged in")
                    locator.WebLocators().click_button(self.driver, locator.WebLocators().dropdownLocator)
                    locator.WebLocators().click_button(self.driver, locator.WebLocators().logoutLocator)
                    data.WebData().write_data(row, 7, "PASSED")
                else:
                    print("Login Unsuccessful")
                    data.WebData().write_data(row, 7, "FAILED")
        except NoSuchElementException as e:
            print("Error!")


























