from models.car import car
from models.customer import customer
from datetime import datetime
import csv

class order:
    def __init__(self, carID, customerSSN ,priceGroup, dateOfHandover, returnDate, extraInsurance, cardnum):
        self.__orderID = id(self)
        self.__carID = carID
        self.__customerSSN = customerSSN
        self.__priceGroup = priceGroup
        self.__dateOfHandover = dateOfHandover
        self.__returnDate = returnDate
        self.__extraInsurance = extraInsurance
        self.__cardnum = cardnum
        self.__orderTotal = self.totalPrice()

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{} \n".format(self.__orderID, self.__carID, self.__customerSSN, self.__dateOfHandover, self.__returnDate, self.__extraInsurance, self.__orderTotal, self.__cardnum)

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

    def get_orderTotal(self):
        return self.__orderTotal

    def __repr__(self):
        return self.__str__()

    def get_priceGroupCost(self, x):
        pg = 0
        if x == "F":
            pg = 10000
        elif x == "J":
            pg = 15000
        elif x == "L":
            pg = 20000
        return pg
            
    def get_priceGroup(self):
        return self.__priceGroup

    def totalPrice(self):
        date_format = "%d/%m/%Y"
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

