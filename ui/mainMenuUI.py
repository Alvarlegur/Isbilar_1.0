from ui.carUI import carUI
from ui.customerUi import customerUI
# from ui.orderUi import orderUi
import os


class mainMenuUI():
<<<<<<< HEAD
    def __init__(self):
        self.__carUI = carUI()
<<<<<<< HEAD
=======
>>>>>>> 5f528edcfb607cc02b9aae38f71790c6d1088c37
=======
>>>>>>> parent of dc973b2... s
>>>>>>> 1b18400455c391f5b422f37c0f95fd435e9343e6

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
