from ui.carUI import carUI
from ui.customerUi import customerUI
from ui.orderUi import orderUI
import os


class mainMenuUI():
    def __init__(self):
        self.__carUI = carUI()

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
