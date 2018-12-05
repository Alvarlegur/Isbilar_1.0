from models.order import order

class orderRepo():
    def __init__(self):
        self.__order = []

    def add_order(self,order):
        with open ("./data/orders.txt", "a+") as orders_file:
            orderID = order.get_orderID()
            dateOfHandover = order.get_dateOfHandover()
            returnDate = order.get_returnDate()
            orderTotal = order.get_orderTotal()
            orders_file.write("{},{},{},{}\n".format(orderID,dateOfHandover, returnDate, orderTotal))

    def get_order(self):
        if self.__order == []:
            with open ("./data/orders.txt", "r") as orders_file:
                for line in orders_file.readlines():
                    orderID, dateOfHandover, returnDate, orderTotal = line.split(",")
                    all_orders = order(orderID, dateOfHandover, returnDate, orderTotal)
                    self.__order.append(all_orders)
                    
        return self.__order
            
    def delete_order(self):
        entername = str(input("Enter a order to delete: "))
        with open("./data/orders.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if not entername in i:
                    f.write(i)
            f.truncate()
