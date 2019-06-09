import tkinter as tk
import View.Video as Video
import Module.DB as Db
import Module.Driver as Driver
import tkinter.messagebox as messagebox


x = 0
y = 0
wh = 400
ww = 300
bgc = "#121212"
top_bgc = "#272727"
fbgc = "#1C1C1C"


def register(title, id, psd, name, login_btn):
        title.configure(text="註冊")
        name[0].place(x=40, y=180)
        name[1].place(x=110, y=180)
        id[0].place(x=40, y=230)
        id[1].place(x=110, y=230)
        psd[0].place(x=40, y=280)
        psd[1].place(x=110, y=280)
        login_btn.place(x=80, y=340, width=150, height=30)
        login_btn.configure(text="註冊")

def login(title, id, psd, name, login_btn):
        title.configure(text="登入")
        name[0].place_forget()
        name[1].place_forget()
        id[0].place(x=40, y=180)
        id[1].place(x=110, y=180)
        psd[0].place(x=40, y=230)
        psd[1].place(x=110, y=230)
        login_btn.place(x=80, y=320, width=150, height=30)
        login_btn.configure(text="登入")


def commit(var, _id, _psd, _name, browser, window):
        id = _id.get().strip()
        psd = _psd.get().strip()
        name = _name.get().strip()
        if var.get() == 1:
                if id != "" or psd != "":
                        user = Db.login(id, psd)
                        if user:
                                window.destroy()
                                Video.init(user, browser)
                        else:
                                messagebox.showerror("登入失敗", "帳號密碼錯誤!")
                else:
                        messagebox.showerror("登入失敗", "請勿空白!")
                
        else:
                if id != "" or psd != "" or psd != "":
                        user = Db.checkUser(id)
                        if user == None:
                                result = Db.register(id, psd, name)
                                if result:
                                        user = Db.login(id, psd)
                                        if user:
                                                window.destroy()
                                                Video.init(user, browser)
                                        else:
                                                messagebox.showerror("註冊失敗", "帳號密碼錯誤!")
                                else:
                                        messagebox.showerror("註冊失敗", "註冊過程出現錯誤!")
                        else:
                                messagebox.showerror("註冊失敗", "帳號已經被人使用!")
                else:
                        messagebox.showerror("註冊失敗", "請勿空白!")

def create(browser):

        window = tk.Tk()
        window.title('影片搜搜')
        ws = window.winfo_screenwidth() # width of the screen
        hs = window.winfo_screenheight() # height of the screen
        x = (ws/2) - (ww/2)
        y = (hs/2) - (wh/2)
        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
        window.resizable(False, False)
        window.configure(background=bgc)

        title = tk.Label(window, bg=bgc, text="登入", fg='#aaaaaa', font=('Arial', 40))
        id_lb = tk.Label(window, bg=bgc, text="帳號", fg='#aaaaaa', font=('Arial', 20))
        psd_lb = tk.Label(window, bg=bgc, text="密碼", fg='#aaaaaa', font=('Arial', 20))
        name_lb = tk.Label(window, bg=bgc, text="暱稱", fg='#aaaaaa', font=('Arial', 20))


        var = tk.IntVar()
        var.set(1)
        rb1 = tk.Radiobutton(window, text="登入", variable=var, value=1, bg="#adadad", selectcolor="#fcf5bf", indicatoron=0)
        rb2 = tk.Radiobutton(window, text="註冊", variable=var, value=2, bg="#adadad", selectcolor="#fcf5bf", indicatoron=0)


        name_tb = tk.Entry(window,
                                width=10, bg='#383838',
                                highlightbackground="#303030",
                                highlightthickness=2,
                                highlightcolor='#666666',
                                fg="white",
                                relief="flat",
                                font=('Verdana',18),
                                )

        id_tb = tk.Entry(window,
                                width=10, bg='#383838',
                                highlightbackground="#303030",
                                highlightthickness=2,
                                highlightcolor='#666666',
                                fg="white",
                                relief="flat",
                                font=('Verdana',18),
                                )

        psd_tb = tk.Entry(window,
                                width=10, bg='#383838',
                                highlightbackground="#303030",
                                highlightthickness=2,
                                highlightcolor='#666666',
                                fg="white",
                                relief="flat",
                                font=('Verdana',18),
                                show="*"
                                )



        login_btn = tk.Button(window, 
                                text="登入", 
                                fg='#373737', 
                                highlightbackground='#d8d8d8', 
                                highlightthickness=0,
                                )


        title.place(x=110, y=40)
        rb1.place(x=50, y=130, width=100)
        rb2.place(x=150, y=130, width=100)

        id_lb.place(x=40, y=180)
        id_tb.place(x=110, y=180)
        psd_lb.place(x=40, y=230)
        psd_tb.place(x=110, y=230)

        login_btn.place(x=80, y=320, width=150, height=30)



        rb1.bind("<Button-1>", lambda e: login(title, [id_lb, id_tb], [psd_lb, psd_tb], [name_lb, name_tb], login_btn))
        rb2.bind("<Button-1>", lambda e: register(title, [id_lb, id_tb], [psd_lb, psd_tb], [name_lb, name_tb], login_btn))
        login_btn.bind("<Button-1>", lambda e: commit(var, id_tb, psd_tb, name_tb, browser, window))
        window.bind('<Return>', lambda e: commit(var, id_tb, psd_tb, name_tb, browser, window))


        window.mainloop()
