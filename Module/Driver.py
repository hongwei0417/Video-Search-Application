from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def scroll(browser):
    elm = browser.find_element_by_tag_name('html')
    elm.send_keys(Keys.END)
    # browser.execute_script("window.onblur = function() { window.onfocus() }")
    # browser.execute_script('alert("Focus window")')
    # browser.switch_to.alert.accept()
    time.sleep(2)

def newTab(browser, url):
    # ActionChains(self.browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    browser.execute_script("window.open(" + url + ");")

