import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import names
import random

from pages.cartPage import CartPage
from pages.cellphonesPage import CellphonesPage
from pages.checkoutAsGuestPage import CheckoutAsGuest
from pages.landingPage import LandingPage
from pages.nokiaLumia1020Page import NokiaLumia1020Page
from pages.onePageCheckoutPage import OnePageCheckout


class TestPurchase:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome("E:/Study Related/Selenium/NOPCommerce/Tests/chromedriver.exe", options=options)

    def test_purchase(self):
        driver = self.driver
        driver.get("https://training.nop-station.com/")
        driver.maximize_window()

        landing = LandingPage(driver)
        time.sleep(3)
        landing.click_cellphones_link()

        cellphone = CellphonesPage(driver)
        cellphone.click_nokia_lumia_1020()

        nokia = NokiaLumia1020Page(driver)
        nokia.enter_quantity(2)
        nokia.click_add_to_cart_button()
        time.sleep(2)
        nokia.click_shopping_cart_link()

        cart = CartPage(driver)
        cart.select_terms_of_service()
        cart.click_checkout_button()

        guest = CheckoutAsGuest(driver)
        guest.click_checkout_as_guest_button()

        checkout = OnePageCheckout(driver)
        first_name = names.get_first_name()
        checkout.enter_first_name(first_name)
        checkout.enter_last_name(names.get_last_name())
        checkout.enter_email(first_name + "@gmail.com")
        checkout.enter_company_name(first_name + " Ltd.")
        checkout.select_country()
        time.sleep(5)
        checkout.select_state_province()
        checkout.enter_city_name("Dhaka")
        checkout.enter_address_line_1("qwerty")
        checkout.enter_address_line_2("poiuy")
        checkout.enter_zip_postal_code(random.randint(1200, 1299))
        checkout.enter_phone_number("+880" + str(random.randint(1000000000, 9999999999)))
        checkout.enter_fax_number("+8802" + str(random.randint(1000000, 9999999)))
        checkout.click_continue_button()
        time.sleep(2)
        checkout.select_shipping_method()
        time.sleep(2)
        checkout.select_payment_method()
        time.sleep(2)
        checkout.select_credit_cart_type()
        checkout.enter_cardholder_name(first_name)
        checkout.enter_card_number("4000 0200 0000 0000")
        checkout.enter_expiry_date()
        checkout.enter_card_code(random.randint(1000, 9999))
        time.sleep(2)
        checkout.click_next_step_button()
        time.sleep(2)
        checkout.click_confirm_oder_button()

        time.sleep(1)
        element = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div/div[1]/strong")
        assert element.text == 'Your order has been successfully processed!'

        # self.driver.find_element(By.CSS_SELECTOR, ".order-completed-continue-button").click()

    def teardown_method(self):
        self.driver.quit()


# if __name__ == '__main__':
#     t = TestPurchase()
#     t.setup_method()
#     t.test_purchase()
#     # t.teardown_method()
