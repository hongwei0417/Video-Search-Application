import requests
from bs4 import BeautifulSoup
import time
import Module.Driver as Driver
class Bili:

    def __init__(self, browser):
        self.url = 'https://search.bilibili.com/all?keyword='
        self.browser = browser
        self.page = 1
        self.data = {
            "imgs": [],
            "titles": [],
            "authors": [],
            "views": [],
            "hrefs": []
        }
        Driver.newTab(self.browser)

    def search(self, keyword):
        Driver.switchTab(self.browser, 1)
        self.keyword = keyword
        url = self.url + keyword
        self.browser.get(url)
        Driver.scrollLazy(self.browser, 5, 0.5)
        self.updateSoup()
        self.appendData()

    def updateSoup(self):
        source = self.browser.page_source
        self.soup = BeautifulSoup(source, 'html.parser')
          
    def getData(self):
        return self.data

    def appendData(self):
        video_obj = self.soup.select('.video-contain .video')

        for video in video_obj:
            img_obj = video.select('.img img')[0]

            if img_obj.has_attr('src'): # 判斷有沒有圖片
                img = "https:" + img_obj['src']
                title = video.select('.info .title')[0]['title']
                author = video.select('.info .tags .up-name')[0].text
                view = video.select('.info .tags .watch-num')[0].text.strip()
                print(view)
                href = video.select('.img-anchor')[0]['href']
                self.data['imgs'].append(img)
                self.data['titles'].append(title)
                self.data['authors'].append(author)
                self.data['views'].append(view)
                self.data['hrefs'].append(href)
            else:
                continue # 沒有圖片就放棄取下一個影片
        
        print(len(self.data['imgs']), len(self.data['hrefs']), len(self.data['titles']),len(self.data['authors']),len(self.data['views']))


    def getMore(self):
        Driver.switchTab(self.browser, 1)
        url = self.url + self.keyword + "&page=" + str(self.page)
        self.browser.get(url)
        Driver.scrollLazy(self.browser, 4, 0.5)
        self.updateSoup()
        self.appendData()
        self.page += 1
            
        return self.data



