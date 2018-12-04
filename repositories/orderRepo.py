from models.order import order

class orderRepo():
    def __init__(self):
        self.__order = []

    def add_order(self,order):
        with open ("./data/orders.txt", "a+") as orders_file:
            orderID = order.get_orderID()
            carID = order.get_carID()
            customerID = order.get_customerID()
            dateOfHandover = order.get_dateOfHandover()
            returnDate = order.get_returnDate()
            orderTotal = order.get_orderTotal()
            orders_file.write("{},{},{},{},{},{}\n".format(orderID, carID, customerID, dateOfHandover, returnDate, orderTotal))
            
