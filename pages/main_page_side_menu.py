from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

class MainPageSideMenu(BasePage):
    SETTINGS_BUTTON = (By.CSS_SELECTOR, '.menu-button-block[href="/settings"]')

    def click_settings(self):
        settings_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS_BUTTON)
        )
        settings_button.click()

        current_url = self.driver.current_url
        assert "settings" in current_url, f"Expected 'settings' in URL, but got: {current_url}"
        print(f"✓ Settings page verified: {current_url}")