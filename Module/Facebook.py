import requests
from bs4 import BeautifulSoup
import time
import Module.Driver as Driver

class Facebook:

    def __init__(self, browser):
        self.url = 'https://www.facebook.com/search/videos/?q='
        self.browser = browser
        Driver.newTab(self.browser)

    def search(self, keyword):
        Driver.switchTab(self.browser, 2)
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
        data['descriptions'] = []
        video_obj = self.soup.findAll("div", {"role":"VIDEOS"})

        for video in video_obj:
            img_obj = video.select('.img')[0]

            if img_obj.has_attr('src'): # 判斷有沒有圖片
                img = img_obj['src']
                title = video.select('._4ovi')[0].text.strip()
                author = video.select('.fwb a')[0].text.strip()
                view = video.select('.fsm.fwn.fcg')[0].text.strip()
                href = video.select('.async_saving')[0]['href']
                description = video.select('._4ovj._4ovl')[0].text.strip()
                data['imgs'].append(img)
                data['titles'].append(title)
                data['authors'].append(author)
                data['views'].append(view)
                data['hrefs'].append(href)
                data['descriptions'].append(description)
            else:
                continue # 沒有圖片就放棄取下一個影片
        
        print(len(data['imgs']), len(data['hrefs']), len(data['titles']),len(data['authors']),len(data['views']), len(data['descriptions']))

        return data

    def getMore(self, pages=2):
        Driver.switchTab(self.browser, 0)
        for i in range(pages):
            Driver.scrollToButtom(self.browser)
        self.updateSoup()
        data = self.getData()
            
        return data
