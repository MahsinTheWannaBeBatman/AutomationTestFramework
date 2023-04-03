from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LandingPage:

    def __init__(self, driver):
        self.driver = driver

        self.register_link_text = "Register"
        self.electronics_xpath = "/html/body/div[6]/div[2]/ul[1]/li[6]/a"
        self.cellphone_xpath = "/html/body/div[6]/div[2]/ul[1]/li[6]/ul/li[2]/a"
        self.cellphone_link_text = "Cell phones"

    def click_register_link(self):
        self.driver.find_element(By.LINK_TEXT, self.register_link_text).click()

    def click_cellphones_link(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH, self.electronics_xpath)
        a.move_to_element(m).perform()
        n = self.driver.find_element(By.XPATH, self.cellphone_xpath)
        a.move_to_element(n).click().perform()
        self.driver.find_element(By.LINK_TEXT, self.cellphone_link_text).click()
