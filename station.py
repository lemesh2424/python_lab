from fuel import Fuel


class Station:
    def __init__(self, name):
        self.__name__ = name
        self.__fuelList__ = list()

    def add_fuel_type(self, fuel: Fuel):
        """
        Adds fuel type to the station

        >>> st = Station("St")
        >>> fuel = Fuel(98,200);
        >>> st.add_fuel_type(fuel)
        >>> fuel == st.__fuelList__.pop()
        True

        >>> st = Station("St")
        >>> fuel = Fuel(98,200);
        >>> fuel2 = Fuel(84,400);
        >>> st.add_fuel_type(fuel)
        >>> st.add_fuel_type(fuel2)
        >>> fuel2 == st.__fuelList__.pop() and fuel == st.__fuelList__.pop()
        True
        """
        exist = False
        for f in self.__fuelList__:
            if f.__name__ == fuel.__name__:
                f.__tank__ += fuel.__tank__
                exist = True

        if exist is False:
            self.__fuelList__.append(fuel)

    def spend_fuel(self, name, volume):
        """
        Spends fuel in fuel type in this station

        >>> st = Station("St")
        >>> st.add_fuel_type(Fuel(98,200))
        >>> st.spend_fuel(98,150)
        >>> st.__fuelList__.pop().__tank__
        50

        >>> st = Station("St")
        >>> st.add_fuel_type(Fuel(98,200))
        >>> st.spend_fuel(98,500)
        >>> st.__fuelList__.pop().__tank__
        0

        >>> st = Station("St")
        >>> st.add_fuel(Fuel(98,200))
        >>> st.spend_fuel(98,-30)
        >>> st.__fuelList__.pop().__tank__
        200
        """
        for f in self.__fuelList__:
            if f.__name__ == name:
                f.__tank__ -= volume
                if f.__tank__ <= 0:
                    f.__tank__ = 0

    def is_fuel(self, name):
        """
        Checks if fuel type is Named as in parameter
        :rtype: bool

        >>> st = Station("St")
        >>> st.add_fuel_type(Fuel(98,200))
        >>> st.is_fuel(98)
        True

        >>> st = Station("St")
        >>> st.add_fuel_type(Fuel(98,200))
        >>> st.is_fuel(923)
        False
        """
        for f in self.__fuelList__:
            if f.__name__ == name:
                return True
        return False

    def delete_fuel_type(self, name):
        """Deletes fuel type from station"""
        fuel_list = self.__fuelList__
        fuel_list = list(filter(lambda x: x.__name__ != name, fuel_list))
        self.__fuelList__ = fuel_list

    def show_formatted_fuel_list(self):
        """
        Shows list of all fuel types with their tank values
        :rtype: list

        >>> Station("St").show_formatted_fuel_list()
        []

        >>> st = Station("Stat")
        >>> st.add_fuel_type(Fuel(200,300))
        >>> st.show_formatted_fuel_list()
        ['\\n            Name: 200\\n            Fuel Volume: 300\\n            ']

        >>> st.add_fuel_type(Fuel(90,4000))
        >>> st.show_formatted_fuel_list()
        ['\\n            Name: 200\\n            Fuel Volume: 300\\n            ', '\\n            Name: 90\\n            Fuel Volume: 4000\\n            ']
        """
        output_list = list()
        for f in self.__fuelList__:
            description = """
            Name: {}
            Fuel Volume: {}
            """.format(f.__name__, f.__tank__)
            output_list.append(description)
        return output_list

    def is_empty(self):
        """Checks if station doesn't have any fuel
        :rtype: bool

        >>> Station("Stat").is_empty()
        True

        >>> st = Station("Stat")
        >>> st.add_fuel_type(Fuel(200,300))
        >>> st.is_empty()
        False
        """
        return len(self.__fuelList__) == 0
