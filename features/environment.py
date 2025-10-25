from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Application.app import Application


def browser_init(context):
    """
    :param context: Behave context
    """

    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)

    context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    context.app = Application(context.driver)
    context.driver.implicitly_wait(4)



    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.app = Application(context.driver)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
