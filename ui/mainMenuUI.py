from .carUI import carUI
from .customerUi import customerUI
from .orderUi import orderUi
import os


class mainMenuUI():

    def menu(self):
        choice = ""
        clear = lambda: os.system('cls')
        while choice != "q":
            print("Press 1 for Cars")
            print("Press 2 for Customers")
            print("Press 3 for Orders")
            print("Press q to quit")
            choice = input("choose an option: ").lower()
            clear()
            if choice == "1":
                ui = carUI()
                ui.menu()
            elif choice == "2":
                ui2 = customerUI()
                ui2.menu()

            elif choice == "3":
                ui3 = orderUI()
                ui3.menu()
            else:
                print("please try again")
