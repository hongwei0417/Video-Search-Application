import tkinter as tk
from Module.Tools import openLocal, openOnline, with_surrogates, remove_emoji
import Module.DB as Db
import webbrowser

class VideoItem:

    def __init__(self, frame, n):
        self.w = 750
        self.h = 150
        self.fbgc = "#1C1C1C"
        self.type = n

        self.frame = tk.Frame(frame, bg=self.fbgc, width=self.w, height=self.h)
        self.del_btn = tk.Button(self.frame, text="刪除", fg='#373737', bg='#777777', highlightbackground=self.fbgc, highlightthickness=0)
        self.video = tk.Button(self.frame, borderwidth=0, highlightbackground=self.fbgc, relief="groove")
        self.logo = tk.Label(self.frame, bg=self.fbgc, borderwidth=0)
        self.title = tk.Label(self.frame, wraplength=400, bg=self.fbgc, fg="white", font=('Arial', 15), anchor="nw", justify = 'left')
        self.author = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))
        self.views = tk.Label(self.frame, bg=self.fbgc, fg='#aaaaaa', font=('Arial', 10))
        self.intro = tk.Label(self.frame, wraplength=250, bg=self.fbgc, fg="white", font=('Arial', 10), anchor="nw", justify = 'left')

    def setLink(self, href):
        self.video.bind('<Button-1>', lambda e: webbrowser.open(href))

    def setDelete(self, user, link, frame, lbs, refresh, layer):
        self.del_btn.bind('<Button-1>', lambda e: self.delete(user, link, frame, lbs, refresh, layer))

    def delete(self, user, link, frame, lbs, refresh, layer):
        try:
            Db.delCollection(user[0], link)
        except:
            print("刪除最愛失敗!")

        refresh(user, frame, lbs, self.type, layer)

    def setImg(self, url, logoUrl):
        logoImg = openLocal(logoUrl, 50, 30)
        self.logo.configure(image=logoImg)
        self.logo.image = logoImg
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
            a = with_surrogates(author)
            v = with_surrogates(view)
            i = with_surrogates(intro)
            self.title.config(text=remove_emoji(t))
            self.author.config(text=remove_emoji(a))
            self.views.config(text=remove_emoji(v))
            self.intro.config(text=remove_emoji(i))
        
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def load(self):
        self.frame.place(x=self.x, y=self.y)
        if(self.type != 3):
            self.del_btn.place(x=700, y=0, height=150, width=50)
        self.video.place(x=0, y=0)
        self.logo.place(x=200, y=120)
        self.title.place(x=270, y=10, height=50)
        self.author.place(x=270, y=100)
        self.views.place(x=270, y=120)
        self.intro.place(x=430, y=80, height=60)


class UserItem:


    def __init__(self, frame, user):
        self.w = 750
        self.h = 80
        self.fbgc = "#1C1C1C"
        self.user = user

        self.frame = tk.Frame(frame, bg=self.fbgc, width=self.w, height=self.h)
        self.name = tk.Label(self.frame, bg=self.fbgc, text=user[2], fg='#aaaaaa', font=('Arial', 30), anchor="w", justify = 'left')
        self.count = tk.Label(self.frame, bg=self.fbgc, text=str(user[4]) + "個影片", fg='#aaaaaa', font=('Arial', 20))
        self.view = tk.Label(self.frame, bg='#fcf5bf', text="查看收藏", fg=self.fbgc, font=('Arial', 20))

    def setLink(self, frame, lbs, refresh, overlayer):
        self.view.bind('<Button-1>', lambda e: refresh(self.user, frame, lbs, 3, overlayer))

    
    def setPos(self, x, y):
        self.x = x
        self.y = y


    def load(self):
        self.frame.place(x=self.x, y=self.y)
        self.name.place(x=20, y=0, width=320, height=self.h)
        self.count.place(x=350, y=0, height=self.h)
        self.view.place(x=600, y=0, width=150, height=self.h)


