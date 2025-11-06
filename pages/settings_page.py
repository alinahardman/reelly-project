from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

class SettingsPage(BasePage):

  NEW_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.page-setting-block[href="/set-new-password"]')
  CHANGE_PASSWORD_BUTTON_MOBILE = (By.CSS_SELECTOR, "a[href='/set-new-password']")

  def click_change_password_option(self):
      # Scroll to and click change password button
      button = self.wait.until(EC.element_to_be_clickable(self.CHANGE_PASSWORD_BUTTON_MOBILE))
      self.driver.execute_script("arguments[0].scrollIntoView();", button)
      self.driver.execute_script("arguments[0].click();", button)

  def verify_right_page(self):
   current_url = self.driver.current_url
   assert "set-new-password" in current_url, f"Expected 'settings' in URL, but got: {current_url}"
   print(f"✓ Settings page verified: {current_url}")

