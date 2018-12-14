from services.orderService import orderService
from models.order import order
from services import carService
from services.customerService import customerService
from ui.customerUi import customerUI
from services.inputCheck import *

class orderUI():

    def __init__(self):
        self.__order_service = orderService()
        self.__customer_service = customerService()
        self.__custUI = customerUI()

    def menu(self):
        
        choice = ''
        while choice != 'q':
            print("---------------ORDERS---------------\n")
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press 3 to delete order")
            print("Press 4 to change a order")
            print("Press q to go back")

            choice = input("Choose an option: ").lower()
            
            if choice == '1':
                print("\nS for Sedan 10.000kr \nJ for Jeep 15.000kr \nL for Luxury 20.000kr")
                priceGroup = checkPriceGroup()
                carID = ""
                while carID == "":
                    carID = self.__order_service.get_RandomAvailCar(priceGroup)
                    if carID == "":
                        print("There are no cars available in this price group.")
                        priceGroup = checkPriceGroup()
                    else:
                        print("CarID: " + carID)
                customerSSN = checkSSN()
                while self.__customer_service.customerExists(customerSSN) != True:
                    print("Please try again \nYou can also press N to register new customer")
                    customerSSN = input("Enter a registered SSN: ").upper()
                    if customerSSN == 'N':
                        self.__custUI.menu()
                print("Pick-up date (dd-mm-yyyy)")
                dateOfHandover = checkDate()
                print("Return date (dd-mm-yyyy)")
                returnDate = checkDate()
                while checkDatetime(dateOfHandover, returnDate): 
                    print("Invalid dates, please try again.")
                    print("Pick-up date (dd-mm-yyyy)")
                    dateOfHandover = checkDate()
                    print("Return date (dd-mm-yyyy)")
                    returnDate = checkDate()
                extrainsurance = checkInsurance()
                cardnum = checkCardnum()
                paymentMethod = checkPaymentMethod()
                new_order = order(carID, customerSSN, priceGroup, dateOfHandover, returnDate, extrainsurance, cardnum, paymentMethod)
                self.__order_service.add_order(new_order)

            elif choice == '2':
                orders = self.__order_service.get_order()
                for allOrders in orders:
                    print(allOrders)
             
            elif choice == "3":
                orders = self.__order_service.delete_order()
            
            elif choice == "4":
                orders = self.__order_service.changeOrder()