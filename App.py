import View.Video as Video
import Module.Driver as Driver
from Module.Youtube import Youtube
from selenium import webdriver
import time
import Module.DB as Db

###### for windows ######
# driver1 = webdriver.Chrome('D:\Hongwei\Python\chromedriver')
# driver1 = webdriver.Firefox(executable_path='D:\Hongwei\Python\geckodriver')

###### for macos ######
# driver1 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')
driver1 = webdriver.Firefox(executable_path='/Users/hongwei/Documents/Python/geckodriver')

Driver.setWindow(driver1, 350, 190)

user = Db.login("test", "1234")
if(user != None):
    Video.init(user, driver1)
else:
    print("登入失敗")





driver1.close()