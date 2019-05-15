import tkinter as tk

wh = 500
ww = 800
fh = 200
fw = 760
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"

def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

def creat():
    window = tk.Tk()
    window.title('My Collections')
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