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
            print("---------------ORDERS---------------\n")
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press 3 to delete order")
            print("Press 4 to change a order")
            print("Press q to go back")

            choice = input("Choose an option: ").lower()
            
            if choice == '1':
                print("S for Sedan 10.000kr \nJ for Jeep 15.000kr \nL for Luxury 20.000kr")
                priceGroup = input("What type of car?: ").lower()
                carID = ""
                while carID == "":
                    while priceGroup != "s" and priceGroup != "j" and priceGroup != "l":
                        print("Try again")
                        priceGroup = input("Please choose S, J or L for car type: ").lower()
                    if priceGroup == "s":
                        priceGroup = "Sedan"
                    elif priceGroup == "j":
                        priceGroup = "Jeep"
                    elif priceGroup == "l":
                        priceGroup = "Luxury"
                    carID = self.__order_service.get_RandomAvailCar(priceGroup)
                    if carID == "":
                        print("There are no cars available in this price group.")
                    else:
                        print("CarID: " + carID)
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
                while dateOfHandover >= returnDate: 
                    print("Invalid dates, please try again.")
                    returnDate = input("Return date (dd/mm/yyyy): ")
                extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
                while extrainsurance != "y" and extrainsurance != "n":
                    print("Please enter Y or N!")
                    extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
                if extrainsurance == "y":
                    extrainsurance = "Yes"
                elif extrainsurance == "n":
                    extrainsurance = "No"
                cardnum = input("Enter a creditcard number: ")
                while len(cardnum) !=16:
                    print("Please enter a valid creditcard number!")
                    cardnum = input("Enter a creditcard number: ")
                print("Credit card (C), Debit card (D), Money (M)")
                paymentMethod = input("Payment method: ").lower()
                while paymentMethod != "c" and paymentMethod != "d" and paymentMethod != "m":
                    print("Try again")
                    print("Please input (c) for Credit card,(d) for Debit card and (m) for Money")
                    paymentMethod = input("Payment method: ").lower()
                if paymentMethod == "c":
                    paymentMethod = "Credit"
                elif paymentMethod == "d":
                    paymentMethod = "Debit"
                elif paymentMethod == "m":
                    paymentMethod = "Money"
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