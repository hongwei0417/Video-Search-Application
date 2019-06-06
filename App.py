import View.Video as Video
import Module.Driver as Driver
from Module.Youtube import Youtube
from selenium import webdriver
import time
import Module.DB as Db
import View.Welcome as Welcome

###### for windows ######
# driver1 = webdriver.Chrome('D:\Hongwei\Python\chromedriver')
driver1 = webdriver.Firefox(executable_path='D:\Hongwei\Python\geckodriver')

###### for macos ######
# driver1 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')
# driver1 = webdriver.Firefox(executable_path='/Users/hongwei/Documents/Python/geckodriver')
driver1.minimize_window()

Welcome.create(driver1)



driver1.close()