import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import names
import random

from pages.landingPage import LandingPage
from pages.registerPage import RegisterPage


class TestRegister:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome("E:/Study Related/Selenium/NOPCommerce/Tests/chromedriver.exe", options=options)

    def test_register(self):
        driver = self.driver

        driver.get("https://training.nop-station.com/")
        driver.maximize_window()

        landing = LandingPage(driver)
        landing.click_register_link()

        register = RegisterPage(driver)
        register.select_gender(random.randint(0, 1))
        first_name = names.get_first_name()
        register.enter_first_name(first_name)
        register.enter_last_name(names.get_last_name())
        register.enter_dob()
        register.enter_email(first_name + "@gmail.com")
        register.enter_company(first_name + " Ltd.")
        register.select_newsletter(random.randint(0, 1))
        register.enter_password(first_name + "123")
        register.enter_confirm_password(first_name + "123")
        register.click_register_button()

        time.sleep(1)
        element = driver.find_element(By.CLASS_NAME, "result")
        assert element.text == 'Your registration completed'

        time.sleep(1)

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()


# if __name__ == '__main__':
#     t = TestRegister()
#     t.setup_method()
#     t.test_register()
#     t.teardown_method()
