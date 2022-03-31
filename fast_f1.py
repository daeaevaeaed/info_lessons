import fastf1
import random as rnd
import matplotlib.pyplot as plt
fastf1.Cache.enable_cache("A:\cache")
session = fastf1.get_session(2022, 2, "Q")
session.load()
# driver_number = []
# position = []
# for i in session.results.Q3:
#     driver_number.append[]
a = []
number = 1
for index in session.results.FullName:
    print(index)
    a.append(number)
plot = plt.plot(a, session.results.Abbreviation, "or")
plot
plt.xlabel(None)
plt.ylabel(None)
plt.tight_layout()
plt.xscale = 1
plt.grid(True)
plt.colormaps()
plt.setp(plot, 'color', 'g', 'linewidth', 1.0)
plt.show()
print(session.results.columns)