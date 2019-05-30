import tkinter as tk
import tkinter.messagebox as messagebox
from View.VideoObj import Video, VideoList
import View.Collection as Collection
import  Module.Driver as Driver
from Module.Youtube import Youtube
from Module.Facebook import Facebook
from Module.Bili import Bili
import Module.DB as Db
import Module.Driver as Driver

x = 0
y = 0
wh = 700
ww = 1180
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"
links = ['https://www.youtube.com', 'https:', 'https://www.facebook.com']
logoUrl = ['./Asset/youtube.png', './Asset/bili.jpg', './Asset/facebook.jpg']

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

def init(user, browser):
        Driver.setWindow(browser, 300, 200, 900, 700)
        yt = Youtube(browser)
        bili = Bili(browser)
        # fb = Facebook(browser)
        create(user, [yt, bili])

def search_All(engines, vlists, text, filter):
        if(not(text.strip() == '')):
                search(engines[0], vlists[0], text, filter)
                search(engines[1], vlists[1], text, filter)
                # search(engines[2], vlists[2], text)
        else:
                print('搜尋字串空白')

def search(engine, vlist, text, filter):
        engine.search(text.strip(), filter)
        data = engine.getData()
        count = len(data['imgs'])
        while(count < 12):
                data = engine.getMore()
                if(count == len(data['imgs'])): # 沒取得新資料
                        break
                else:
                        count = len(data['imgs']) # 有取的新資料
        vlist.page = 1
        vlist.setData(data)
        vlist.load()

def openCollection(user):
        Collection.create(user)
                

def create(user, engines):
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
        frame = tk.Frame(canvas, background=bgc, width=ww, height=1000)
        vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window(0,0, window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event,_canvas=canvas: onFrameConfigure(_canvas))

        top_frame = tk.Frame(frame, bg=top_bgc, width=ww, height=60)
        top_frame.place(x=0, y=0)

        name_lb = tk.Label(top_frame, bg=fbgc, text=user[2], fg='#aaaaaa', font=('Arial', 20))
        name_lb.place(x=20, y=15)

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
        search_tb.place(x=150, y=15)
        

        search_btn = tk.Button(top_frame, 
                                text="搜尋", 
                                fg='#373737', 
                                highlightbackground='#d8d8d8', 
                                highlightthickness=0,
                                )
        search_btn.place(x=600, y=17, height=30, width=50)

        var = tk.IntVar()
        var.set(1)
        rb1 = tk.Radiobutton(top_frame, text="關聯性", variable=var, value=1, bg="#adadad", selectcolor="#fcf5bf", indicatoron=0)
        rb2 = tk.Radiobutton(top_frame, text="上傳日期", variable=var, value=2, bg="#adadad", selectcolor="#fcf5bf", indicatoron=0)
        rb3 = tk.Radiobutton(top_frame, text="觀看次數", variable=var, value=3, bg="#adadad", selectcolor="#fcf5bf", indicatoron=0)
        rb4 = tk.Radiobutton(top_frame, text="評價與評分", variable=var, value=4, bg="#adadad", selectcolor="#fcf5bf", indicatoron=0)

        rb1.place(x=700, y=20)
        rb2.place(x=780, y=20)
        rb3.place(x=850, y=20)
        rb4.place(x=920, y=20)

        collec_btn = tk.Button(top_frame, 
                                text="喜愛", 
                                fg='#373737', 
                                highlightbackground='#d8d8d8', 
                                highlightthickness=0,
                                )
        collec_btn.place(x=1050, y=17, height=30, width=50)

        ytList = VideoList(frame)
        ytList.set(user, "youtube", logoUrl[0], links[0], engines[0])
        ytList.setPos(30, 80)

        biliList = VideoList(frame)
        biliList.set(user, "bilibili", logoUrl[1], links[1], engines[1])
        biliList.setPos(30, 500)

        # fbList = VideoList(frame)
        # fbList.set(user, "bilibili", logoUrl[2], links[2], engines[2])
        # fbList.setPos(30, 920)


        search_btn.bind('<Button-1>', lambda e: search_All(engines, [ytList, biliList], search_tb.get(), var.get()))
        collec_btn.bind('<Button-1>', lambda e: openCollection(user))
        window.bind('<Return>', lambda e:search_All(engines, [ytList, biliList], search_tb.get(), var.get()))

        window.mainloop()


