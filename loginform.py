import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
import PIL
from PIL import Image,ImageTk
import cv2


root = tk.Tk()
root.title('Vehicle Counting APP')
w = 550
h = 350
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 7) - (h / 7)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0,0)
root.config(background='#1889C8')
#adding icon
icon=tk.PhotoImage(file="F:\easy detection\MeroGUI\VCA\Images\App_logo.png")
root.iconphoto(True,icon)

#logo image
img_logo = Image.open("F:\easy detection\MeroGUI\VCA\Image\\toplogin3.png")
img_logo = img_logo.resize((40,40), Image.ANTIALIAS)
img1_logo = ImageTk.PhotoImage(img_logo)
img_login = Image.open("F:\easy detection\MeroGUI\VCA\Image\Login.jpg")
img1_login1 = ImageTk.PhotoImage(img_login)
applogo = Image.open("F:\easy detection\MeroGUI\VCA\Images\\app_frame.jpg")
applogo = applogo.resize((160,100), Image.ANTIALIAS)
applogo = ImageTk.PhotoImage(applogo)


def create_window():
    root.withdraw()
    import secondwin

def check():
    if(name.get()=='trafficapp' and password.get()=='vehicle32'):
        create_window()
    elif(name.get()=='trafficapp' and password.get()!='vehicle32'):
        msg.showerror('Error : ', 'Invalid Password ')
    elif (name.get() != 'trafficapp' and password.get() == 'vehicle32'):
        msg.showerror('Error : ', ' Ivalid UserName')
    else:
        msg.showerror('Error : ', ' Ivalid UserName And Password')

fontStyle_login = tkFont.Font(family="arial", size=25,weight='bold')
fontStyle_other=tkFont.Font(family="arial", size=13,weight='bold')
fontStyle_button=tkFont.Font(family="arial", size=15,weight='bold')
label2=tk.Label(root,text='LOGIN',font=fontStyle_login,foreground='white',background='#1889C8')
label2.place(relx=0.38,rely=0.03)
label1_logo = tk.Label(root, image=img1_logo,border=0)
label1_logo.place(relx=0.58,rely=0.03)
frame_inner=tk.Frame(root,borderwidth=1,relief="solid",background='white')
applogo_label=tk.Label(frame_inner,image=applogo,border=0)
applogo_label.place(relx=0.1,rely=0.2)
pname=tk.Label(frame_inner,text='Falcon',bg='white',font=fontStyle_button).place(relx=0.19,rely=0.63)

user=tk.Label(frame_inner,text='UserName:',foreground='#1889C8',font=fontStyle_other,background='white').place(relx=0.5,rely=0.1)
pas=tk.Label(frame_inner,text='Password:',foreground='#1889C8',font=fontStyle_other,background='white').place(relx=0.5,rely=0.4)

#Adding Entry
name=tk.StringVar()
User_name=tk.Entry(frame_inner,width=35,textvariable=name,foreground='#1889C8')
User_name.place(relx=0.5,rely=0.2,height=25)
password=tk.StringVar()
Pass_word=ttk.Entry(frame_inner,width=35,textvariable=password,show='*',foreground='#1889C8')
Pass_word.place(relx=0.5,rely=0.5,height=25)

#button
button_login=tk.Button(frame_inner,image=img1_login1,command=check,border=0,bg='white')
button_login.place(relx=0.5,rely=0.75)
frame_inner.place(relwidth=1,relheight=0.7,relx=0,rely=0.15)

label3=tk.Label(root,text='Note:Username and Password requried',foreground='white',background='#1889C8',font=fontStyle_other)
label3.place(relx=0.25,rely=0.9)


root.mainloop()