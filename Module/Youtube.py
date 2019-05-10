import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time


class Youtube:

    def __init__(self, browser):
        self.url = 'https://www.youtube.com/results?search_query='
        self.browser = browser

    def search(self, keyword):
        url = self.url + keyword
        self.browser.get(url)
        self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        return self.soup

    def getData(self):
        data = {}
        imgs = self.getImgs()
        titles = self.getTitles()
        authors = self.getAuthors()
        views = self.getViews()

        print(imgs)
        print('-------------------------------------------------------')
        print(titles)
        print('-------------------------------------------------------')
        print(authors)
        print('-------------------------------------------------------')
        print(views)
        print('-------------------------------------------------------')

        print(len(imgs),len(titles),len(authors),len(views))


    def getImgs(self):
        img_obj = self.soup.select('#contents ytd-video-renderer #img[src]')
        img_list = list(map(lambda item: item['src'], img_obj))
        return img_list

    def getTitles(self):
        title_obj = self.soup.select("#contents ytd-video-renderer #video-title[title]")
        title_list = list(map(lambda item: item['title'], title_obj))
        return title_list

    def getAuthors(self):
        author_obj = self.soup.select("#contents ytd-video-renderer #byline[title]")
        author_list = list(map(lambda item: item['title'], author_obj))
        return author_list

    def getViews(self):
        view_obj = self.soup.select("#contents ytd-video-renderer #metadata-line span:first-child")
        view_list = list(map(lambda item: item.text.strip(), view_obj))
        return view_list

    def scroll(self):
        for i in range(5):
            elm = self.browser.find_element_by_tag_name('html')
            elm.send_keys(Keys.END)
            time.sleep(5)

    def openTab(self):
        # ActionChains(self.browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
        self.browser.execute_script("window.open('https://www.google.com');")







