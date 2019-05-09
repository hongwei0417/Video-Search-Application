import requests
from bs4 import BeautifulSoup


class Youtube:

    def __init__(self, browser):
        self.url = 'https://www.youtube.com/results?search_query='
        self.browser = browser

    def search(self, keyword):
        self.url += keyword
        self.browser.get(self.url)
        self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        return self.soup

    def getData(self):
        data = {}
        video_obj = self.soup.select('#contents ytd-video-renderer')
        imgUrls = self.getImgs(video_obj)

        # print(imgUrls)

    def getImgs(self, video_obj):
        img_list = []
        img_obj = video_obj[0].select('#img')

        print(img_obj[0].has_attr('src'))
        # 
        # img_list = list(map(lambda item: item['src'], img_obj))

        # print(img_list)
        # return img_list

    def getTitles(self, soup):
        title_obj = soup.select("#contents ytd-video-renderer #video-title")
        title_list = list(map(lambda item: item['title'], title_obj))
        return title_list





