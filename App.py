# import View.Welcome
from Module.Youtube import Youtube
from selenium import webdriver

# View.window.mainloop()

browser = webdriver.Chrome('D:\Hongwei\Python\chromedriver')
# browser = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')


yt = Youtube(browser)
soup = yt.search("一拳超人")
yt.getData()




browser.close()