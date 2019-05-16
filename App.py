import View.Video as Video
import Module.Driver as Driver
from Module.Youtube import Youtube
from selenium import webdriver
import time

###### for windows ######
# driver1 = webdriver.Chrome('D:\Hongwei\Python\chromedriver')

###### for macos ######
# driver1 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')
driver1 = webdriver.Firefox(executable_path='/Users/hongwei/Documents/Python/geckodriver')
Driver.setWindow(driver1, 350, 190)
# driver2 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')

Video.init(driver1)

driver1.close()