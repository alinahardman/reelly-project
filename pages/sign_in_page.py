from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

class SignInPage(BasePage):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open_sign_in(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def login(self, email, password):
       email_field = WebDriverWait(self.driver, 15).until(
    EC.element_to_be_clickable(self.EMAIL_FIELD)
)
       email_field.send_keys(email)

       password_field = WebDriverWait(self.driver, 15).until(
    EC.element_to_be_clickable(self.PASSWORD_FIELD)
)
       password_field.send_keys(password)

       continue_button = WebDriverWait(self.driver, 15).until(
    EC.element_to_be_clickable(self.CONTINUE_BUTTON)
)
       continue_button.click()

