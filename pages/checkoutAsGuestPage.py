from selenium.webdriver.common.by import By


class CheckoutAsGuest:

    def __init__(self, driver):
        self.driver = driver

        self.checkout_as_guest_button_css_selector = ".checkout-as-guest-button"

    def click_checkout_as_guest_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkout_as_guest_button_css_selector).click()
