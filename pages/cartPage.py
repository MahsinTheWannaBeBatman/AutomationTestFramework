from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

        self.terms_of_service_id = "termsofservice"
        self.checkout_button_id = "checkout"

    def select_terms_of_service(self):
        self.driver.find_element(By.ID, self.terms_of_service_id).click()

    def click_checkout_button(self):
        self.driver.find_element(By.ID, self.checkout_button_id).click()
