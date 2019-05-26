from serialization import Serialization
from menu import Menu

s = Serialization()


station = s.load()

m = Menu(station)
m.start()
