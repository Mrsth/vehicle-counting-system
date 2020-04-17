#-------------------GENERAL LIBRARIES---------------------------------------------------------------------------
import numpy as np
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from connecting_to_db import dynamic_data_entry
from connecting_to_db import fetching_data
#--------------GENERAL LIBRARIES ENDS HERE-----------------------------------------------------------------------


#---------------------TKINTER LIBRARIES--------------------------------------------------------------------------
from tkinter import *
import PIL
from PIL import Image,ImageTk
import cv2
from tkinter import ttk
from tkinter import messagebox as msg

#-----------------TKINTER LIBRARIES ENDS HERE------------------------------------------------------------------------

#_____________________________CODING FOR ROOT_________________________________________________________________
root = Tk()
root.geometry("1000x600")
root.title("Vehicle Counting Application")
root.resizable(0,0)




#---------------------ADDING ICON------------------------------------------------------------------------------
icon=PhotoImage(file='caricon.png')
root.iconphoto(False,icon)
#----------------ADDING ICON ENDS HERE-------------------------------------------------------------------------

#-------------CODE FOR QUITTING WINDOW-------------------------------------------------------------------------
def quit():
    root.quit()
    root.destroy()
    exit()
#--------------------------------------------------------------------------------------------------------------    


#-------------------ADDING MENU ITEMS---------------------------------------------------------------------------
menu_bar=Menu(root)
root.config(menu=menu_bar)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Exit', command=quit)
menu_bar.add_cascade(label='File', menu=file_menu)

def about():
    msg.showinfo('About',' DEVELOPERS: MANISH SHREEV SUMESH PANDU')

help_menu=Menu(menu_bar,tearoff=0)
help_menu.add_command(label='About', command=about)
menu_bar.add_cascade(label='Help', menu=help_menu)
#------------------ADDING MENU ITEMS ENDS HERE-----------------------------------------------------------------



#-----------------------FRAME LAYOUT---------------------------------------------------------------------------
left = Frame(root, borderwidth=0,  width=600)
right = Frame(root, borderwidth=0)
right.config(background='light blue')
container = Frame(left, borderwidth=0, relief="solid")
box1 = Frame(right, borderwidth=0, relief="solid")
box1.config(background='white')
box2 = Frame(right, borderwidth=0, relief="solid")
box2.config(background='white')
box3= Frame(right, borderwidth=0, relief="solid")
box3.config(background='white')
box4= Frame(right, borderwidth=0, relief="solid")
box4.config(background='white')

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
container.pack(expand=True, fill="both", padx=5, pady=5)
box1.pack(expand=True, fill="both", padx=10, pady=10)
box2.pack(expand=True, fill="both", padx=10, pady=10)
box3.pack(expand=True, fill="both", padx=10, pady=10)
box4.pack(expand=True, fill="both", padx=10, pady=10)
#------------------FRAME LAYOUT ENDS HERE----------------------------------------------------------------------



#-----------------LOADING IMAGE ON CONTAINER FRAME--------------------------------------------------------------
img = Image.open("trafficback.png")
img = img.resize((400,400), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img)
label1 = Label(container, image=img1)
label1.pack()

#-----------LOADING IMAGE ON CONTAINER FRAME ENDS HERE---------------------------------------------------------




