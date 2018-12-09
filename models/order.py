from models.car import car
from models.customer import customer
from datetime import timedelta
from models.priceGroup import priceGroup

class order:
    #initalizing order instance
    #vantar að tengja carID og customerID inn í orders
    def __init__(self, orderID,dateOfHandover, returnDate, orderTotal,extraInsurance):
        self.__orderID = id(orderID)
        self.__dateOfHandover = dateOfHandover
        self.__returnDate = returnDate
        self.__orderTotal = orderTotal
        self.__extrainsurance = extraInsurance

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{} \n".format(self.__orderID,self.__dateOfHandover, self.__returnDate, self.__extrainsurance, self.__orderTotal)

    # def get_orderID(self):
    #     return self.__orderID


    def get_orderID(self):
        return self.__orderID

    def get_dateOfHandover(self):
        return self.__dateOfHandover

    def get_returnDate(self):
        return self.__returnDate

    def get_extraInsurance(self):
        return self.__extrainsurance

    def get_orderTotal(self):
        return self.__orderTotal

    def __repr__(self):
        return self.__str__()
    
    #def totalPrice(self):
        #timeDelta = (datetime.timedelta(self.__returnDate) - datetime.timedelta(self.__dateOfHandover))
        #print(timeDelta)

