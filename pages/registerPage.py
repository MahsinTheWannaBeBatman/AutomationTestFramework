from selenium.webdriver.common.by import By

class RegisterPage():

    def __init__(self, driver):
        self.driver = driver

        self.gender_male_id = "gender-male"
        self.gender_female_id = "gender-female"
        self.first_name_id = "FirstName"
        self.last_name_id = "LastName"
        self.date_of_birth_day_name = "DateOfBirthDay"
        self.date_of_birth_month_name = "DateOfBirthMonth"
        self.date_of_birth_year_name = "DateOfBirthYear"
        self.email_id = "Email"
        self.company_id = "Company"
        self.newsletter_id = "Newsletter"
        self.password_id = "Password"
        self.confirm_password_id = "ConfirmPassword"
        self.register_button_id = "register-button"
        self.confirmation_text_classname = "result"


    def select_gender(self, r):
        if r==0:
          self.driver.find_element(By.ID, self.gender_male_id).click()
        else:
          self.driver.find_element(By.ID, self.gender_female_id).click()
    
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).click()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)
        
    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).click()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def enter_dob(self):
        self.driver.find_element(By.NAME, self.date_of_birth_day_name).click()
        dropdown = self.driver.find_element(By.NAME, self.date_of_birth_day_name)
        dropdown.find_element(By.XPATH, "//option[. = '6']").click()
        self.driver.find_element(By.NAME, self.date_of_birth_month_name).click()
        dropdown = self.driver.find_element(By.NAME, self.date_of_birth_month_name)
        dropdown.find_element(By.XPATH, "//option[. = 'June']").click()
        self.driver.find_element(By.NAME, self.date_of_birth_year_name).click()
        dropdown = self.driver.find_element(By.NAME, self.date_of_birth_year_name)
        dropdown.find_element(By.XPATH, "//option[. = '1966']").click()
       
    def enter_email(self, email):
        self.driver.find_element(By.ID, "Email").click()
        self.driver.find_element(By.ID, "Email").send_keys(email)
        
    def enter_company(self, company):
        self.driver.find_element(By.ID, "Company").click()
        self.driver.find_element(By.ID, "Company").send_keys(company)

    def select_newsletter(self, r):
        if r==0:
          pass
        else:
          self.driver.find_element(By.ID, "Newsletter").click()
       
    def enter_password(self, password):
        self.driver.find_element(By.ID, "Password").click()
        self.driver.find_element(By.ID, "Password").send_keys(password)
       
    def enter_confirm_password(self, password):
        self.driver.find_element(By.ID, "ConfirmPassword").click()
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
       
    def click_register_button(self):
        self.driver.find_element(By.ID, "register-button").click()