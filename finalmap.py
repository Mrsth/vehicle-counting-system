from tkinter import *
import tkinter as tk
import webview
from tkinter import messagebox as msg
import tkinter.font as tkFont
from tkinter import ttk
from PIL import Image,ImageTk
from cefpython3 import cefpython as cef
import sys


#loading images
btngo= Image.open("F:\easy detection\MeroGUI\VCA\Img\go.jpg")
btngo = ImageTk.PhotoImage(btngo)
applogo3 = Image.open("F:\easy detection\MeroGUI\VCA\Images\App_frame.png")
applogo3 = applogo3.resize((70,50), Image.ANTIALIAS)
applogo3= ImageTk.PhotoImage(applogo3)

# MAP
def map():
    # button_map.config(state=tk.DISABLED)
    googlewin = tk.Toplevel()

    ww = 300
    hh = 200
    wss = googlewin.winfo_screenwidth()
    hss = googlewin.winfo_screenheight()
    xx = (wss / 2) - (ww / 2)
    yy = (hss / 7) - (hh / 7)
    googlewin.geometry('%dx%d+%d+%d' % (ww, hh, xx, yy))
    googlewin.title('MAP')
    googlewin.resizable(0, 0)

    

    # # adding icon
    # icon = tk.PhotoImage(file="F:\easy detection\MeroGUI\VCA\Images\App_logo.png")
    # googlewin.iconphoto(True, icon)

    # # frames
    frame_upper = tk.Frame(googlewin, bg='#1889C8')
    frame_upper.place(relx=0, rely=0, relheight=0.2, relwidth=1)
    frame_lower = tk.Frame(googlewin, bg='#1889C8')
    frame_lower.place(relx=0, rely=0.85, relheight=0.15, relwidth=1)
    main_frame = tk.Frame(googlewin, bg='white')
    main_frame.place(relx=0, rely=0.2, relheight=0.65, relwidth=1)

    # labels
    labelgmap = tk.Label(frame_upper, text='Google Map', bg='#1889C8', fg='white',
                         font=tkFont.Font(family='arial', size=14, weight='bold'))
    labelgmap.pack(pady=8)
    labelchoice = tk.Label(main_frame, text='Choose the Location', bg='white',
                           font=tkFont.Font(family='arial', size=10, weight='bold'))
    labelchoice.place(relx=0.1, rely=0.1)
    label_logo = tk.Label(main_frame, image=applogo3, border=0)
    label_logo.place(relx=0.68, rely=0.3)


    # combo box
    map_name = tk.StringVar()
    map_combo = ttk.Combobox(main_frame, width=20, textvariable=map_name)
    map_combo['values'] = ('foliumap')
    map_combo.place(relx=0.1, rely=0.3, relheight=0.2)

    def show():
        name = (map_name.get())
        if (name == 'foliumap'):
            googlewin.destroy()
            sys.excepthook = cef.ExceptHook
            cef.Initialize()
            cef.CreateBrowserSync(url="F:\easy detection\MeroGUI\VCA\\foliumap.html", window_title="Hello World!")
            cef.MessageLoop()
            button_map.config(state=tk.NORMAL)
           
        else:
            msg.showerror('Error : ', 'Sorry!! We do not have this location ')

    # buttons
    btn = tk.Button(main_frame, image=btngo, command=show, border=0, bg='white').place(relx=0.09, rely=0.65)
    # webview.create_window('MAP','https://www.google.com/')
    # webview.start()




# def map():
#     sys.excepthook = cef.ExceptHook
#     cef.Initialize()
#     cef.CreateBrowserSync(url="F:\easy detection\MeroGUI\VCA\\foliumap.html", window_title="Hello World!")
#     cef.MessageLoop()
    # cef.Shutdown()
