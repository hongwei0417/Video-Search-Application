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


def populate(frame):
        '''Put in some fake data'''
        for row in range(100):
                tk.Label(frame, text="%s" % row, width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
                t="this is the second column for row %s" %row
                tk.Label(frame, text=t).grid(row=row, column=1)

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

# ytFrame = tk.Frame(frame, bg=fbgc, width=fw, height=fh)
# ytFrame.place(x=10, y=80)

# yhFrame = tk.Frame(frame, bg=fbgc, width=fw, height=fh)
# yhFrame.place(x=10, y=300)

# fbFrame = tk.Frame(frame, bg=fbgc, width=fw, height=fh)
# fbFrame.place(x=10, y=520)

logoUrl = './Asset/yt.png'
urls = ['https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg',
        'https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg',
        'https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg',
        'https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg'
        ]
infos = [{'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'},
        {'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'},
        {'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'},
        {'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'}
        ]
vl = VideoList(frame)
vl.set(logoUrl, urls, infos)
vl.load()


# populate(frame) ##資料測試

window.mainloop()
