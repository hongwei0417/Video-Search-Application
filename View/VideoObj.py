import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen
from Tools import openLocal, openOnline

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
        self.video_img = openOnline(url, self.w, 100)
        self.video.config(image = self.video_img)
        
    def setInfo(self, info):
        self.title.config(text=info["title"])
        self.author.config(text=info["author"])
        self.views.config(text=info['views'])

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
        self.fh = 200
        self.fw = 760
        self.fbgc = "#1C1C1C"
        self.vList = {}
        self.frame = tk.Frame(frame, bg=self.fbgc, width=self.fw, height=self.fh)
        self.logo = tk.Label(self.frame, bg=self.fbgc, borderwidth=0)
        self.up = tk.Button(self.frame, text="▲", font=30, bg=self.fbgc, fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)
        self.down = tk.Button(self.frame, text="▼", font=30, bg=self.fbgc, fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)

    def set(self, logoUrl, urls, infos):
        posX = 130
        logoImg = openLocal(logoUrl, 100, 60)
        self.logo.configure(image=logoImg)
        self.logo.image = logoImg
        for n in range(len(urls)):
            self.vList['v'+str(n+1)] = Video(self.frame)
            video = self.vList['v'+str(n+1)]
            video.setImg(urls[n])
            video.setInfo(infos[n])
            video.setPos(posX, 0)
            posX += 150

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def load(self):
        self.frame.place(x=self.x, y=self.y)
        self.logo.place(x=10, y=20)
        self.up.place(x=727, y=40, height=25, width=25)
        self.down.place(x=727, y=140, height=25, width=25)
        for n in range(len(self.vList)):
            self.vList['v'+str(n+1)].locate()