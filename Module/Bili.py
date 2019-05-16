import requests
from bs4 import BeautifulSoup
import time
import Module.Driver as Driver
class Bili:

    def __init__(self, browser):
        self.url = 'https://search.bilibili.com/all?keyword='
        self.browser = browser
        Driver.newTab(self.browser)

    def search(self, keyword):
        Driver.switchTab(self.browser, 1)
        url = self.url + keyword
        self.browser.get(url)
        Driver.scrollLazy(self.browser, 5, 0.5)
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
        video_obj = self.soup.select('.video-contain .video')

        for video in video_obj:
            img_obj = video.select('.img img')[0]

            if img_obj.has_attr('src'): # 判斷有沒有圖片
                img = "https:" + img_obj['src']
                title = video.select('.info .title')[0]['title']
                author = video.select('.info .tags .up-name')[0].text
                view = video.select('.info .tags .watch-num')[0].text.strip()
                print(view)
                href = "https:" + video.select('.img-anchor')[0]['href']
                data['imgs'].append(img)
                data['titles'].append(title)
                data['authors'].append(author)
                data['views'].append(view)
                data['hrefs'].append(href)
            else:
                continue # 沒有圖片就放棄取下一個影片
        
        print(len(data['imgs']), len(data['hrefs']), len(data['titles']),len(data['authors']),len(data['views']))

        return data

    def getMore(self, pages=1):
        Driver.switchTab(self.browser, 1)
        for i in range(pages):
            Driver.scrollLazy(self.browser, 5, 0.5)
        self.updateSoup()
        data = self.getData()
            
        return data



