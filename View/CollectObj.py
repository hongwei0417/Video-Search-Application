import tkinter as tk
from Module.Tools import openLocal, openOnline, with_surrogates, remove_emoji

class VideoItem:

    def __init__(self, frame):
        self.w = 750
        self.h = 150
        self.fbgc = "#1C1C1C"

        self.frame = tk.Frame(frame, bg=self.fbgc, width=self.w, height=self.h)
        self.del_btn = tk.Button(self.frame,  text="刪除", fg='#373737', highlightbackground='#d8d8d8', highlightthickness=0)
        self.video = tk.Button(self.frame, borderwidth=0, highlightbackground=self.fbgc, relief="groove", highlightthickness=0)
        self.title = tk.Label(self.frame, wraplength=400, bg=self.fbgc, fg="white", font=('Arial', 15), anchor="nw", justify = 'left')
        self.author = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))
        self.views = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))
        self.intro = tk.Label(self.frame, wraplength=250, bg=self.fbgc, fg="white", font=('Arial', 10), anchor="nw", justify = 'left')

    def setImg(self, url):
        self.video_img = openOnline(url, 250, self.h)
        self.video.config(image = self.video_img)
        self.video.img = self.video_img
    
    def setInfo(self, title, author, view, intro):
        try:
            self.title.config(text=title)
            self.author.config(text=author)
            self.views.config(text=view)
            self.intro.config(text=intro)

        except:
            t = with_surrogates(title)
            self.title.config(text=remove_emoji(t))
            self.author.config(text=remove_emoji(author))
            self.views.config(text=remove_emoji(view))
            self.intro.config(text=remove_emoji(intro))
        
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def load(self):
        self.frame.place(x=self.x, y=self.y)
        self.del_btn.place(x=700, y=0, height=150, width=50)
        self.video.place(x=0, y=0)
        self.title.place(x=270, y=10, height=80)
        self.author.place(x=270, y=100)
        self.views.place(x=270, y=120)
        self.intro.place(x=430, y=100, height=40)




