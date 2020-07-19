from tkinter import *
import tkinter as tk
import numpy as np
import PIL
from PIL import Image,ImageTk
import cv2
from tkinter import ttk
global warning_label
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import webview
from finalmap import map
from cefpython3 import cefpython as cef
import sys
import datetime 
global flag, dt_main, main_time


#1889C8


from connecting_to_db import dynamic_data_entry
from connecting_to_db import fetching_data
import itertools

from tkinter import messagebox as msg
import tkinter.font as tkFont
import sqlite3
import time as tm
global cap

# Load Yolo
net = cv2.dnn.readNet("F:\easy detection\MeroGUI\VCA\yolov3.weights", "F:\easy detection\MeroGUI\VCA\yolov3.cfg")
classes = []
with open("F:\easy detection\MeroGUI\VCA\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

conn = sqlite3.connect('CSVDB1.db')
c= conn.cursor()

 

def clear():
    database = r"CSVDB1.db"
    name = (c.execute("SELECT Total_time FROM record Limit 1"))
    rows = c.fetchall()
    df = pd.DataFrame(rows)
    time = df[0].tolist()  # making the row as list

    finaltime = time[0]  # extracting the date
    year = int(finaltime[:4])  # slicing to get year
    month = int(finaltime[5:7])  # slicing to get month
    day = int(finaltime[8:10])  # slicing to get day
    past = datetime.date(year, month, day)  # converting it into datetime format
    today = datetime.date.today()  # current date
    age = (today - past)  # the days difference
    return age

try:
    number=clear()
    print(number)
    count=datetime.timedelta(5)
    print(count)
    if(number>=count):
        c.execute("DELETE FROM record")
        conn.commit()  
except:
    print("Empty database.")


def disable_event():
    msg.askokcancel('Logout INFO','Please logout to close the window')
    
root=tk.Toplevel()
root.title('Vehicle Counting Application')
w=1100
h=690
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=0
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
root.resizable(0,0)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.config(background="white")





#loading necessary images
logo = Image.open("F:\easy detection\MeroGUI\VCA\Images\App_logo.png")
logo = logo.resize((40,40), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
bicycle = Image.open("F:\easy detection\MeroGUI\VCA\Images\cycle2.jpg")
bicycle = bicycle.resize((80,80), Image.ANTIALIAS)
bicycle1 = ImageTk.PhotoImage(bicycle)
bike = Image.open("F:\easy detection\MeroGUI\VCA\Images\Bike.png")
bike = bike.resize((80,80), Image.ANTIALIAS)
bike1 = ImageTk.PhotoImage(bike)
car = Image.open("F:\easy detection\MeroGUI\VCA\Images\car.png")
car = car.resize((80,80), Image.ANTIALIAS)
car1 = ImageTk.PhotoImage(car)
bus = Image.open("F:\easy detection\MeroGUI\VCA\Images\Bus.png")
bus = bus.resize((80,80), Image.ANTIALIAS)
bus1 = ImageTk.PhotoImage(bus)
truck = Image.open("F:\easy detection\MeroGUI\VCA\Images\Truck.png")
truck = truck.resize((80,80), Image.ANTIALIAS)
truck1 = ImageTk.PhotoImage(truck)


btncam = Image.open("F:\easy detection\MeroGUI\VCA\Img\showcam.jpg")
btncam = ImageTk.PhotoImage(btncam)
btnabout = Image.open("F:\easy detection\MeroGUI\VCA\Img\\about.jpg")
btnabout = ImageTk.PhotoImage(btnabout)
btnendcam = Image.open("F:\easy detection\MeroGUI\VCA\Img\endcam.jpg")
btnendcam = ImageTk.PhotoImage(btnendcam)
btnshowdb = Image.open("F:\easy detection\MeroGUI\VCA\Img\db.jpg")
btnshowdb = ImageTk.PhotoImage(btnshowdb)
btnlogout = Image.open("F:\easy detection\MeroGUI\VCA\Img\logout.jpg")
btnlogout = ImageTk.PhotoImage(btnlogout)
btngraph=Image.open("F:\easy detection\MeroGUI\VCA\Img\showgraph.jpg")
btngraph=ImageTk.PhotoImage(btngraph)
btnmap=Image.open("F:\easy detection\MeroGUI\VCA\Img\showmap.jpg")
btnmap=ImageTk.PhotoImage(btnmap)
logoframe = Image.open("F:\easy detection\MeroGUI\VCA\Images\App_frame.png")
logoframe = logoframe.resize((int(w*0.35),int(h*0.35)), Image.ANTIALIAS)
logoframe1 = ImageTk.PhotoImage(logoframe)



#adding image
group = Image.open("F:\easy detection\MeroGUI\VCA\Image\Final About.png")
group= group.resize((650,690), Image.ANTIALIAS)
group = ImageTk.PhotoImage(group)
      

def about():
    button_abt.config(state=tk.DISABLED)
    def enableabt():
        button_abt.config(state=tk.NORMAL)
        about.destroy()
    about=tk.Toplevel()
    about.title('Vehicle Counting Application')
    w=650
    h=690
    ws=about.winfo_screenwidth()
    hs=about.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=0
    about.geometry('%dx%d+%d+%d'%(w,h,x,y))
    about.resizable(0,0)
    #adding icon
    # icon=tk.PhotoImage(file="F:\easy detection\MeroGUI\VCA\Images\App_logo.png")
    # about.iconphoto(True,icon)
    #adding label to put the image
    label=tk.Label(about,image=group)
    about.protocol("WM_DELETE_WINDOW", enableabt)
    label.pack()

def logout():
    ans=msg.askokcancel('Logout INFO','Are you sure you want to logout?')
    if(ans==True):
        root.destroy()
        exit()

#font style
font_welcome=tkFont.Font(family='arial',size='20',weight='bold')
font_root=tkFont.Font(family='arial',size='15',weight='bold')
font_total=tkFont.Font(family='arial',size='15',weight='bold')

root_label=tk.Label(root,text="Space for live cam",font=font_root,background='white').place(relx=0.4)
warning_label = tk.Label(root,font=font_root,background='white', fg="red")
warning_label.place(relx=0.645)
time=tk.Label(root,font=font_root,background='white')
time.place(relx=0.88)

#adding frames in root
left_frame=tk.Frame(root,background='#1889C8')   # PURANO USED COLOR DAEEF3
logo_label=tk.Label(left_frame,image=logo1,background='#1889C8').place(relx=0.1,rely=0.02)
label1=tk.Label(left_frame,text="Welcome to Falcon",foreground='white',background='#1889C8',font=font_welcome).place(relx=0.23,rely=0.025)
inside_frame=tk.Frame(left_frame,background='white')
heading_label=tk.Label(inside_frame,text="DataBase",font=font_welcome,background='white').pack(pady=7)
inside_frame.place(relwidth=0.98,relheight=0.74,relx=0.01,rely=0.1)
left_frame.place(relwidth=0.38,relheight=1,relx=0,rely=0)

frame_right=tk.Frame(root,background='#F2F2F2',border=0)
labelframe=tk.Label(frame_right,image=logoframe1,background='#F2F2F2').pack(pady=70)
projectname=tk.Label(frame_right,text='Falcon',font=font_welcome,background='#F2F2F2').place(relx=0.43,rely=0.78)
cap=cv2.VideoCapture(1)
lmain = tk.Label(frame_right)
lmain.place(relx=0,rely=0)
def clock():
    current_time=tm.strftime('%I:%M:%S%p')
    time['text']=current_time
    root.after(1000,clock)


            


tree = ttk.Treeview(inside_frame, columns=("Total time", "Total object", "Total car","Total bus","Total person","Total bike","Total cycle","Total truck"), show='headings', height=22)    

def database():
  
    #tree = ttk.Treeview(inside_frame, columns=("SID", "Total time", "Total object", "Total car","Total bus","Total person","Total bike","Total cycle","Total truck"), show='headings', height=18)
    treeScroll = ttk.Scrollbar(inside_frame, orient=tk.VERTICAL)
    treeScroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.place(relx=0.96,rely=0.09,relheight=1)

    #tree.heading('SID', text="SID")
    tree.heading('Total time', text="Time")
    tree.heading('Total object', text="Total")
    tree.heading('Total car',text="Car")
    tree.heading('Total bus',text="Bus")
    tree.heading('Total person',text="Person")
    tree.heading('Total bike',text="Bike")
    tree.heading('Total cycle',text="Cycle")
    tree.heading('Total truck',text="Truck")


    tree.column('#0', stretch=False, minwidth=0, width=0,anchor=CENTER)
    tree.column('#1', stretch=False, minwidth=0, width=115,anchor=CENTER) #time
    tree.column('#2', stretch=False, minwidth=0, width=43,anchor=CENTER) #obj
    tree.column('#3', stretch=False, minwidth=0, width=30,anchor=CENTER) #car
    tree.column('#4', stretch=False, minwidth=0, width=35,anchor=CENTER) #bus
    tree.column('#5', stretch=False, minwidth=0, width=50,anchor=CENTER) #person
    tree.column('#6', stretch=False, minwidth=0, width=38,anchor=CENTER) #bike
    tree.column('#7', stretch=False, minwidth=0, width=42,anchor=CENTER) #cycle
    tree.column('#8', stretch=False, minwidth=0, width=43,anchor=CENTER)
    #tree.column('#9', stretch=False, minwidth=0, width=100)
    tree.place(relx=0.0,rely=0.09)
   

def show_data():
    tree.delete(*tree.get_children())
    fetched_data_result = fetching_data()
    for fetched_data in fetched_data_result:
        #label_1 = Label(box3,text=fetched_data).pack(expand=True)
        tree.insert("",0,values=(fetched_data))

database() 

    

# loading image
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

canvas_1 = tk.Canvas(root, bg="white", highlightthickness=0)
canvas_2 = tk.Canvas(root, bg="white", highlightthickness=0)

now = datetime.datetime.now()
main_time=now.strftime("%Y-%m-%d %H:%M:%S")
dt_main=now.strptime(main_time,"%Y-%m-%d %H:%M:%S")
flag=1

def yolo():
    # loading image
    #cap = cv2.VideoCapture(0)
    #font = cv2.FONT_HERSHEY_PLAIN
    global flag, dt_main, main_time
    button_cam.config(state=tk.DISABLED)
    frame_id = 0
    _, frame = cap.read()
    frame_id += 1
    height, width, channels = frame.shape
    total_length = 0
    total_person = 0
    total_bus = 0
    total_car = 0
    total_cycle = 0
    total_motorbike = 0
    total_truck = 0
    if _:
        # Detecting object
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = np.array([])
        confidences = np.array([])
        boxes = []
        detected_object = np.array([])

        for out in outs:  # OUTS CONTAINS ALL THE INFORMATION ABOUT OBJECTS DETECTED
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if (class_id == 1 or class_id == 2 or class_id == 5 or class_id == 7 or class_id == 3) and confidence > 0.3:
                    # OBJECT DETECTED
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # RECTANGLE COORDINATES
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences = np.append(confidences, [confidence])
                    class_ids = np.append(class_ids, [class_id])

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[int(class_ids[i])])
                detected_object = np.append(detected_object, [label])
                color = colors[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y), font, 1, color, 2)
             
                total_length = len(detected_object)

                #total_length = len(detected_object)

                car = np.where(detected_object == "car")
                total_car = len(detected_object[car])
                carlabel['text'] = total_car

                motorbike = np.where(detected_object == "motorbike")
                total_motorbike = len(detected_object[motorbike])
                bikelabel['text'] = total_motorbike

                people = np.where(detected_object == "person")
                total_person = len(detected_object[people])

                bus = np.where(detected_object == "bus")
                total_bus = len(detected_object[bus])
                buslabel['text'] = total_bus

                cycle = np.where(detected_object == "bicycle")
                total_cycle = len(detected_object[cycle])
                bilabel['text'] = total_cycle

                truck = np.where(detected_object == "truck")
                total_truck = len(detected_object[truck])
                trucklabel['text'] = total_truck

        #carlabel['text'] = total_car
        b = cv2.resize(frame, (700, 450), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        cv2image = cv2.cvtColor(b, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(100, lambda: yolo())
        
    #FOR NOTIFICATION
    x = "test";
    if (flag==1):
        traffic=False       
        if total_truck>=5 and total_motorbike>=20 and total_bus>=5 and total_cycle>=10 and total_car>=25:
            popup_traffic("HIGH TRAFFIC")
            x = "high"
            canvas_1.create_oval(5,5,30,30,fill="green",outline="green")
            canvas_1.place(relx=0.57,rely=0, relwidth=0.035, relheight=0.05)

            canvas_2.create_oval(5,5,30,30,fill="green",outline="green")
            canvas_2.place(relx=0.84,rely=0, relwidth=0.035, relheight=0.05)

        elif total_truck<=5 and total_motorbike<=20 and total_bus<=5 and total_cycle<=10 and total_car<=20:
            popup_traffic("MEDIUM TRAFFIC")
            x = "medium"
            canvas_1.create_oval(5,5,30,30,fill="yellow",outline="yellow")
            canvas_1.place(relx=0.57,rely=0, relwidth=0.035, relheight=0.05)

            canvas_2.create_oval(5,5,30,30,fill="yellow",outline="yellow")
            canvas_2.place(relx=0.84,rely=0, relwidth=0.035, relheight=0.05)

        elif total_truck<=2 and total_motorbike<=10 and total_bus<=3 and total_cycle<=10 and total_car<=15:
            popup_traffic("LOW TRAFFIC") 
            x = "low"
            canvas_1.create_oval(5,5,30,30,fill="red",outline="red")
            canvas_1.place(relx=0.57,rely=0, relwidth=0.035, relheight=0.05)

            canvas_2.create_oval(5,5,30,30,fill="red",outline="red")
            canvas_2.place(relx=0.84,rely=0, relwidth=0.035, relheight=0.05)   
            traffic=True
        elif total_truck == 0 and total_motorbike == 0 and total_bus == 0 and total_cycle == 0 and total_car == 0:
            popup_traffic("NO TRAFFIC")
            x = "no" 

    if total_truck>=5 and total_motorbike>20 and total_bus>=5 and total_cycle>=20 and total_car>=20:
        popup_traffic("HIGH TRAFFIC")
        x = "high"
    elif total_truck>2 and total_motorbike>10 and total_bus>3 and total_cycle>10 and total_car>15:
        popup_traffic("MEDIUM TRAFFIC")
        x = "medium"           
    elif total_truck<=2 and total_motorbike<=10 and total_bus<=3 and total_cycle<=10 and total_car<=15:
        popup_traffic("LOW TRAFFIC") 
        x = "low"
    elif total_truck == 0 and total_motorbike == 0 and total_bus == 0 and total_cycle == 0 and total_car == 0:
        popup_traffic("NO TRAFFIC") 
        x = "no"    
    
    now1 = datetime.datetime.now()
    sec_time=now1.strftime("%Y-%m-%d %H:%M:%S")
    dt_sec=now1.strptime(sec_time,"%Y-%m-%d %H:%M:%S")
    print("Dt_Second = ",dt_sec)
    print("Dt_main_Second = ",dt_main)
    time_diff = dt_sec-dt_main 
    second=time_diff.seconds        
    print("Second = ",second)
        
    named_tuple = tm.localtime() # get struct_time
    time_string = tm.strftime("%Y/%m/%d,%H:%M:%S", named_tuple)
    only_year = tm.strftime("%Y/%m/%d", named_tuple)

    if (second>10):
        if(x=="high"):
            canvas_1.create_oval(5,5,30,30,fill="green",outline="green")
            canvas_1.place(relx=0.57,rely=0, relwidth=0.035, relheight=0.05)
    
            canvas_2.create_oval(5,5,30,30,fill="green",outline="green")
            canvas_2.place(relx=0.84,rely=0, relwidth=0.035, relheight=0.05)

            now2 = datetime.datetime.now()
            main_time=now2.strftime("%Y-%m-%d %H:%M:%S")
            dt_main=now2.strptime(main_time,"%Y-%m-%d %H:%M:%S")
        elif(x=="medium"):
            canvas_1.create_oval(5,5,30,30,fill="yellow",outline="yellow")
            canvas_1.place(relx=0.57,rely=0, relwidth=0.035, relheight=0.05)

            canvas_2.create_oval(5,5,30,30,fill="yellow",outline="yellow")
            canvas_2.place(relx=0.84,rely=0, relwidth=0.035, relheight=0.05)

            now3 = datetime.datetime.now()
            main_time=now3.strftime("%Y-%m-%d %H:%M:%S")
            dt_main=now3.strptime(main_time,"%Y-%m-%d %H:%M:%S")
        elif(x=="low"):
            canvas_1.create_oval(5,5,30,30,fill="red",outline="red")
            canvas_1.place(relx=0.57,rely=0, relwidth=0.035, relheight=0.05)

            canvas_2.create_oval(5,5,30,30,fill="red",outline="red")
            canvas_2.place(relx=0.84,rely=0, relwidth=0.035, relheight=0.05)

            now4 = datetime.datetime.now()

            main_time=now4.strftime("%Y-%m-%d %H:%M:%S")
            dt_main=now4.strptime(main_time,"%Y-%m-%d %H:%M:%S")
        elif (x=="no"):
            popup_traffic("NO TRAFFIC") 

   
    flag=2
    #timeclock=tm.strftime('%I:%M:%S')
    # seconds = tm.time()
    dynamic_data_entry(time_string, total_length, total_person ,total_car, total_motorbike, total_bus, total_cycle, total_truck)    

frame_right.place(relheight=0.6,relwidth=0.6,relx=0.39,rely=0.05)

    


frame_b=tk.Frame(root,background='white')

label_bicycle=tk.Label(frame_b,image=bicycle1,border=0)
label_bicycle.place(relx=0.05,rely=0.05)

label_bike=tk.Label(frame_b,image=bike1,border=0)
label_bike.place(relx=0.25,rely=0.05)


label_car=tk.Label(frame_b,image=car1,border=0)
label_car.place(relx=0.45,rely=0.05)

label_bus=tk.Label(frame_b,image=bus1,border=0)
label_bus.place(relx=0.65,rely=0.05)

label_truck=tk.Label(frame_b,image=truck1,border=0)
label_truck.place(relx=0.85,rely=0.05)


tk.Label(frame_b,text='Total',font=font_total,background='white').place(relx=0.07,rely=0.5)
tk.Label(frame_b,text='Total',font=font_total,background='white').place(relx=0.27,rely=0.5)
tk.Label(frame_b,text='Total',font=font_total,background='white').place(relx=0.47,rely=0.5)
tk.Label(frame_b,text='Total',font=font_total,background='white').place(relx=0.67,rely=0.5)
tk.Label(frame_b,text='Total',font=font_total,background='white').place(relx=0.87,rely=0.5)

font_total_number=tkFont.Font(family='arial',size='15')
bilabel=tk.Label(frame_b,text='0',font=font_total_number,background='white')
bilabel.place(relx=0.10,rely=0.7)

bikelabel=tk.Label(frame_b,text='0',font=font_total_number,background='white')
bikelabel.place(relx=0.30,rely=0.7)

carlabel=tk.Label(frame_b,text='0',font=font_total_number,background='white')
carlabel.place(relx=0.50,rely=0.7)

buslabel=tk.Label(frame_b,text='0',font=font_total_number,background='white')
buslabel.place(relx=0.70,rely=0.7)

trucklabel=tk.Label(frame_b,text='0',font=font_total_number,background='white')
trucklabel.place(relx=0.91,rely=0.7)

frame_b.place(relwidth=0.6,relheight=0.25,relx=0.39,rely=0.75)

def graph():
    button_graph.config(state=tk.DISABLED)
    def enable():
        button_graph.config(state=tk.NORMAL)
        graphwin.destroy()
    conn = sqlite3.connect('CSVDB1.db')
    # create a database connection
    cur = conn.cursor()
    cur.execute("SELECT * FROM record")
    rows = cur.fetchall()
    # list = [i.replace('(','') for i in rows]
    df = pd.DataFrame(rows)
    time = df[0].tolist()
    total = df[1].tolist()
    car = df[2].tolist()
    bus = df[3].tolist()
    person = df[4].tolist()
    bike = df[5].tolist()
    cycle = df[6].tolist()
    truck = df[7].tolist()
    


    # car = df[1].tolist()
    # bike = df[2].tolist()
    # bus = df[3].tolist()
    # cycle = df[4].tolist()
    # truck = df[5].tolist()

    # --------------------------------------------------------------
    fig = Figure(figsize=(10, 6), facecolor='white')
    # --------------------------------------------------------------
    axis = fig.add_subplot(111)
    axis.set_title("Graph plot of different vehicles and their count")
    t0, = axis.plot(time, car)
    t1, = axis.plot(time, bike)
    t2, = axis.plot(time, bus)
    t3, = axis.plot(time, cycle)
    t4, = axis.plot(time, truck)
    # axis.xticks(rotation=90)
    axis.set_ylabel('COUNT')
    axis.set_xlabel('TIME')
    axis.xaxis.set_major_locator(plt.MaxNLocator(4))
    # axis.set_xticklabels(time, rotation=45, ha='right')
    axis.grid()
    fig.legend((t0, t1, t2, t3, t4), ('CAR', 'BIKE', 'BUS', 'CYCLE', 'TRUCK'), 'upper right')

    graphwin = tk.Toplevel()
    graphwin.protocol("WM_DELETE_WINDOW", enable)

    canvas = FigureCanvasTkAgg(fig, master=graphwin)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    graphwin.update()
    graphwin.deiconify()

# MAP
#loading images
btngo= Image.open("F:\easy detection\MeroGUI\VCA\Img\go.jpg")
btngo = ImageTk.PhotoImage(btngo)
applogo3 = Image.open("F:\easy detection\MeroGUI\VCA\Images\App_frame.png")
applogo3 = applogo3.resize((70,50), Image.ANTIALIAS)
applogo3= ImageTk.PhotoImage(applogo3)
def map():
    button_map.config(state=tk.DISABLED)
    googlewin = tk.Toplevel()

    def show():
        name = (map_name.get())
        
        if (name == 'kalanki' or name=='kalimati' or name=='ktm' or name=='lalitpur' or name=='baneshwor' or name=='tinkune' or name=='bhaktapur'):
            googlewin.destroy()
            #sys.excepthook = cef.ExceptHook
            cef.Initialize()
            cef.CreateBrowserSync(url='F:\easy detection\MeroGUI\VCA\\' +name+'.html',window_title=name)
            cef.MessageLoop() 
            button_map.config(state=tk.NORMAL)                              
        else:
            msg.showerror('Error : ', 'Sorry!! We do not have this location ')

    ww = 300
    hh = 200
    wss = googlewin.winfo_screenwidth()
    hss = googlewin.winfo_screenheight()
    xx = (wss / 2) - (ww / 2)
    yy = (hss / 7) - (hh / 7)
    googlewin.geometry('%dx%d+%d+%d' % (ww, hh, xx, yy))
    googlewin.title('MAP')
    googlewin.resizable(0, 0)


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
    map_combo['values'] = ('ktm','lalitpur','bhaktapur','kalanki','kalimati','baneshwor','tinkune')
    map_combo.place(relx=0.1, rely=0.3, relheight=0.2)



    # buttons
    btn = tk.Button(main_frame, image=btngo, command=show, border=0, bg='white').place(relx=0.09, rely=0.65)
    # webview.create_window('MAP','https://www.google.com/')
    # webview.start()







#buttons
# button_cam1=tk.Button(root,image=btn11,border=0,bg='white',command=yolo).place(relx=0.41,rely=0.67)
# button_cam2=tk.Button(root,text='End CAM',image=btn13,border=0,bg='white',command=lambda :quit(lmain)).place(relx=0.61,rely=0.67)
# button_cam3=tk.Button(root,text='About System',image=btn12,border=0,bg='white',command=about).place(relx=0.81,rely=0.67)
# button_cam4=tk.Button(left_frame,text='Show DB',image=btn14,border=0,bg='#1889C8',command=show_data).place(relx=0.04,rely=0.87)
# button_cam5=tk.Button(left_frame,text='Logout',image=btn15,border=0,bg='#1889C8',command=logout).place(relx=0.5,rely=0.87)

#buttons
button_cam=tk.Button(root,image=btncam,border=0,bg='white',command=lambda: yolo())
button_cam.place(relx=0.4,rely=0.67)
button_endcam=tk.Button(root,image=btnendcam,border=0,bg='white',command=lambda :quit(lmain))
button_endcam.place(relx=0.544,rely=0.67)
button_map=tk.Button(root,image=btnmap,border=0,bg='white',command=map)
button_map.place(relx=0.688,rely=0.67)
button_graph=tk.Button(root,image=btngraph,border=0,bg='white',command=graph)
button_graph.place(relx=0.832,rely=0.67)
button_db=tk.Button(left_frame,image=btnshowdb,border=0,bg='#1889C8',command=show_data)
button_db.place(relx=0.04,rely=0.85)
button_abt=tk.Button(left_frame,image=btnabout,border=0,bg='#1889C8',command=about)
button_abt.place(relx=0.055,rely=0.92)
button_logout=tk.Button(left_frame,image=btnlogout,border=0,bg='#1889C8',command=logout)
button_logout.place(relx=0.5,rely=0.92)





def popup_traffic(a):
    global warning_label
    warning_label['text']= a
    print(a)  


    
    
def popup_new():
    #msg.showinfo("Information","hope you took diversion and detecting vehicles again from zero")
    print("Information","hope you took diversion and detecting vehicles again from zero")



def quit(widget):
    global lmain,cap
    global warning_label
    button_cam.config(state=tk.NORMAL)
    widget.destroy()
    lmain = tk.Label(frame_right)
    lmain.place(relx=0,rely=0)
    carlabel['text'] = 0
    bikelabel['text'] = 0
    buslabel['text'] = 0
    bilabel['text'] = 0
    trucklabel['text'] = 0
    warning_label ['text']= " "

    canvas_1.create_oval(5,5,30,30,fill="white",outline="white")
    canvas_1.place(relx=0.6,rely=0, relwidth=0.035, relheight=0.05)

    canvas_2.create_oval(5,5,30,30,fill="white",outline="white")
    canvas_2.place(relx=0.82,rely=0, relwidth=0.035, relheight=0.05)
    
    cap.release()
    cap=cv2.VideoCapture(0)
clock()


