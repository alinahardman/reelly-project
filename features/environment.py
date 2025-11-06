from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Application.app import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    #
    # # ===== LOCAL MOBILE EMULATION =====
    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

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
    # bs_user = 'alinahardman_xqthko'
    # bs_key = 'fzyrfds8uiTSRYYmKoFj'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Sonoma",
    #     "browserName": "Chrome",
    #     "browserVersion": "latest",
    #     "sessionName": scenario_name,
    #     "local": "false",
    #     "seleniumVersion": "4.8.0",
    #     "resolution": "1920x1080",
    #     "userName": bs_user,
    #     "accessKey": bs_key,
    #     "consoleLogs": "disable",  # or "errors" instead of "verbose"
    #     "networkLogs": False,
    #     # "video": False,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #
    # # Chrome specific options
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-infobars')

    # ===== BROWSERSTACK MOBILE CHROME =====
    bs_user = 'alinahardman_xqthko'
    bs_key = 'fzyrfds8uiTSRYYmKoFj'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
    "os": "android",
    "osVersion": "12.0",
    "deviceName": "Samsung Galaxy S22",
    "browserName": "chrome",  # Use mobile Chrome browser
    "sessionName": scenario_name,
    "realMobile": "true",
    "userName": bs_user,
    "accessKey": bs_key,
    "buildName": "Reelly Mobile Browser Tests Android",
    "projectName": "Reelly Project",
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)

    # Print mobile viewport info for verification
    window_size = context.driver.get_window_size()
    print(f"Mobile viewport size: {window_size['width']}x{window_size['height']}")

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)
    # Define require to prevent the specific error
    context.driver.execute_script("""
      if (typeof require === 'undefined') {
          window.require = function() { return {}; };
      }
      """)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_scenario(context, scenario):
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test completed"}}'
        )
        context.driver.quit()
