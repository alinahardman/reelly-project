from behave import given, when, then
from selenium.webdriver.common.by import By

CONTINUE_BUTTON = (By.CSS_SELECTOR, '[wized="loginButton"]')

# TEMPORARY CREDENTIALS - WILL MOVE TO ENVIRONMENT FILE LATER
TEST_EMAIL = "halina.hard@gmail.com"
TEST_PASSWORD = "xxxxx"

@given("Open Sign In page")
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in()


@when("Login to the page")
def login(context):
    context.app.sign_in_page.login(TEST_EMAIL, TEST_PASSWORD)
    context.driver.find_element(*CONTINUE_BUTTON).click()








