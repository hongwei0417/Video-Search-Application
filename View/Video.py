import tkinter as tk
from PIL import ImageTk, Image

wh = 500
ww = 1200
bgc = "#121212"
top_bgc = "#272727"

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

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))


top_frame = tk.Frame(frame, bg=top_bgc, width=ww, height=50)
top_frame.place(x=0, y=0)

ytFrame = tk.Frame(frame, bg="white", width=600, height=50)
ytFrame.place(x=100, y=100)

# populate(frame) ##資料測試

window.mainloop()
