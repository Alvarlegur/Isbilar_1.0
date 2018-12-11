from services.orderService import orderService
from models.order import order
from services import carService
from services.customerService import customerService

class orderUI():

    def __init__(self):
        self.__order_service = orderService()
        self.__customer_service = customerService()

    def menu(self):
        
        choice = ''
        while choice != 'q':
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press 3 to delete order")
            print("Press q to go back")

            choice = input("Choose an option: ").lower()
            
            if choice == '1':
                print("F for Folksbill 10.000kr \n J for Jeppi 15.000kr \n L for Luxusbill 20.000kr")
                priceGroup = input("What type of car?: ").capitalize()
                while priceGroup != "F" and priceGroup != "J" and priceGroup != "L":
                    print("Try again")
                    priceGroup = input("Please choose F, J or L for car type: ").capitalize()
                carID = self.__order_service.get_RandomAvailCar(priceGroup)
                customerSSN = input("Customer social security number: ") 
                while self.__customer_service.customerExists(customerSSN) != False:
                    print("Please try again")
                    customerSSN = input("Enter a registered SSN: ")
                dateOfHandover = input("Pick-up date (dd/mm/yyyy): ")
                while len(dateOfHandover) != 10:
                    print("Please enter a valid date!")
                    dateOfHandover = input("Pick-up date (dd/mm/yyyy): ")
                returnDate = input("Return date (dd/mm/yy): ")
                while len(returnDate) !=10:
                    print("Please enter a valid date!")
                    returnDate = input("Return date (dd/mm/yy): ")
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