#-------------------------------------------------LOADING YOLO-------------------------------------------------
net = cv2.dnn.readNet("F:\easy detection\pysource\yolov3.weights", "F:\easy detection\pysource\yolov3.cfg")
classes = []
with open("F:\easy detection\pysource\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
#--------------------------------LOADING YOLO ENDS HERE--------------------------------------------------------


#------CODE FOR STARTING VIDEO---------------------------------------------------------------------------------
cap = cv2.VideoCapture("v1.mp4")
font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()


#-------CODE FOR STARTING VIDEO ENDS HERE----------------------------------------------------------------------



#--------------------------CODE FOR DETECTING VEHICLES STARTS HERE----------------------------------------------
def yolo():
    
    frame_id = 0
    _,frame = cap.read()
    frame_id +=1
    height, width, channels = frame.shape


    if _:
        #Detecting object
        blob = cv2.dnn.blobFromImage(frame, 0.00392,(416,416),(0,0,0),True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        #Showing information on the screen
        class_ids = np.array([])
        confidences = np.array([])
        boxes = []
        detected_object = np.array([])
        
        for out in outs: #OUTS CONTAINS ALL THE INFORMATION ABOUT OBJECTS DETECTED
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence>0.1:
                    #OBJECT DETECTED
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)
                    #RECTANGLE COORDINATES
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    boxes.append([x,y,w,h])
                    confidences = np.append(confidences,[confidence])
                    class_ids = np.append(class_ids,[class_id])

        indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(boxes)):
            if i in indexes:
                x,y,w,h = boxes[i]
                label =str(classes[int(class_ids[i])])
                detected_object=np.append(detected_object,[label])
                color = colors[i]
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,1)
                cv2.putText(frame,label,(x,y),font,1,color,2)
                seconds = time.time()
                local_time = time.ctime(seconds)
                cv2.putText(frame,local_time,(10,30),font,1,(0,255,255),1)
                
                total_length = len(detected_object)

                car = np.where(detected_object=="car")
                total_car = len(detected_object[car])

                motorbike = np.where(detected_object=="motorbike")
                total_motorbike = len(detected_object[motorbike])

                people = np.where(detected_object == "person")
                total_person = len(detected_object[people])

                bus = np.where(detected_object == "bus")
                total_bus = len(detected_object[bus])

                cycle = np.where(detected_object=="bicycle")
                total_cycle = len(detected_object[cycle])
                
                truck = np.where(detected_object=="truck")
                total_truck = len(detected_object[truck])
          
             
        
        print("Total object detected",len(detected_object))
        print(detected_object)
       
        
        

        lmain = Label(container)
        lmain.place(relx=0.1, rely=0.1)
        b = cv2.resize(frame, (350, 300), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        cv2image = cv2.cvtColor(b, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, yolo)
    dynamic_data_entry(local_time, total_length, total_car, total_motorbike, total_person, total_bus, total_cycle,total_truck)


#--------------------------CODE FOR DETECTING VEHICLES ENDS HERE-----------------------------------------------       
  

#------------------EMBEDDING BUTTON ON SCREEN------------------------------------------------------------------
button=ttk.Button(box1,text="livecamera",command=yolo).pack(expand=True)


label_1 = Label(box4,text="DATAS FROM DATABASE",font="arial 24 bold",bg='white').pack(expand=True)
#button=ttk.Button(box3,text="Show Graph").pack(expand=True)
#button=ttk.Button(box4,text="Notification").pack(expand=True)
#query_result = Label(box3, text=fetching_data).pack(expand=True)

#------------------EMBEDDING BUTTON ON SCREEN ENDS HERE------------------------------------------------------------------


#---------------------------CODE FOR SHOWING TABLE--------------------------------------------------------------

TableMargin = Frame(box4, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("SID", "Total time", "Total object", "Total car","Total bus","Total person","Total bike","Total cycle","Total truck"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('SID', text="SID", anchor=CENTER)
tree.heading('Total time', text="Total time", anchor=CENTER)
tree.heading('Total object', text="Total object", anchor=CENTER)
tree.heading('Total car',text="Total car", anchor=CENTER)
tree.heading('Total bus',text="Total bus", anchor=CENTER)
tree.heading('Total person',text="Total person", anchor=CENTER)
tree.heading('Total bike',text="Total bike", anchor=CENTER)
tree.heading('Total cycle',text="Total cycle", anchor=CENTER)
tree.heading('Total truck',text="Total truck", anchor=CENTER)
tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
tree.column('#1', stretch=NO, minwidth=0, width=50, anchor=CENTER)
tree.column('#2', stretch=NO, minwidth=0, width=150, anchor=CENTER)
tree.column('#3', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.column('#4', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.column('#5', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.column('#6', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.column('#7', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.column('#8', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.column('#9', stretch=NO, minwidth=0, width=100, anchor=CENTER)
tree.pack()
def call_data():
    fetched_data_result = fetching_data()
    #print("Data fetched",fetched_data_ko_result)

    for fetched_data in fetched_data_result:
        #label_1 = Label(box3,text=fetched_data).pack(expand=True)
        tree.insert("",0,values=(fetched_data))
        #print(fetched_data[1:-1])
        #tree.insert("",'end',text='display',values=(fetched_data))
button=ttk.Button(box2,text="Show Database",command=call_data).pack(expand=True)    
#---------------------------CODE FOR SHOWING TABLE ENDS HERE--------------------------------------------------------------

root.mainloop()
#________________________________CODE FOR ROOT ENDS HERE_______________________________________________________
