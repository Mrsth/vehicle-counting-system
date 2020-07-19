import sqlite3
sqlite3.sqlite_version
from matplotlib import pyplot as plt
import itertools
from matplotlib.animation import FuncAnimation
import time
import schedule
import pandas as pd
import datetime


conn = sqlite3.connect('CSVDB1.db')
c= conn.cursor()


'''c.execute("""  
    CREATE TABLE record(
        SID integer integer PRIMARY KEY NOT NULL,
        Total_time datetime NOT NULL,
        Total_object integer NOT NULL,
        Total_car integer NOT NULL,
        Total_bus integer NOT NULL,
        Total_person integer NOT NULL,
        Total_bike integer NOT NULL,
        Total_cycle integer NOT NULL,
        Total_truck integer NOT NULL
    )
""")
'''


def dynamic_data_entry(only_year, total_length, total_person ,total_car, total_motorbike, total_bus, total_cycle, total_truck):
    c.execute("INSERT INTO record (Total_time,Total_object,Total_car,Total_bus, Total_person, Total_bike, Total_cycle, Total_truck) VALUES (?,?,?,?,?,?,?,?)", 
    (only_year, total_length, total_car ,total_bus, total_person, total_motorbike, total_cycle, total_truck) )

    conn.commit()

def fetching_data():
    c.execute("SELECT * FROM record")
    records = c.fetchall()
    # delete_records()

    print_records = []
    for r in records:
        print_records.append(r)

    return(print_records) 







conn.commit()