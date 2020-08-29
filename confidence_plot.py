import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

df = pd.read_csv('confidence_plot.csv')

bike = df.loc[df["Type"]=="motorbike"]
car = df.loc[df["Type"]=="car"]
bus = df.loc[df["Type"]=="bus"]
truck = df.loc[df["Type"]=="truck"]
cycle = df.loc[df["Type"]=="bicycle"]

#print(bike[0:6], car[0:6], bus[0:6], truck[0:6], cycle[0:6])

# only_bike = bike[0:6]

t_cycle = len(cycle)
t_car = len(car)
t_bus = len(bus)
t_truck = len(truck)
t_bike = len(bike)

print("Total cycle = ", t_cycle)
print("Total car = ", t_car)
print("Total bus = ", t_bus)
print("Total truck = ", t_truck)
print("Total bike = ", t_bike)


# print(car[0:6])
# print(bus[0:6])
# print(truck[0:6])

Max_bike_confidence = bike.confidence_value.max()
Min_bike_confidence = bike.confidence_value.min()

Max_car_confidence = car.confidence_value.max()
Min_car_confidence = car.confidence_value.min()

Max_bus_confidence = bus.confidence_value.max()
Min_bus_confidence = bus.confidence_value.min()

Max_truck_confidence = truck.confidence_value.max()
Min_truck_confidence = truck.confidence_value.min()

Max_cycle_confidence = cycle.confidence_value.max()
Min_cycle_confidence = cycle.confidence_value.min()

max_list = [Max_bike_confidence, Max_bus_confidence, Max_car_confidence, Max_truck_confidence]
min_list = [Min_bike_confidence, Min_bus_confidence, Min_car_confidence, Min_truck_confidence]



print("Max bike confidence = ",Max_bike_confidence,"%", "\t Min bike confidence = ", Min_bike_confidence,"%")
print("Max car confidence = ",Max_car_confidence,"%"," \t Min car confidence = ", Min_car_confidence,"%")
print("Max bus confidence = ",Max_bus_confidence,"%"," \t Min bus confidence = ", Min_bus_confidence,"%")
print("Max truck confidence = ",Max_truck_confidence,"%"," \t Min truck confidence = ", Min_truck_confidence,"%")
print("Max cycle confidence = ",Max_cycle_confidence,"%"," \t Min cycle confidence = ", Min_cycle_confidence,"%")

max_sum = int(Max_bike_confidence) + int(Max_bus_confidence )+ int(Max_car_confidence )+ int(Max_cycle_confidence) + int(Max_truck_confidence)
max_mean = max_sum/5
print("Max confidence average = ", max_mean)

min_sum = int(Min_bike_confidence) + int(Min_bus_confidence )+ int(Min_car_confidence )+ int(Min_cycle_confidence) + int(Min_truck_confidence)
min_mean = min_sum/5
print("Min confidence average = ", min_mean) 




# only_car = df.loc[df["Type"]=="car"][0:2]
# print(only_car.confidence_value)

# h_bike = bike.head(20)
# h_car = car.head(20)
# h_bus = bus.head(20)
# h_truck = truck.head(20)
# h_cycle = cycle.head(20)

# plt.bar(h_bike.Type,h_bike.confidence_value)
# plt.bar(h_car.Type, h_car.confidence_value)
# plt.bar(h_bus.Type, h_bus.confidence_value)
# plt.bar(h_truck.Type, h_truck.confidence_value)
# plt.bar(h_cycle.Type, h_cycle.confidence_value)



# plt.plot(h_car.confidence_value, h_car.Type, 'bo')
# plt.plot(h_bike.confidence_value, h_bike.Type, 'bo')
# plt.plot(h_bus.confidence_value, h_bus.Type, 'bo')
# plt.plot(h_truck.confidence_value, h_truck.Type, 'bo')
# plt.plot(h_cycle.confidence_value, h_cycle.Type, 'bo')

# plt.xticks(rotation=90)

# plt.show()





