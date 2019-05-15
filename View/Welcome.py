import tkinter as tk
import re
import json

bgc = "#121212"

window = tk.Tk()
window.title('Video Search')
window.geometry('800x500')
window.resizable(False, False)
window.configure(background=bgc)
# window.tk.call('encoding', 'system', 'unicode')


def populate(frame):
        '''Put in some fake data'''
        for row in range(100):
                tk.Label(frame, text="%s" % row, width=3, borderwidth="1", relief="solid").grid(row=row, column=0)
                t="this is the second column for row %s" %row
                tk.Label(frame, text=t).grid(row=row, column=1)

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

canvas = tk.Canvas(window, borderwidth=0, background=bgc)
frame = tk.Frame(canvas, background=bgc)
vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, _canvas=canvas: onFrameConfigure(_canvas))

# populate(frame) ##資料測試


_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')

def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def with_surrogates(text):
    return _nonbmp.sub(_surrogatepair, text)


import re

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

t = '這邊\uD83D\uDE05是文字'
# print(u'\uD83D\uDE05')
#convert to unicode
# teststring = unicode('🙏', 'utf-8')

#encode it with string escape
# teststring = teststring.encode('unicode_escape')
# print(ascii(json.loads('🙏')))
l = tk.Label(window, 
    text= remove_emoji(t),    # 标签的文字
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
l.place(anchor=tk.CENTER, x=400, y=100, height=50, width=300)    # 固定窗口位置



b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, command=lambda : print(123), relief="raised"
    ) 

b.place(x=100, y=100)



window.mainloop()
