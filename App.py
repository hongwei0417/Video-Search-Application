import View
from Youtube import Youtube
from selenium import webdriver

browser = webdriver.Chrome('/Users/hongwei/Documents/Python/chromedriver')

yt = Youtube(browser)
soup = yt.search("臺北大學")
yt.getVideosName(soup)

# View.window.mainloop()


browser.close()