import tkinter as tk

bgc = "#121212"

window = tk.Tk()
window.title('Video Search')
window.geometry('800x500')
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

canvas = tk.Canvas(window, borderwidth=0, background=bgc)
frame = tk.Frame(canvas, background=bgc)
vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame) ##資料測試

l = tk.Label(canvas, 
        text='OMG! this is TK!',    # 标签的文字
        font=('Arial', 50),     # 字体和字体大小
        fg="white",
        bg=bgc
        )
l.place(anchor=tk.CENTER, x=400, y=100, height=50, width=300)    # 固定窗口位置









window.mainloop()
