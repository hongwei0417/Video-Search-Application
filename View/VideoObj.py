import tkinter as tk
import re
import math
import requests
import webbrowser
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen
from View.Tools import openLocal, openOnline

_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')

def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def with_surrogates(text):
    return _nonbmp.sub(_surrogatepair, text)

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

class Video:
    
    def __init__(self, frame):
        self.w = 140
        self.h = 200
        self.fbgc = "#1C1C1C"
        self.frame = tk.Frame(frame, width=self.w, height=self.h, bg=self.fbgc)
        self.video = tk.Button(self.frame, borderwidth=0, highlightbackground=self.fbgc, relief="groove")
        self.title = tk.Label(self.frame, wraplength=130, bg=self.fbgc, fg="white", font=('Arial', 12), anchor="n", justify = 'left')
        self.author = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))
        self.views = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))

    def setImg(self, url):
        print(url)
        self.video_img = openOnline(url, self.w, 100)
        self.video.config(image = self.video_img)
    
    def setLink(self, href):
        print(href)
        self.video.bind('<Button-1>', lambda x: webbrowser.open(href))
        
    def setInfo(self, title, author, view):
        try:
            self.title.config(text=title)
            self.author.config(text=author)
            self.views.config(text=view)
        except:
            t = with_surrogates(title)
            self.title.config(text=remove_emoji(t))
            self.author.config(text=remove_emoji(author))
            self.views.config(text=remove_emoji(view))

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
        self.author.place(x=0, y=155, width=self.w)
        self.views.place(x=0, y=175, width=self.w)
        


class VideoList:
    
    def __init__(self, frame):
        self.page = 1
        self.fh = 200
        self.fw = 760
        self.fbgc = "#1C1C1C"
        self.link = 'https://www.youtube.com'
        self.vList = []
        self.frame = tk.Frame(frame, bg=self.fbgc, width=self.fw, height=self.fh)
        self.logo = tk.Label(self.frame, bg=self.fbgc, borderwidth=0)
        self.up = tk.Button(self.frame, text="▲", font=30, bg=self.fbgc, fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)
        self.down = tk.Button(self.frame, text="▼", font=30, bg=self.fbgc, fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)

    def set(self, logoUrl, engine):
        logoImg = openLocal(logoUrl, 100, 60)
        self.logo.configure(image=logoImg)
        self.logo.image = logoImg
        self.up.bind('<Button-1>', lambda x: self.prePage(engine))
        self.down.bind('<Button-1>', lambda x: self.nextPage(engine))
    
    def setData(self, data):
        posX = 130
        count = len(data['imgs'])
        display = self.checkToDisplay(count)

        if(display == 0): return
        self.clear()
        i = 0
        for n in range((self.page-1)*4, ((self.page-1)*4+display)):
            self.vList.append(Video(self.frame))
            video = self.vList[i]
            video.setImg(data['imgs'][n])
            video.setInfo(data['titles'][n], data['authors'][n], data['views'][n])
            video.setLink(self.link + data['hrefs'][n])
            video.setPos(posX, 0)
            video.locate()
            posX += 150
            i += 1
    
    def prePage(self, engine):
        if self.page > 1:
            data = engine.getData()
            self.page -= 1
            self.setData(data)

    def nextPage(self, engine):
        self.page += 1
        data = engine.getData()
        count = len(data['imgs'])
        if(count < self.page * 4):
            data = engine.getMore()
            count = len(data['imgs'])
        self.setData(data)

    def checkToDisplay(self, count):
        n = 4
        display = 4
        needPages = math.ceil(count / n)
        if(self.page > needPages): # 頁面超過顯示範圍
            self.page = needPages
            display = 0
        else:
            if(self.page == needPages and count % n != 0):
                display = count % n
        
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
        self.logo.place(x=10, y=20)
        self.up.place(x=727, y=40, height=25, width=25)
        self.down.place(x=727, y=140, height=25, width=25)
        for n in range(len(self.vList)):
            self.vList[n].locate()