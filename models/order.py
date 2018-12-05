# from models.car import car
# from models.customer import customer

class order:
    #initalizing order instance
    #vantar að tengja carID og customerID inn í orders
    def __init__(self, orderID, carID, customerID, dateOfHandover, returnDate, orderTotal):
        self.__orderID = orderID
        # self.__carID = car.getcarID()
        # self.__customerID = customer.getSSN()
        self.__dateOfHandover = dateOfHandover
        self.__returnDate = returnDate
        self.__orderTotal = orderTotal

    def __str__(self):
        return (self.__orderID, self.__carID, self.__customerID,self.__dateOfHandover, self.__returnDate)

    def get_orderID(self):
        return self.__orderID

    def get_carID(self):
        return self.__carID

    def get_customerID(self):
        return self.__customerID

    def get_dateOfHandover(self):
        return self.__dateOfHandover

    def get_returnDate(self):
        return self.__returnDate

    def get_orderTotal(self):
        return self.__orderTotal
