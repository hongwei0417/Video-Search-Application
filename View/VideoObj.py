import tkinter as tk
from tkinter import messagebox
import math
import requests
import webbrowser
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen
from Module.Tools import openLocal, openOnline, with_surrogates, remove_emoji, show
import View.Collection as Collection
import Module.DB as Db

class Video:
    
    def __init__(self, frame):
        self.w = 140
        self.h = 200
        self.fbgc = "#262626"
        self.frame = tk.Frame(frame, width=self.w, height=self.h, bg=self.fbgc)
        self.video = tk.Button(self.frame, borderwidth=0, highlightbackground=self.fbgc, relief="groove")
        self.title = tk.Label(self.frame, wraplength=130, bg=self.fbgc, fg="white", font=('Arial', 12), anchor="n", justify = 'left')
        self.author = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))
        self.views = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))

    def setImg(self, url):
        self.video_img = openOnline(url, self.w, 100)
        self.video.config(image = self.video_img)
    
    def setLink(self, href):
        self.video.bind('<Button-1>', lambda e: webbrowser.open(href))
    
    def setCollection(self, user, ty, img, title, author, view, description, link):
        self.video.bind('<Button-2>', lambda e: self.addCollection(user, ty, img, title, author, view, description, link))

    def addCollection(self, user, ty, img, title, author, view, description, link):
        # try:
        result = Db.addCollection(user[0], ty, img, title, author, view, description, link)
        if(result):  
            messagebox.showinfo("蒐藏提醒", "影片已加入蒐藏!")
        else:
            messagebox.showinfo("蒐藏提醒", "這影片加入過囉!")
        # except:
        #     print("加入蒐藏失敗!")
            
    def setInfo(self, title, author, view):
        try:
            self.title.config(text=title)
            self.author.config(text=author)
            self.views.config(text=view)
        except:
            t = with_surrogates(title)
            a = with_surrogates(author)
            v = with_surrogates(view)
            self.title.config(text=remove_emoji(t))
            self.author.config(text=remove_emoji(a))
            self.views.config(text=remove_emoji(v))

    def clear(self):
        self.frame.destroy()
        self.video.destroy()
        self.title.destroy()
        self.author.destroy()
        self.views.destroy()

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def locate(self):
        self.frame.place(x=self.x, y=self.y)
        self.video.place(x=0, y=10)
        self.title.place(x=0, y=120, width=self.w, height=35)
        self.author.place(x=0, y=160, width=self.w)
        self.views.place(x=0, y=175, width=self.w)


class VideoList:
    
    def __init__(self, frame):
        self.page = 1
        self.pageCount = 12 # 一頁要顯示的數目
        self.fh = 400
        self.fw = 1100
        self.fbgc = "#262626"
        self.vList = []
        self.frame = tk.Frame(frame, bg=self.fbgc, width=self.fw, height=self.fh)
        self.logo = tk.Label(self.frame, bg=self.fbgc, borderwidth=0)
        self.up = tk.Button(self.frame, text="▲", font=50, bg=self.fbgc, fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)
        self.down = tk.Button(self.frame, text="▼", font=50, bg=self.fbgc, fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)
        self.pageLb = tk.Label(self.frame, text="1", font=('Arial', 20), bg="#272727", fg='#f8f499')


    def set(self, user, ty, logoUrl, link, engine):
        logoImg = openLocal(logoUrl, 100, 60)
        self.user = user
        self.type = ty
        self.logo.configure(image=logoImg)
        self.logo.image = logoImg
        self.up.bind('<Button-1>', lambda x: self.prePage(engine))
        self.down.bind('<Button-1>', lambda x: self.nextPage(engine))
        self.link = link
    
    def setData(self, data):
        posX = 140
        count = len(data['imgs'])
        display = self.checkToDisplay(count)

        if(display == 0): return
        self.clear()
        i = 0
        for n in range((self.page-1)*self.pageCount, ((self.page-1)*self.pageCount + display)):
            link = self.link + data['hrefs'][n]
            if(i < self.pageCount / 2):
                self.vList.append(Video(self.frame))
                video = self.vList[i]
                video.setImg(data['imgs'][n])
                video.setInfo(data['titles'][n], data['authors'][n], data['views'][n])
                video.setLink(link)
                video.setCollection(self.user, self.type, data['imgs'][n], data['titles'][n], data['authors'][n], data['views'][n], data['descriptions'][n], link)
                video.setPos(posX, 0)
                video.locate()
                posX += 150
                i += 1
                if(i == self.pageCount / 2): posX = 140 # 第一行最後一個
            else: # 顯示在第二行
                self.vList.append(Video(self.frame))
                video = self.vList[i]
                video.setImg(data['imgs'][n])
                video.setInfo(data['titles'][n], data['authors'][n], data['views'][n])
                video.setLink(self.link + data['hrefs'][n])
                video.setCollection(self.user, self.type, data['imgs'][n], data['titles'][n], data['authors'][n], data['views'][n], data['descriptions'][n], link)
                video.setPos(posX, 200)
                video.locate()
                posX += 150
                i += 1
                if(i == self.pageCount): posX = 140

    
    def prePage(self, engine):
        if self.page > 1:
            data = engine.getData()
            self.page -= 1
            self.pageLb.configure(text = str(self.page))
            self.setData(data)

    def nextPage(self, engine):
        self.page += 1
        self.pageLb.configure(text = str(self.page))
        data = engine.getData()
        count = len(data['imgs'])
        while(count < self.page * self.pageCount):
            data = engine.getMore()
            if(count == len(data['imgs'])): # 沒取得新資料
                break
            else:
                count = len(data['imgs']) # 有取的新資料
        self.setData(data)

    def checkToDisplay(self, count):
        display = self.pageCount
        needPages = math.ceil(count / self.pageCount)
        if(self.page > needPages): # 頁面超過顯示範圍
            self.page = needPages
            display = 0
        else:
            if(self.page == needPages and count % self.pageCount != 0):
                display = count % self.pageCount
        
        print(self.page, needPages, count, display)
        return display

    def clear(self):
        for n in range(len(self.vList)):
            if(self.vList[n] != None):
                self.vList[n].clear()
        self.vList.clear()
            

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def load(self):
        self.frame.place(x=self.x, y=self.y)
        self.logo.place(x=20, y=20)
        self.up.place(x=self.fw-50, y=30, height=40, width=40)
        self.down.place(x=self.fw-50, y=330, height=40, width=40)
        self.pageLb.place(x=self.fw-45, y=175)
        for n in range(len(self.vList)):
            self.vList[n].locate()