import json
from station import Station
from fuel import Fuel


class Serialization:
    
    def save(self, station: Station):
        """Saves the station into Json file

        >>> st = Station("station")
        >>> st.add_fuel_type(Fuel("95",20))
        >>> Serialization().save(st)
        >>> ser = Serialization().load()
        >>> ser.__name__
        'station'
        >>> st.__name__ = "AYAYAY"
        >>> Serialization().save(st)
        >>> ser = Serialization().load()
        >>> ser.__name__
        'AYAYAY'
        """

        fuel_list = station.__fuelList__
        obj = {"name": station.__name__, "fuel": list(
            map(lambda x: {"name": x.__name__, "tank": x.__tank__}, fuel_list))}

        with open("data.json", "w") as outfile:
            json.dump(
                obj,
                outfile,
                ensure_ascii=False,
                indent=4,
                sort_keys=True)

    def load(self):
        """
        Loads the station from Json file

        >>> st = Station("station")
        >>> st.add_fuel_type(Fuel("95",20))
        >>> Serialization().save(st)
        >>> ser = Serialization().load()
        >>> ser.__fuelList__.__getitem__(0).__name__
        '95'
        >>> ser.__fuelList__.__getitem__(0).__tank__
        20
        >>> ser.__name__
        'station'
        """
        with open("data.json") as f:
            d = json.load(f)
            fuel_list = list()
            for f in d["fuel"]:
                fuel_list.append(Fuel(f["name"], f["tank"]))
            station = Station(d["name"])
            station.__fuelList__ = fuel_list
        return station

    def load_json(self):
        """
        Loads Json from file
        :return: JSON formatted string
        >>> st = Station("Test station")
        >>> st.add_fuel_type(Fuel("95",20))
        >>> Serialization().save(st)
        >>> Serialization().load_json()
        {'fuel': [{'name': '95', 'tank': 20}], 'name': 'Test station'}

        >>> st = Station("Next Test station")
        >>> Serialization().save(st)
        >>> Serialization().load_json()
        {'fuel': [], 'name': 'Next Test station'}

        >>> st = Station("")
        >>> Serialization().save(st)
        >>> Serialization().load_json()
        {'fuel': [], 'name': ''}
        """
        with open("data.json") as f:
            return json.load(f)
