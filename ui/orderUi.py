from services.orderService import orderService
from models.order import order
from services import carService

class orderUI():

    def __init__(self):
        self.__order_service = orderService()

    def menu(self):
        
        choice = ''
        while choice != 'q':
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press 3 to delete order")
            print("Press q to go back")

            choice = input("Choice a option: ").lower()
            
            if choice == '1':
                #orderID = input("Input orderID: ")
                carID = input("License plate number: ")
                #while carService.is_available(carID) != True:
                    #print("This vehicle is not available, please try again")
                    #carID = input("License plate number: ")
                # checka hvort fastanr sé til í lausir bílar
                customerSSN = input("Customer social security number: ") 
                # checka hvort það sé búið að skrá þennan
                dateOfHandover = input("Pick-up date (yy, mm, dd): ")
                returnDate = input("Return date: (yy, mm, dd)")
                extrainsurance = input("Extra insurance: (Yes/No)")
                orderTotal = input("Total Prize: ")
                new_order = order(orderID,dateOfHandover,returnDate,orderTotal)
                self.__order_service.add_order(new_order)

            elif choice == '2':
                orders = self.__order_service.get_order()
                print(orders)
            
            elif choice == "3":
                orders = self.__order_service.delete_order()