import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen

class Video:
    
    def __init__(self, frame):
        self.w = 140
        self.h = 200
        self.fbgc = "#1C1C1C"
        self.frame = tk.Frame(frame, width=self.w, height=self.h, bg=self.fbgc)
        self.video = tk.Button(self.frame, borderwidth=0, )
        self.title = tk.Label(self.frame, wraplength=130, bg=self.fbgc, fg="white", font=('Arial', 10), anchor="n", justify = 'left')
        self.author = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 9))
        self.views = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 9))

    def setUrl(self, url):
        # response = requests.get(url)
        # img_data = response.content
        img_data = urlopen(url).read()
        img_open = Image.open(BytesIO(img_data)).resize((self.w,100), Image.ANTIALIAS)
        self.video_img = ImageTk.PhotoImage(img_open)
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
        self.title.place(x=0, y=115, width=self.w, height=35)
        self.author.place(x=0, y=155, width=self.w)
        self.views.place(x=0, y=175, width=self.w)
        