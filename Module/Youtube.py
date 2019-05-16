import requests
from bs4 import BeautifulSoup
import time
import Module.Driver as Driver
class Youtube:

    def __init__(self, browser):
        self.url = 'https://www.youtube.com/results?search_query='
        self.browser = browser

    def search(self, keyword):
        Driver.switchTab(self.browser, 0)
        url = self.url + keyword
        self.browser.get(url)
        self.updateSoup()

    def updateSoup(self):
        source = self.browser.page_source
        self.soup = BeautifulSoup(source, 'html.parser')

    def getData(self):
        data = {}
        data['imgs'] = []
        data['titles'] = []
        data['authors'] = []
        data['views'] = []
        data['hrefs'] = []
        video_obj = self.soup.select('#contents ytd-video-renderer')

        for video in video_obj:
            img_obj = video.select('#img')[0]

            if img_obj.has_attr('src'): # 判斷有沒有圖片
                img = img_obj['src']
                title = video.select('#video-title')[0]['title']
                author = video.select('#byline')[0]['title']
                view = video.select('#metadata-line span:first-child')[0].text.strip()
                href = video.select('#thumbnail')[0]['href']
                data['imgs'].append(img)
                data['titles'].append(title)
                data['authors'].append(author)
                data['views'].append(view)
                data['hrefs'].append(href)
            else:
                continue # 沒有圖片就放棄取下一個影片
        
        print(len(data['imgs']), len(data['hrefs']), len(data['titles']),len(data['authors']),len(data['views']))

        return data

    def getMore(self, pages=2):
        Driver.switchTab(self.browser, 0)
        for i in range(pages):
            Driver.scrollToButtom(self.browser)
        self.updateSoup()
        data = self.getData()
            
        return data



