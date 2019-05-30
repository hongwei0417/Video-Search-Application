import tkinter as tk
from View.CollectObj import VideoItem
import Module.DB as Db


wh = 500
ww = 800
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"
logoUrl = ['./Asset/youtube.png', './Asset/bili.jpg']

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

def refresh(user, frame):
        for item in frame.winfo_children():
                item.destroy()

        loadVideo(user, frame)

def loadVideo(user, frame):
        dataList = Db.getCollection(user[0])
        itemList = []
        y = 20

        for data in dataList:
                logoIndex = 0
                if data['type'] == 'youtube': logoIndex = 0
                elif data['type'] == 'bilibili': logoIndex = 1
                item = VideoItem(frame)
                item.setImg(data['img'], logoUrl[logoIndex])
                item.setLink(data['link'])
                item.setDelete(user, data['link'], frame, refresh)
                item.setInfo(data['title'], data['author'], data['view'], data['description'])
                item.setPos(20, y)
                itemList.append(item)
                y += 170
        
        frame.config(height=y+20)
        for item in itemList:
                item.load()


def create(user):
        window = tk.Toplevel()
        window.title(user[2] + "的搜尋列表")
        ws = window.winfo_screenwidth() # width of the screen
        hs = window.winfo_screenheight() # height of the screen
        x = (ws/2) - (ww/2)
        y = (hs/2) - (wh/2)
        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        window.resizable(False, False)
        window.configure(background=bgc)

        canvas = tk.Canvas(window, borderwidth=0, background=bgc, highlightthickness=0, relief='ridge')
        frame = tk.Frame(canvas, background=bgc, width=ww, height=wh)
        vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window(0,0, window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event,_canvas=canvas: onFrameConfigure(_canvas))
        
        loadVideo(user, frame)
