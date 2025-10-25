from behave import given, when, then


@when("Click on the Change password option")
def click_change_password_option(context):
     context.app.settings_page.click_change_password_option()


# @then("Verify the right page opens")
# def verify_right_page(context):
#      context.app.settings_page.verify_right_page()