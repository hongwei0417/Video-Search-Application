# import View.Welcome
from Module.Youtube import Youtube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# View.window.mainloop()

# for windows
driver1 = webdriver.Chrome('D:\Hongwei\Python\chromedriver')
driver2 = webdriver.Chrome('D:\Hongwei\Python\chromedriver')

# for macos
# driver1 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')
# driver2 = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')


yt1 = Youtube(driver1)
soup = yt1.search("一拳超人")

yt2 = Youtube(driver2)
soup = yt2.search("長庚大學")


# yt.getData()

# yt.scroll()




# browser.close()