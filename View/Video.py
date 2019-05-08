import tkinter as tk
import requests
from PIL import ImageTk, Image
from VideoObj import Video
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

ytFrame = tk.Frame(frame, bg=fbgc, width=fw, height=fh)
ytFrame.place(x=10, y=80)

yhFrame = tk.Frame(frame, bg=fbgc, width=fw, height=fh)
yhFrame.place(x=10, y=300)

fbFrame = tk.Frame(frame, bg=fbgc, width=fw, height=fh)
fbFrame.place(x=10, y=520)

ytImg_open = Image.open('./Asset/yt.png').resize((100,60), Image.ANTIALIAS)
ytImg = ImageTk.PhotoImage(ytImg_open)
ytLogo = tk.Label(ytFrame, image=ytImg, bg=fbgc, borderwidth=0)
ytLogo.place(x=10, y=20)

# test_open = Image.open('./Asset/google.png').resize((100,100), Image.ANTIALIAS)
# testImg = ImageTk.PhotoImage(test_open)
# testLogo = tk.Label(ytFrame, image=testImg, borderwidth=0)
# testLogo.place(x=150, y=0)
# testLogo.bind("<Button-1>", lambda x: print(123))

# test_open = Image.open('./Asset/google.png').resize((100,100), Image.ANTIALIAS)
# testImg = ImageTk.PhotoImage(test_open)
# testLogo = tk.Button(ytFrame, image=testImg, borderwidth=0)
# testLogo.place(x=150, y=0)
# testLogo.bind("<Button-1>", lambda x: print(123))

v1 = Video(ytFrame)
v1.setUrl('https://i.ytimg.com/vi/J-7SaPOAA24/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAM3g8k5tpc0LPMQeHWQcu3HdR0vg')
v1.setPos(130,0)
v1.setInfo({'title': '【Faker】解謎遊戲天才！芭芭是你系列第一集','author': '中譯版今日韓服精華','views': '觀看次數：113萬次'})
v1.locate()

# v2 = Video(ytFrame)
# v2.setUrl('https://i.ytimg.com/vi/b4hTJLtCcUw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCG5gA6AgbGPbjOknIjavjQA5YsLg')
# v2.setPos(280,0)
# v2.locate()

# v3 = Video(ytFrame)
# v3.setUrl('https://i.ytimg.com/vi/b4hTJLtCcUw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCG5gA6AgbGPbjOknIjavjQA5YsLg')
# v3.setPos(430,0)
# v3.locate()

# v4 = Video(ytFrame)
# v4.setUrl('https://i.ytimg.com/vi/b4hTJLtCcUw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCG5gA6AgbGPbjOknIjavjQA5YsLg')
# v4.setPos(580,0)
# v4.locate()

# response = requests.get('https://is2-ssl.mzstatic.com/image/thumb/Purple128/v4/fb/26/01/fb2601b9-27b3-a701-f011-48808eaae98d/source/256x256bb.jpg')
# img_data = response.content
# testImg = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
# testLogo = tk.Button(ytFrame, image=testImg, borderwidth=0)
# testLogo.place(x=0, y=0)


# populate(frame) ##資料測試

window.mainloop()
