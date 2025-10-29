from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Application.app import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    ### FIREFOX###
    # context.driver = webdriver.Firefox()

    ### SAFARI###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'alinahardman_xqthko'
    bs_key = 'fzyrfds8uiTSRYYmKoFj'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os": "OS X",
        "osVersion": "Sonoma",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "sessionName": scenario_name,
        "local": "false",
        "seleniumVersion": "4.8.0",
        "resolution": "1920x1080",
        "userName": bs_user,
        "accessKey": bs_key,
        "consoleLogs": "disable",  # or "errors" instead of "verbose"
        "networkLogs": False,
        # "video": False,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # Chrome specific options
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.quit()

