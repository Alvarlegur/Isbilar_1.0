from ui.carUI import carUI
from ui.customerUi import customerUI
<<<<<<< HEAD
from ui.orderUi import orderUI
=======
from ui.orderUi import orderUi
>>>>>>> 6df2f98e08bb17e7f49819bb3b40dfa5617113a2
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
<<<<<<< HEAD
            elif choice == "3":
                ui3 = orderUI
                orderUI.menu()
            else:
                print("please try again")
=======

            if choice == "3":
                ui3 = orderUI()
                ui3.menu()
>>>>>>> 6df2f98e08bb17e7f49819bb3b40dfa5617113a2
