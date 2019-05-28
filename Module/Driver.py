from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def setWindow(browser, x, y):
    browser.set_window_position(x, y)
    browser.set_window_size(700, 500)

def scrollToButtom(browser):
    elm = browser.find_element_by_tag_name('html')
    elm.send_keys(Keys.END)
    time.sleep(2)

def scrollLazy(browser, times, wait):
    maxH = browser.execute_script("return document.body.scrollHeight")
    perH = int(maxH / times) # 每次下滑距離
    currentH = browser.execute_script("return window.pageYOffset")
    while(True):
        currentH += perH
        browser.execute_script("window.scrollTo(0,"+ str(currentH) + ")")
        time.sleep(wait)
        if(currentH > maxH): break
    
    # browser.execute_script("window.onblur = function() { window.onfocus() }")
    # browser.execute_script('alert("Focus window")')
    # browser.switch_to.alert.accept()
    

def switchTab(browser, index):
    browser.switch_to_window(browser.window_handles[index])
    # browser.find_element_by_tag_name('html').send_keys(Keys.COMMAND + Keys.NUMPAD2)


def newTab(browser):
    # browser.find_element_by_tag_name('html').send_keys(Keys.COMMAND + 't')
    # ActionChains(self.browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    browser.execute_script("window.open();")


def relevance(browser, type):
    if type == 'youtube':
        link = browser.find_element_by_css_selector("#container > ytd-toggle-button-renderer > a")
        link.click()
        link = browser.find_element_by_css_selector("#collapse-content > ytd-search-filter-group-renderer:nth-child(5) > ytd-search-filter-renderer:nth-child(2) a")
        link.click()
    elif type == 'bilibili':
        link = browser.find_element_by_css_selector("div.filter-wrap > ul.filter-type.clearfix.order > li:nth-child(1) > a")
        link.click()
    
    time.sleep(1)


def uploadDate(browser, type):
    if type == 'youtube':
        link = browser.find_element_by_css_selector("#container > ytd-toggle-button-renderer > a")
        link.click()
        link = browser.find_element_by_css_selector("#collapse-content > ytd-search-filter-group-renderer:nth-child(5) > ytd-search-filter-renderer:nth-child(4) a")
        link.click()
    elif type == 'bilibili':
        link = browser.find_element_by_css_selector("div.filter-wrap > ul.filter-type.clearfix.order > li:nth-child(3) > a")
        link.click()
    
    time.sleep(1)


def viewCount(browser, type):
    if type == 'youtube':
        link = browser.find_element_by_css_selector("#container > ytd-toggle-button-renderer > a")
        link.click()
        link = browser.find_element_by_css_selector("#collapse-content > ytd-search-filter-group-renderer:nth-child(5) > ytd-search-filter-renderer:nth-child(6) a")
        link.click()
    elif type == 'bilibili':
        link = browser.find_element_by_css_selector("div.filter-wrap > ul.filter-type.clearfix.order > li:nth-child(2) > a")
        link.click()
    
    time.sleep(1)


def score(browser, type):
    if type == 'youtube':
        link = browser.find_element_by_css_selector("#container > ytd-toggle-button-renderer > a")
        link.click()
        link = browser.find_element_by_css_selector("#collapse-content > ytd-search-filter-group-renderer:nth-child(5) > ytd-search-filter-renderer:nth-child(7) a")
        link.click()
    elif type == 'bilibili':
        link = browser.find_element_by_css_selector("div.filter-wrap > ul.filter-type.clearfix.order > li:nth-child(4) > a")
        link.click()
    
    time.sleep(1)


