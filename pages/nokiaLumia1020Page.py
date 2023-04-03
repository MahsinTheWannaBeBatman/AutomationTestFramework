from selenium.webdriver.common.by import By


class NokiaLumia1020Page:

    def __init__(self, driver):
        self.driver = driver

        self.nokia_lumia_1020_css_selector = ".item-box:nth-child(1) img"
        self.quantity_id = "product_enteredQuantity_20"
        self.add_to_cart_button_id = "add-to-cart-button-20"
        self.shopping_cart_link_text = "shopping cart"

    def enter_quantity(self, quantity):
        self.driver.find_element(By.ID, self.quantity_id).click()
        self.driver.find_element(By.ID, self.quantity_id).clear()
        self.driver.find_element(By.ID, self.quantity_id).send_keys(quantity)

    def click_add_to_cart_button(self):
        self.driver.find_element(By.ID, self.add_to_cart_button_id).click()

    def click_shopping_cart_link(self):
        self.driver.find_element(By.LINK_TEXT, self.shopping_cart_link_text).click()


