import requests
from bs4 import BeautifulSoup


class Youtube:

    def __init__(self, browser):
        self.url = 'https://www.youtube.com/results?search_query='
        self.browser = browser

    def search(self, keyword):
        self.url += keyword
        self.browser.get(self.url)
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        return soup

    def getVideosName(self, soup):
        title_obj = soup.select("#contents ytd-video-renderer #video-title")
        title_list = list(map(lambda item: item['title'], title_obj))
        return title_list

        




