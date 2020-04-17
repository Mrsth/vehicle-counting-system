import sqlite3
sqlite3.sqlite_version
from plotting_graph import read_from_db
from matplotlib import pyplot as plt
import itertools
from matplotlib.animation import FuncAnimation


conn = sqlite3.connect('CSVDB.db')
c= conn.cursor()

#c.execute("INSERT INTO recording VALUES (1,'person','1')")

def dynamic_data_entry(seconds,totallength,total_car, total_motorbike, total_person, total_bus, total_cycle,total_truck):
    c.execute("INSERT INTO recording (time,total,total_car,total_bus, total_person, total_bike, total_cycle, total_truck) VALUES (?,?,?,?,?,?,?,?)", (seconds,totallength,total_car,total_bus,total_person,total_motorbike,total_cycle,total_truck))
    conn.commit()


def fetching_data():
    c.execute("SELECT * FROM recording")
    records = c.fetchall()
    #time_data = list(itertools.chain(*time_fetched_data))
    #print("Time data = ",time_data)
    #print("Fetching data hai guys = ",records)

    print_records = []
    for record in records:
        print_records.append(record)
        #print(print_records) 
    return(print_records)   


    '''c.execute("SELECT total_car FROM recording")
    car_fetched_data = c.fetchall()
    car_data = list(itertools.chain(*car_fetched_data))
    print("Car data = ",car_data) 

    c.execute("SELECT total_bus FROM recording")
    bus_fetched_data = c.fetchall()
    bus_data = list(itertools.chain(*bus_fetched_data))
    print("Bus data = ",bus_data)'''


conn.commit()
#conn.close()