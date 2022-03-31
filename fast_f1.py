import fastf1
import random as rnd
import matplotlib.pyplot as plt
fastf1.Cache.enable_cache("A:\cache")
year = int(input("Wich Year"))
race_number = int(input("Wich race? (number)"))
qualy_session = fastf1.get_session(year, race_number, "Qualifying")
race_session = fastf1.get_session(year, race_number, "Race")
qualy_session.load()
race_session.load()
schedule = fastf1.get_event_schedule(2022)
print(race_session.)
# driver_number = []
# position = []
# for i in session.results.Q3:
#     driver_number.append[]
a = []
b =  []
number = 0
for index in race_session.results.FullName:
    a.append(number)
    number +=1
number = 0
for index in qualy_session.results.FullName:
    b.append(number)
    number += 1
    
plot = plt.plot(race_session.results.Abbreviation, a, "or")
plot2 = plt.plot(qualy_session.results.Abbreviation, b, "or")
plot2
plot
plt.xlabel(None)
plt.ylabel(None)
plt.tight_layout()
plt.xscale = 1
plt.grid(True)
plt.colormaps()
plt.setp(plot, 'color', 'r', 'linewidth', 2)
plt.setp(plot2, 'color', 'g', 'linewidth', 0.1)
plt.show()