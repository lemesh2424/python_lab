from serialization import Serialization
from fuel import Fuel


class Menu:
    def __init__(self, station):
        self.__station__ = station

    def print_menu(self):
        """
        Function that creates UI in terminal
        """
        print("_______MENU_______\n")
        print('[a]dd fuel')
        print('[s]pent certain fuel from station')
        print('[d]elete fuel')
        print('[i]mport to JSON')
        print('[e]xport from JSON')
        print("[p]rint station")
        print('[q]uit')
        print("input option: ")

    def start(self):
        """
        Creates the UI of the station
        """
        option = ''
        while option != 'q':
            self.print_menu()
            option = input()

            print('\n' * 80)

            if option == 'a':
                self.option_add()
            elif option == 's':
                self.option_spend()
            elif option == 'd':
                self.option_delete()
            elif option == 'i':
                self.option_save()
            elif option == 'e':
                self.option_load()
            elif option == 'p':
                self.option_print()
            elif option == 'q':
                print("BYE!")
                pass
            else:
                print("Input menu option")

            print('\n' * 3)

    def option_add(self):
        """
        Creates UI for adding new fuel type
        """
        print("Input fuel name")
        name = input()

        if self.__station__.is_fuel(name):
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
            self.__station__.add_fuel(Fuel(name, tank))
            print("Successfully added!")
        else:
            print("Tank must a number!")

    def option_spend(self):
        """
        Creates UI for spending fuel from certain fuel type
        """
        self.option_print()
        print("\n\nInput fuel name that you want to spend: ")
        name = input()
        if self.__station__.is_fuel(name):
            print("Input spending volume")
            volume = input()
            try:
                volume = int(volume)
            except ValueError:
                print("Volume must be a number!")
                return
            self.__station__.spend_fuel(name, volume)
            print("Spent!")
        else:
            print("Fuel with name " + name + " not found")

    def option_delete(self):
        """
        Creates UI for deleting fuel type from station
        """
        self.option_print()
        print("\n\nInput fuel name that you want to delete: ")
        name = input()
        if self.__station__.is_fuel(name):
            self.__station__.delete_fuel(name)
        else:
            print("Fuel with name " + name + " not found")

    def option_load(self):
        """
        Loads station from Json file
        """
        s = Serialization()
        self.__station__ = s.load()
        print('Successfully imported')

    def option_save(self):
        """
        Saves station to Json file
        """
        s = Serialization()
        s.save(self.__station__)
        print('Successfully exported')

    def option_print(self):
        """
        Creates UI with information about all fuel types
        """
        print("#########")

        if self.__station__.is_empty():
            print("Station is empty")
        else:
            formatted_list = self.__station__.show_formatted_fuel_list()

            for f in formatted_list:
                print(f)

        print("#########")
