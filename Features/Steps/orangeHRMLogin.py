import time

from behave import *
from selenium import webdriver


@given(u'Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'Visit OrangeHRM website')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


@when(u'Enter username "{user}" and Password "{pws}"')
def step_impl(context, user, pws):
    context.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys(user)
    context.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys(pws)


@when(u'Click on Login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='btnLogin']").click()


@then(u'User should successfully login to Dashboard')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.quit()
        assert False, "Test Failed"
    if text == "Dashboard":
        time.sleep(5)
        context.driver.quit()
        assert True, "Test Pass"
