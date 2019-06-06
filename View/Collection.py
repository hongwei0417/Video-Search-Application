import tkinter as tk
from View.CollectObj import VideoItem, UserItem
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

def refresh(user, frame, lbs, n, overlayer):
        x = 0
        for item in frame.winfo_children():
                if isinstance(item, tk.Frame):
                        item.destroy()
                x += 1

        loadVideo(user, frame, lbs, n, overlayer)

def set_lb(n, lbs):
        x = 0
        for lb in lbs:
                if(x == n):
                        lb.configure(bg='#aaaaaa', fg=fbgc)
                else:
                        lb.configure(bg=fbgc, fg='#aaaaaa')
                x += 1

def getData(user, n):
        if(n == 0 or n == 3):
                return Db.getCollection(user[0], 'all')
        elif(n == 1):
                return Db.getCollection(user[0], 'youtube')
        elif(n == 2):
                return Db.getCollection(user[0], 'bilibili')

def loadVideo(user, frame, lbs, n, overlayer):
        set_lb(n, lbs)
        dataList = getData(user, n)

        if len(dataList) == 0:
                overlayer.place(x=250, y=220)
        else:
                overlayer.place_forget()


        itemList = []
        y = 70

        for data in dataList:
                logoIndex = 0
                if data['type'] == 'youtube': logoIndex = 0
                elif data['type'] == 'bilibili': logoIndex = 1
                item = VideoItem(frame, n)
                item.setImg(data['img'], logoUrl[logoIndex])
                item.setLink(data['link'])
                item.setDelete(user, data['link'], frame, lbs, refresh, overlayer)
                item.setInfo(data['title'], data['author'], data['view'], data['description'])
                item.setPos(20, y)
                itemList.append(item)
                y += 170
        
        frame.config(height=wh if y <= wh else y)
        for item in itemList:
                item.load()



def loadUser(frame, lbs, n, overlayer):
        overlayer.place_forget()
        set_lb(n, lbs)
        users = Db.getAllUser()
        itemList = []
        y = 70
        i = 0
        for item in frame.winfo_children():
                if isinstance(item, tk.Frame):
                        item.destroy()
                i += 1

        for user in users:
                item = UserItem(frame, user)
                item.setPos(x=20, y=y)
                item.setLink(frame, lbs, refresh, overlayer)
                itemList.append(item)
                y += 100

        frame.config(height=y+20)
        for item in itemList:
                item.load()

def create(user):
        window = tk.Toplevel()
        window.title(user[2] + "  的蒐藏")
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


        all_lb = tk.Label(frame, bg=fbgc, text="我的全部收藏", fg='#aaaaaa', font=('Arial', 10))
        all_lb.place(x=0, y=0, width=195, height=50)
        
        yt_lb = tk.Label(frame, bg=fbgc, text="Youtube", fg='#aaaaaa', font=('Arial', 10))
        yt_lb.place(x=195, y=0, width=195, height=50)

        bili_lb = tk.Label(frame, bg=fbgc, text="BiliBili", fg='#aaaaaa', font=('Arial', 10))
        bili_lb.place(x=390, y=0, width=195, height=50)

        other_lb = tk.Label(frame, bg=fbgc, text="查看其他使用者", fg='#aaaaaa', font=('Arial', 10))
        other_lb.place(x=585, y=0, width=198, height=50)
        

        overlayer = tk.Label(frame, bg=fbgc, text="無收藏影片~", fg='#aaaaaa', font=('Arial', 50))


        lbs = [all_lb, yt_lb, bili_lb, other_lb]
        
        loadVideo(user, frame, lbs, 0, overlayer)


        all_lb.bind('<Button-1>', lambda x: refresh(user, frame, lbs, 0, overlayer))
        yt_lb.bind('<Button-1>', lambda x: refresh(user, frame, lbs, 1, overlayer))
        bili_lb.bind('<Button-1>', lambda x: refresh(user, frame, lbs, 2, overlayer))
        other_lb.bind('<Button-1>', lambda x: loadUser(frame, lbs, 3, overlayer))
