import View.Video as Video
from Module.Driver import scroll
from Module.Youtube import Youtube
from selenium import webdriver
import time

###### for windows ######
driver1 = webdriver.Chrome('D:\Hongwei\Python\chromedriver')

###### for macos ######
# driver1 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')
# driver2 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')

Video.init(driver1)

driver1.close()