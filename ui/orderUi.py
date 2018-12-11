from services.orderService import orderService
from models.order import order
from services import carService
from services.customerService import customerService
from ui.customerUi import customerUI

class orderUI():

    def __init__(self):
        self.__order_service = orderService()
        self.__customer_service = customerService()
        self.__custUI = customerUI()

    def menu(self):
        
        choice = ''
        while choice != 'q':
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press 3 to delete order")
            print("Press 4 to change a order")
            print("Press q to go back")

            choice = input("Choose an option: ").lower()
            
            if choice == '1':
                print("F for Folksbill 10.000kr \nJ for Jeppi 15.000kr \nL for Luxusbill 20.000kr")
                priceGroup = input("What type of car?: ").capitalize()
                while priceGroup != "F" and priceGroup != "J" and priceGroup != "L":
                    print("Try again")
                    priceGroup = input("Please choose F, J or L for car type: ").capitalize()
                carID = self.__order_service.get_RandomAvailCar(priceGroup)
                customerSSN = input("Customer social security number: ").upper()
                while self.__customer_service.customerExists(customerSSN) != True:
                    print("Please try again \nYou can also press N to register new customer")
                    customerSSN = input("Enter a registered SSN: ").upper()
                    if customerSSN == 'N':
                        self.__custUI.menu()
                dateOfHandover = input("Pick-up date (dd/mm/yyyy): ")
                while len(dateOfHandover) != 10:
                    print("Please enter a valid date!")
                    dateOfHandover = input("Pick-up date (dd/mm/yyyy): ")
                returnDate = input("Return date (dd/mm/yyyy): ")
                while len(returnDate) !=10:
                    print("Please enter a valid date!")
                    returnDate = input("Return date (dd/mm/yyyy): ")
                extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
                while extrainsurance != "y" and extrainsurance != "n":
                    print("Please enter Y or N!")
                    extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
                if extrainsurance == "y":
                    extrainsurance = "Yes"
                elif extrainsurance == "n":
                    extrainsurance = "No"
                new_order = order(carID, customerSSN, priceGroup, dateOfHandover,returnDate, extrainsurance)
                self.__order_service.add_order(new_order)

            elif choice == '2':
                orders = self.__order_service.get_order()
                print(orders)
            
            elif choice == "3":
                orders = self.__order_service.delete_order()
            
            elif choice == "4":
                orders = self.__order_service.changeOrder()