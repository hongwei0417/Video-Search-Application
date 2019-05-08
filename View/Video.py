import tkinter as tk
import requests
from PIL import ImageTk, Image
from VideoObj import Video, VideoList
from io import BytesIO

wh = 500
ww = 800
fh = 200
fw = 760
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"

window = tk.Tk()
window.title('Video Search')
window.geometry(str(ww) + 'x' + str(wh))
window.resizable(False, False)
window.configure(background=bgc)

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

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
                width=30, bg=fbgc,
                highlightbackground="#303030",
                highlightthickness=2,
                highlightcolor='#666666',
                fg="white",
                relief="flat",
                font=('Verdana',20),
                )
search_tb.place(x=170, y=15)

search_btn = tk.Button(top_frame, text="搜尋")
search_btn.place(x=600, y=20)

# logoUrl = './Asset/yt.png'
# urls = ['https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg',
#         'https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg',
#         'https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg',
#         'https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg'
#         ]
# infos = [{'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'},
#         {'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'},
#         {'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'},
#         {'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'}
#         ]

# ytList = VideoList(frame)
# ytList.set(logoUrl, urls, infos)
# ytList.setPos(10, 80)
# ytList.load()

# fbList = VideoList(frame)
# fbList.set(logoUrl, urls, infos)
# fbList.setPos(10, 300)
# fbList.load()

# yhList = VideoList(frame)
# yhList.set(logoUrl, urls, infos)
# yhList.setPos(10, 520)
# yhList.load()


window.mainloop()
