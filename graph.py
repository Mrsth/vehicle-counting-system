import pandas as pd
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.font as tkFont
from matplotlib import pyplot as plt


conn = sqlite3.connect('CSVDB1.db')
# create a database connection
cur = conn.cursor()
cur.execute("SELECT * FROM record")
rows=cur.fetchall()
#list = [i.replace('(','') for i in rows]
df=pd.DataFrame(rows)
time=df[0].tolist()
car=df[1].tolist()
bike=df[2].tolist()
bus=df[3].tolist()
cycle=df[4].tolist()
truck=df[5].tolist()

#--------------------------------------------------------------
fig = Figure(figsize=(10, 6), facecolor='white')
#--------------------------------------------------------------
axis = fig.add_subplot(111)
axis.set_title("Graph plot of different vehicles and their count")
t0, = axis.plot(time, car)
t1, = axis.plot(time, bike)
t2, = axis.plot(time, bus)
t3, = axis.plot(time, cycle)
t4, = axis.plot(time, truck)
#axis.xticks(rotation=90)
axis.set_ylabel('COUNT')
axis.set_xlabel('TIME')
#axis.set_xticklabels(time, rotation=90, ha='right')
axis.xaxis.set_major_locator(plt.AutoLocator())
axis.grid()
fig.legend((t0, t1, t2, t3, t4), ('CAR', 'BIKE', 'BUS','CYCLE','TRUCK'), 'upper right')

#--------------------------------------------------------------
def _destroyWindow():
    root.quit()
    root.destroy()
#--------------------------------------------------------------
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)
#--------------------------------------------------------------
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#--------------------------------------------------------------
root.update()
root.deiconify()
root.mainloop()








