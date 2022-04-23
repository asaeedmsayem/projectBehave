from behave import *

@given(u'I will Launch browser')
def step_impl(context):
    assert True, "Test Pass"


@when(u'I will Visit OrangeHRM Website')
def step_impl(context):
    assert True, "Test Pass"


@then(u'I will Verify the logo on the Homepage')
def step_impl(context):
    assert True, "Test Pass"


@then(u'I will Close browser')
def step_impl(context):
    assert True, "Test Pass"


@then(u'Enter username "{user}" and Password "{pwd}"')
def step_impl(context,user, pwd):
    assert True, "Test Pass"


@then(u'Click on Login button')
def step_impl(context):
    assert True, "Test Pass"
