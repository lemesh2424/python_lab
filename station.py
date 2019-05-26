from fuel import Fuel

class Station:
    def __init__(self, name):
        self.__name__ = name
        self.__fuelList__ = list()

    def addFuel(self, fuel: Fuel):
        exist = False
        for f in self.__fuelList__:
            if f.__name__ == fuel.__name__:
                f.__tank__ += fuel.__tank__
                exist = True
        
        if exist == False:
            self.__fuelList__.append(fuel)

    def spentFuel(self, name, volume):
        for f in self.__fuelList__:
            if f.__name__ == name:
                f.__tank__ -= volume

    def isFuel(self, name):
        for f in self.__fuelList__:
            if f.__name__ == name:
                return True
        return False

    def deleteFuel(self, name):
        self.__fuelList__ = list(filter(lambda x: x.__name__ != name, self.__fuelList__))
    
    def showFormattedFuelList(self):
        output_list = list()
        for f in self.__fuelList__:
            description = """
            Name: {}
            Fuel Volume: {}
            """.format(f.__name__, f.__tank__)
            output_list.append(description)
        return output_list

    def isEmpty(self):
        return len(self.__fuelList__) == 0

