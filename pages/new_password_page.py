from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

class NewPasswordPage(BasePage):
    NEW_PASSWORD_FIELD = (By.ID, 'Enter-new-password')
    REPEAT_PASSWORD_FIELD = (By.ID, 'Repeat-password')
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.submit-button-2[wized="changePasswordButton"]')


    def set_new_test_password(self, new_password):
        new_password_field = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.NEW_PASSWORD_FIELD)
    )
        new_password_field.send_keys(new_password)

        repeat_password_field = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.REPEAT_PASSWORD_FIELD)
    )
        repeat_password_field.send_keys(new_password)

    def verify_change_password_button_is_clickable(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHANGE_PASSWORD_BUTTON)
        )

        assert button.is_enabled(), "Change password button is not enabled"
        print(f"Change Password button is clickable")
