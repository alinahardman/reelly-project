from behave import given, when, then
from selenium.webdriver.common.by import By

SETTINGS_BUTTON = (By.CSS_SELECTOR, '.menu-button-block[href="/settings"]')

@when("Click on the settings option")

def click_hamburger_menu(context):
    context.app.main_page_side_menu.click_hamburger_menu()

def click_settings(context):
    context.app.main_page_side_menu.click_settings()

