import json
from station import Station
from fuel import Fuel

class Serialization:
    def save(self, station: Station):
        obj = {
            "name": station.__name__,
            "fuel": list(map(lambda x: {"name": x.__name__, "tank": x.__tank__}, station.__fuelList__ ))
        }

        with open("data.json", "w") as outfile:
            json.dump(obj, outfile, ensure_ascii=False, indent=4, sort_keys=True)

    def load(self):
        station = None
        with open("data.json") as f:
            d = json.load(f)
            fuelList = list()
            for f in d["fuel"]:
                fuelList.append(Fuel(f["name"], f["tank"]))
            station = Station(d["name"])
            station.__fuelList__ = fuelList
        return station
            