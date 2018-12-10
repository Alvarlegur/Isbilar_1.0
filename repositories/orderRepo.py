from models.order import order
from models.car import car

class orderRepo():
    def __init__(self):
        self.__order = []
        self.__car = car()

    def add_order(self,order):
        with open ("./data/orders.csv", "a+") as orders_file:
            orderID = order.get_orderID()
            carID = order.get_carID()
            
            customerSSN = order.get_customerSSN()
            dateOfHandover = order.get_dateOfHandover()
            returnDate = order.get_returnDate()
            extraInsurance = order.get_extraInsurance()
            orderTotal = order.get_orderTotal()
            orders_file.write("{},{},{},{},{},{},{}\n".format(orderID,carID, customerSSN, dateOfHandover, returnDate, extraInsurance, orderTotal))

    def get_order(self):
        if self.__order == []:
            with open ("./data/orders.csv", "r") as orders_file:
                for line in orders_file.readlines():
                    orderID, dateOfHandover, returnDate, extraInsurance, orderTotal = line.split(",")
                    all_orders = order(orderID,dateOfHandover,returnDate,orderTotal,extraInsurance)
                    self.__order.append(all_orders)
                    
        return self.__order
            
    def delete_order(self):
        entername = str(input("Enter orders ID: "))
        with open("./data/orders.csv", "r+") as orders_file:
            temp = orders_file.readlines()
            orders_file.seek(0)
            for line in temp:
                if not entername in line:
                    orders_file.write(line)
            orders_file.truncate()
