from services.orderService import orderService
from models.orders import orders

class orderUI():
    def __init__(self):
        self.__orderService = orderService()

    def menu(self):
        choice = ""
        while choice != "q":
            print("press 1 to add order")
            print("press 2 to list all orders")
            choice = input("choose an option").lower()
            if choice == "1":
                