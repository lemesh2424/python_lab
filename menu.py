from station import Station
from serialization import Serialization
from fuel import Fuel


class Menu:
    def __init__(self, station):
        self.__station__ = station

    def print(self):
        option = ''
        while True:
            print("_______MENU_______\n")
            print('[a]dd fuel')
            print('[s]pent fuel from some station')
            print('[d]elete fuel')
            print('[i]mport to JSON')
            print('[e]xport from JSON')
            print("[p]rint station")
            print('[e]xit')
            print("input option: ")
            option = input()

            print('\n' * 80)

            if option == 'a':
                self.optionAdd()
            elif option == 's':
                self.optionSpent()
            elif option == 'd':
                self.optionDelete()
            elif option == 'i':
                self.optionSave()
            elif option == 'e':
                self.optionLoad()
            elif option == 'p':
                self.optionPrint()
            elif option == 'e':
                print("BYE!")
                return
            else:
                print("Input menu option")

            print('\n' * 3)

    def optionAdd(self):
        print("Input fuel name")
        name = input()

        if self.__station__.isFuel(name):
            print('Fuel already exist')
            return

        print("Input fuel tank")
        tank = input()
        try:
            tank = int(tank)
        except ValueError:
            print("Tank must be a number!")
            return

        if type(tank) == int:
            self.__station__.addFuel(Fuel(name, tank))
            print("Successfully added!")
        else:
            print("Tank must a number!")

    def optionSpent(self):
        self.optionPrint()
        print("\n\nInput fuel name that you want to spent: ")
        name = input()
        if self.__station__.isFuel(name):
            print("Input spending volume")
            volume = input()
            try:
                volume = int(volume)
            except ValueError:
                print("Volume must be a number!")
                return
            self.__station__.spentFuel(name, volume)
            print("Spent!")
        else:
            print("Fuel with name " + name + " not found")

    def optionDelete(self):
        self.optionPrint()
        print("\n\nInput fuel name that you want to delete: ")
        name = input()
        if self.__station__.isFuel(name):
            self.__station__.deleteFuel(name)
        else:
            print("Fuel with name " + name + " not found")

    def optionLoad(self):
        s = Serialization()
        self.__station__ = s.load()
        print('Successfully exported')

    def optionSave(self):
        s = Serialization()
        s.save(self.__station__)
        print('Successfully imported')

    def optionPrint(self):
        print("#########")

        if self.__station__.isEmpty():
            print("Station is empty")
        else:
            formattedList = self.__station__.showFormattedFuelList()

            for f in formattedList:
                print(f)

        print("#########")
