import tkinter as tk
from View.VideoObj import Video, VideoList
import  Module.Driver as Driver
from Module.Youtube import Youtube
from Module.Bili import Bili

x = 0
y = 0
wh = 500
ww = 800
fh = 200
fw = 760
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"
links = ['https://www.youtube.com', '']
logoUrl = ['./Asset/youtube.png', './Asset/bili.jpg']

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

def init(browser):
        yt = Youtube(browser)
        bili = Bili(browser)
        create([yt, bili])

def search_All(engines, vlists, text):
        if(not(text.strip() == '')):
                search(engines[0], vlists[0], text)
                search(engines[1], vlists[1], text)
        else:
                print('搜尋字串空白')

def search(engine, vlist, text):
        engine.search(text.strip())
        data = engine.getData()
        count = len(data['imgs'])
        while(count < 4):
                data = engine.getMore()
                if(count == len(data['imgs'])): # 沒取得新資料
                        break
                else:
                        count = len(data['imgs']) # 有取的新資料
        vlist.page = 1
        vlist.setData(data)
        vlist.load()
                

def create(engines):
        window = tk.Tk()
        window.title('Video Search')
        ws = window.winfo_screenwidth() # width of the screen
        hs = window.winfo_screenheight() # height of the screen
        x = (ws/2) - (ww/2)
        y = (hs/2) - (wh/2)
        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
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
        ytList.set(logoUrl[0], links[0], engines[0])
        ytList.setPos(10, 80)
        

        biliList = VideoList(frame)
        biliList.set(logoUrl[1], links[1], engines[1])
        biliList.setPos(10, 300)

        # yhList = VideoList(frame)
        # yhList.set(logoUrl, urls, infos)
        # yhList.setPos(10, 520)
        # yhList.load()
        search_btn.bind('<Button-1>', lambda e:search_All(engines, [ytList, biliList], search_tb.get()))
        window.bind('<Return>', lambda e:search_All(engines, [ytList, biliList], search_tb.get()))

        window.mainloop()


