from services.orderService import orderService
from models.order import order

class orderUI():

    def __init__(self):
        self.__order_service = orderService

    def menu(self):
<<<<<<< HEAD
        choice = ""
        while choice != "q":
            print("press 1 to add order")
            print("press 2 to list all orders")
            choice = input("choose an option").lower()
            if choice == "1":
                
=======
        
        choice = ''
        while choice != 'q':
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press q to quit")

            choice = input("Choice a option: ").lower()
            
            if choice == '1':
                orderID = input("Input orderID: ")
                carID = input("Input carID: ")
                customerID = input("Input customerID: ")
                dateOfHandover = input("Pick-up date: ")
                returnDate = input("Return date: ")
                orderTotal = input("Total Prize: ")
                new_order = order(orderID, carID, customerID,dateOfHandover,returnDate,orderTotal)
                self.__order_service.add_order(new_order)

            elif choice == '2':
                orders = self.__order_service.get_order()
                print(orders)
>>>>>>> 6df2f98e08bb17e7f49819bb3b40dfa5617113a2
