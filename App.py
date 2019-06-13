import View.Video as Video
import Module.Driver as Driver
from Module.Youtube import Youtube
from selenium import webdriver
import time
import Module.DB as Db
import View.Welcome as Welcome

###### for windows ######
# driver1 = webdriver.Chrome('./chromedriver')
driver1 = webdriver.Firefox(executable_path='./geckodriver')

###### for macos ######
# driver1 = webdriver.Chrome('./geckodriver')
# driver1 = webdriver.Firefox(executable_path='./geckodriver')
driver1.minimize_window()

Welcome.create(driver1)



driver1.close()