import time

from behave import *
from selenium import webdriver

@given(u'Launch browser')
def launchBrowser(context):
    #context.driver = webdriver.Chrome("Drivers/chromedriver.exe")
    context.driver = webdriver.Chrome()

@when(u'Open OrangeHRM Website')
def openOrangeHRM(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


@then(u'Verify the logo on the Homepage')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True

@then(u'Close browser')
def closeBrowser(context):
    time.sleep(5)
    context.driver.quit()