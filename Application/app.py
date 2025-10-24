from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from pages.main_page_side_menu import MainPageSideMenu
from pages.settings_page import SettingsPage
from pages.new_password_page import NewPasswordPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.page = BasePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.main_page_side_menu = MainPageSideMenu(driver)
        self.settings_page = SettingsPage(driver)
        self.new_password_page = NewPasswordPage(driver)
