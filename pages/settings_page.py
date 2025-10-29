from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

class SettingsPage(BasePage):

  NEW_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.page-setting-block[href="/set-new-password"]')

  def click_change_password_option(self):
      change_password_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.NEW_PASSWORD_BUTTON)
        )
      change_password_button.click()


  def verify_right_page(self):
   current_url = self.driver.current_url
   assert "set-new-password" in current_url, f"Expected 'settings' in URL, but got: {current_url}"
   print(f"✓ Settings page verified: {current_url}")

