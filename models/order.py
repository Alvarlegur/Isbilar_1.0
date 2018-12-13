from models.car import car
from models.customer import customer
from datetime import datetime
import csv

class order:
    def __init__(self, carID, customerSSN ,priceGroup, dateOfHandover, returnDate, extraInsurance, cardnum, paymentMethod):
        self.__orderID = id(self)
        self.__carID = carID
        self.__priceGroup = priceGroup
        self.__customerSSN = customerSSN
        self.__dateOfHandover = dateOfHandover
        self.__returnDate = returnDate
        self.__extraInsurance = extraInsurance
        self.__orderTotal = self.totalPrice()
        self.__cardnum = cardnum
        self.__paymentMethod = paymentMethod

    def __str__(self):
        return "\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t\t{:>5}\t\t{:>5}\n".format(self.__carID,self.__customerSSN, self.__dateOfHandover, self.__returnDate, self.__extraInsurance, self.__cardnum, self.__paymentMethod)

    def get_orderID(self):
        return self.__orderID

    def get_carID(self):
        return self.__carID
    
    def get_customerSSN(self):
        return self.__customerSSN

    def get_dateOfHandover(self):
        return self.__dateOfHandover

    def get_returnDate(self):
        return self.__returnDate

    def get_extraInsurance(self):
        return self.__extraInsurance
    
    def get_cardnum(self):
        return self.__cardnum

    def get_paymentMethod(self):
        return self.__paymentMethod
    
    def get_priceGroup(self):
        return self.__priceGroup

    def get_orderTotal(self):
        return self.__orderTotal

    def __repr__(self):
        return self.__str__()

    def get_priceGroupCost(self, x):
        pg = 0
        if x == "Folksbill":
            pg = 10000
        elif x == "Jeppi":
            pg = 15000
        elif x == "Luxusbill":
            pg = 20000
        return pg
            

    def totalPrice(self):
        date_format = "%d-%m-%Y"
        total = 0
        dateReturn = datetime.strptime(self.__returnDate, date_format)
        dateHandover = datetime.strptime(self.__dateOfHandover, date_format)
        delta = dateReturn - dateHandover
        pg = self.get_priceGroupCost(self.__priceGroup)
        if self.__extraInsurance == "Yes":
            total = delta.days * (pg + 2000)
        else:
            total = delta.days * pg
        return total

