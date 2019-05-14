import requests
from bs4 import BeautifulSoup
import time
import Module.Driver as Driver
class Youtube:

    def __init__(self, browser):
        self.url = 'https://www.youtube.com/results?search_query='
        self.browser = browser

    def search(self, keyword):
        url = self.url + keyword
        self.browser.get(url)
        self.updateSoup()

    def updateSoup(self):
        source = self.browser.page_source
        self.soup = BeautifulSoup(source, 'html.parser')

    def getData(self):
        data = {}
        data['imgs'] = self.getImgs()
        data['titles'] = self.getTitles()
        data['authors'] = self.getAuthors()
        data['views'] = self.getViews()
        data['hrefs']= self.getLinks()

        # print(imgs)
        # print('-------------------------------------------------------')
        # print(titles)
        # print('-------------------------------------------------------')
        # print(authors)
        # print('-------------------------------------------------------')
        # print(views)
        # print('-------------------------------------------------------')

        print(len(data['imgs']), len(data['hrefs']), len(data['titles']),len(data['authors']),len(data['views']))

        return data

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

    def getLinks(self):
        src_obj = self.soup.select('#contents ytd-video-renderer #thumbnail')
        src_list = list(map(lambda item: item['href'], src_obj))
        return src_list

    def getMore(self, pages=1):
        for i in range(pages):
            Driver.scroll(self.browser)
        self.updateSoup()
        data = self.getData()
            
        return data



