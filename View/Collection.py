import tkinter as tk
from View.CollectObj import VideoItem


wh = 500
ww = 800
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"
logoUrl = ['./Asset/youtube.png', './Asset/bili.jpg']

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

def create(img, title, author, view, description):
        window = tk.Toplevel()
        window.title('My Collections')
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

        
        item1 = VideoItem(frame)
        item1.setImg(img, logoUrl[0])
        item1.setInfo(title, author, view, description)
        item1.setPos(20, 20)
        item1.load()

        item2 = VideoItem(frame)
        item2.setImg('https://i.ytimg.com/vi/wKpB5sn17T0/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCUOz12pkNeaPFOt4T_mep2W4IJ7g', logoUrl[1])
        item2.setInfo('我是 - 一個小哈哈哈哈希希拉，真的嘿嘿!', 'EHPMusicChannel', '觀看次數：8,851,509次', '木棉花Youtube頻道動畫線上免費看訂閱木棉花以獲得最新訊息http://bit.ly/Muse-TW_YTChannel J市海邊有一群自稱是深海族的怪人 ...')
        item2.setPos(20, 190)
        item2.load()

        item3 = VideoItem(frame)
        item3.setImg('https://i.ytimg.com/vi/wKpB5sn17T0/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCUOz12pkNeaPFOt4T_mep2W4IJ7g', logoUrl[0])
        item3.setInfo('季彥霖 - 多想愛你『也許命中註定，他比我適合你。』【動態歌詞Lyrics】', 'EHPMusicChannel', '觀看次數：8,851,509次', '木棉花Youtube頻道動畫線上免費看訂閱木棉花以獲得最新訊息http://bit.ly/Muse-TW_YTChannel J市海邊有一群自稱是深海族的怪人 ...')
        item3.setPos(20, 360)
        item3.load()

