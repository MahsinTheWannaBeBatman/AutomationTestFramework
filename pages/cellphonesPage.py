from selenium.webdriver.common.by import By


class CellphonesPage:

    def __init__(self, driver):
        self.driver = driver

        self.nokia_lumia_1020_css_selector = ".item-box:nth-child(1) img"

    def click_nokia_lumia_1020(self):
        self.driver.find_element(By.CSS_SELECTOR, self.nokia_lumia_1020_css_selector).click()
