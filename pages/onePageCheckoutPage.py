from selenium.webdriver.common.by import By


class OnePageCheckout:

    def __init__(self, driver):
        self.driver = driver

        self.billing_new_address_first_name_id = "BillingNewAddress_FirstName"
        self.billing_new_address_last_name_id = "BillingNewAddress_LastName"
        self.billing_new_address_email_id = "BillingNewAddress_Email"
        self.billing_new_address_company_id = "BillingNewAddress_Company"
        self.billing_new_address_country_id = "BillingNewAddress_CountryId"
        self.billing_new_address_state_province_id = "BillingNewAddress_StateProvinceId"
        self.billing_new_address_city_id = "BillingNewAddress_City"
        self.billing_new_address_address_line_1_id = "BillingNewAddress_Address1"
        self.billing_new_address_address_line_2_id = "BillingNewAddress_Address2"
        self.billing_new_address_zip_postal_code_id = "BillingNewAddress_ZipPostalCode"
        self.billing_new_address_phone_number_id = "BillingNewAddress_PhoneNumber"
        self.billing_new_address_fax_number_id = "BillingNewAddress_FaxNumber"
        self.continue_button_name = "save"
        self.shipping_method_id = "shippingoption_1"
        self.shipping_method_next_step_button_css = ".shipping-method-next-step-button"
        self.payment_method_id = "paymentmethod_1"
        self.payment_method_next_step_button_css = ".payment-method-next-step-button"
        self.card_type_id = "CreditCardType"
        self.cardholder_name_id = "CardholderName"
        self.card_number_id = "CardNumber"
        self.card_expiry_month_id = "ExpireMonth"
        self.card_code_id = "CardCode"
        self.payment_info_next_step_button_css = ".payment-info-next-step-button"
        self.confirm_order_next_step_button_css = ".confirm-order-next-step-button"

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.billing_new_address_first_name_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.billing_new_address_last_name_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_last_name_id).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.billing_new_address_email_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_email_id).send_keys(email)

    def enter_company_name(self, company):
        self.driver.find_element(By.ID, self.billing_new_address_company_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_company_id).send_keys(company)

    def select_country(self):
        self.driver.find_element(By.ID, self.billing_new_address_country_id).click()
        dropdown = self.driver.find_element(By.ID, self.billing_new_address_country_id)
        dropdown.find_element(By.XPATH, "//option[. = 'Bangladesh']").click()
        self.driver.find_element(By.ID, self.billing_new_address_address_line_1_id).click()

    def select_state_province(self):
        self.driver.find_element(By.ID, self.billing_new_address_state_province_id).click()
        dropdown = self.driver.find_element(By.ID, self.billing_new_address_state_province_id)
        dropdown.find_element(By.XPATH, "//option[. = 'ঢাকা']").click()

    def enter_city_name(self, city):
        self.driver.find_element(By.ID, self.billing_new_address_city_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_city_id).send_keys(city)

    def enter_address_line_1(self, address1):
        self.driver.find_element(By.ID, self.billing_new_address_address_line_1_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_address_line_1_id).send_keys(address1)

    def enter_address_line_2(self, address2):
        self.driver.find_element(By.ID, self.billing_new_address_address_line_2_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_address_line_2_id).send_keys(address2)

    def enter_zip_postal_code(self, postal_code):
        self.driver.find_element(By.ID, self.billing_new_address_zip_postal_code_id ).click()
        self.driver.find_element(By.ID, self.billing_new_address_zip_postal_code_id ).send_keys(postal_code)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.ID, self.billing_new_address_phone_number_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_phone_number_id).send_keys(phone_number)

    def enter_fax_number(self, fax_number):
        self.driver.find_element(By.ID, self.billing_new_address_fax_number_id).click()
        self.driver.find_element(By.ID, self.billing_new_address_fax_number_id).send_keys(fax_number)

    def click_continue_button(self):
        self.driver.find_element(By.NAME, self.continue_button_name).click()

    def select_shipping_method(self):
        self.driver.find_element(By.ID, self.shipping_method_id).click()
        self.driver.find_element(By.CSS_SELECTOR, self.shipping_method_next_step_button_css).click()

    def select_payment_method(self):
        self.driver.find_element(By.ID, self.payment_method_id).click()
        self.driver.find_element(By.CSS_SELECTOR, self.payment_method_next_step_button_css).click()

    def select_credit_cart_type(self):
        self.driver.find_element(By.ID, self.card_type_id).click()

    def enter_cardholder_name(self, name):
        self.driver.find_element(By.ID, self.cardholder_name_id).click()
        self.driver.find_element(By.ID, self.cardholder_name_id).send_keys(name)

    def enter_card_number(self, card_number):
        self.driver.find_element(By.ID, self.card_number_id).click()
        self.driver.find_element(By.ID, self.card_number_id).send_keys(card_number)

    def enter_expiry_date(self):
        self.driver.find_element(By.ID, self.card_expiry_month_id).click()
        dropdown = self.driver.find_element(By.ID, self.card_expiry_month_id)
        dropdown.find_element(By.XPATH, "//option[. = '05']").click()

    def enter_card_code(self, card_code):
        self.driver.find_element(By.ID, self.card_code_id).click()
        self.driver.find_element(By.ID, self.card_code_id ).send_keys(card_code)

    def click_next_step_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.payment_info_next_step_button_css).click()

    def click_confirm_oder_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.confirm_order_next_step_button_css).click()


