from station import Station
from fuel import Fuel
from serialization import Serialization
from menu import Menu


#
# station.addFuel(Fuel("95", 1000))
# station.addFuel(Fuel("98", 2000))
# station.addFuel(Fuel("100", 2000))
#
# station.deleteFuel("98")
#
# station.spentFuel("95", 200)
#
# formattedList = station.showFormattedFuelList()
#
# for f in formattedList:
#     print(f)
#
# s.save(station)

s = Serialization()

station = s.load()

m = Menu(station)
m.print()
