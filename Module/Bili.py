import requests
from bs4 import BeautifulSoup
from Module.Tools import format_view
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
            "hrefs": [],
            "descriptions": []
        }
        Driver.newTab(self.browser)

    def search(self, keyword, filter):
        Driver.switchTab(self.browser, 1)
        self.keyword = keyword
        url = self.url + keyword
        self.browser.get(url)
        time.sleep(1)
        Driver.video_filter(self.browser, filter, "bilibili")
        Driver.scrollLazy(self.browser, 4, 2)
        self.updateSoup()
        self.clearData()
        self.appendData()


    def updateSoup(self):
        source = self.browser.page_source
        self.soup = BeautifulSoup(source, 'html.parser')
        
    def getData(self):
        return self.data

    def clearData(self):
        self.data = {
            "imgs": [],
            "titles": [],
            "authors": [],
            "views": [],
            "hrefs": [],
            "descriptions": []
        }

    def appendData(self):
        n = 0 # 嘗試重新取得資料次數
        while(n < 3):
            imgs, titles, authors, views, hrefs, descriptions = [], [], [], [], [], []
            
            video_obj = self.soup.select('.video-contain .video')
            success = True
            for video in video_obj:
                img_obj = video.select('.img img')[0]
                
                if img_obj.has_attr('src') and img_obj['src'] != "": # 判斷有沒有圖片
                    img = "https:" + img_obj['src']
                    title = video.select('.info .title')[0]['title']
                    author = video.select('.info .tags .up-name')[0].text
                    view = video.select('.info .tags .watch-num')[0].text.strip()
                    description = video.select('.info .des')[0].text.strip()
                    print(img)
                    href = video.select('.img-anchor')[0]['href']
                    imgs.append(img)
                    titles.append(title)
                    authors.append(author)
                    views.append(format_view(view))
                    hrefs.append(href)
                    descriptions.append(description)
                else:
                    Driver.scrollToTop(self.browser)
                    Driver.scrollLazy(self.browser, 4, 0.5)
                    self.updateSoup()
                    success = False
                    break

            if success:
                self.data['imgs'].extend(imgs)
                self.data['titles'].extend(titles)
                self.data['authors'].extend(authors)
                self.data['views'].extend(views)
                self.data['hrefs'].extend(hrefs)
                self.data['descriptions'].extend(descriptions)
                print(len(self.data['imgs']), len(self.data['hrefs']), len(self.data['titles']),len(self.data['authors']),len(self.data['views']), len(self.data['descriptions']))
                return True
            
            n += 1

        
        return False


    def getMore(self):
        self.page += 1
        Driver.switchTab(self.browser, 1)
        url = self.url + self.keyword + "&page=" + str(self.page)
        self.browser.get(url)
        time.sleep(1)
        Driver.scrollLazy(self.browser, 3, 2)
        self.updateSoup()
        success = self.appendData()
        if success:
            self.page += 1
            
        return self.data



