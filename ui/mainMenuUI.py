from ui.carUI import carUI


class mainMenuUI():
    def __init__(self):
        self.__carUI = carUI()

    
    def menu(self):
        choice = ""
        while choice != "q":
            print("Press 1 for Cars")
            print("Press 2 for Customers")
            print("Press 3 for Orders")
            print("Press q to quit")
            choice = input("choose an option: ").lower()

            if choice == "1":
                ui = carUI()
                ui.menu()
