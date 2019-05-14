import tkinter as tk
import requests
from PIL import ImageTk, Image
from View.VideoObj import Video, VideoList
from Module.Youtube import Youtube
from io import BytesIO

wh = 500
ww = 800
fh = 200
fw = 760
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"
logoUrl = ['./Asset/yt.png']

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

def init(browsers):
        yt = Youtube(browsers[0])
        create([yt])

def search(engines, text, ytList):
        if(not(text.strip() == '')):
                yt = engines[0]
                yt.search(text.strip())
                yt_data = yt.getData()
                count = len(yt_data['imgs'])
                while(count < 4):
                        yt_data = yt.getMore()
                        if(count == len(yt_data['imgs'])): # 沒取得新資料
                                break
                        else:
                                count = len(yt_data['imgs']) # 有取的新資料
                ytList.page = 1
                ytList.setData(yt_data)
                ytList.load()
        else:
                print('搜尋字串空白')


def create(engines):
        window = tk.Tk()
        window.title('Video Search')
        window.geometry(str(ww) + 'x' + str(wh))
        window.resizable(False, False)
        window.configure(background=bgc)


        canvas = tk.Canvas(window, borderwidth=0, background=bgc, highlightthickness=0, relief='ridge')
        frame = tk.Frame(canvas, background=bgc, width=ww, height=ww)
        vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window(0,0, window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event,_canvas=canvas: onFrameConfigure(_canvas))

        top_frame = tk.Frame(frame, bg=top_bgc, width=ww, height=60)
        top_frame.place(x=0, y=0)

        search_tb = tk.Entry(
                        top_frame,
                        width=30, bg='#383838',
                        highlightbackground="#303030",
                        highlightthickness=2,
                        highlightcolor='#666666',
                        fg="white",
                        relief="flat",
                        font=('Verdana',20),
                        )
        search_tb.place(x=170, y=15)
        

        search_btn = tk.Button(top_frame, 
                                text="搜尋", 
                                fg='#373737', 
                                highlightbackground='#d8d8d8', 
                                highlightthickness=0,
                                )
        search_btn.place(x=580, y=17, height=30, width=50)
        

        ytList = VideoList(frame)
        ytList.set(logoUrl[0], engines[0])
        ytList.setPos(10, 80)
        

        # fbList = VideoList(frame)
        # fbList.set(logoUrl, urls, infos)
        # fbList.setPos(10, 300)
        # fbList.load()

        # yhList = VideoList(frame)
        # yhList.set(logoUrl, urls, infos)
        # yhList.setPos(10, 520)
        # yhList.load()
        search_btn.bind('<Button-1>', lambda e:search(engines, search_tb.get(), ytList))

        window.mainloop()


