from ui.carUI import carUI
from ui.customerUi import customerUI
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

            if choice == "2":
                ui2 = customerUI()
                ui2.menu()