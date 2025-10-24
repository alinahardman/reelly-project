from behave import given, when, then

@when("Add some test password to the input fields")
def set_new_test_password(context):
    new_test_password = "MyTestPassword123"
    context.app.new_password_page.set_new_test_password(new_test_password)

@then("Verify the “Change password” button is available (but don’t click on it)")
def verify_change_password_button_is_clickable(context):
    context.app.new_password_page.verify_change_password_button_is_clickable()