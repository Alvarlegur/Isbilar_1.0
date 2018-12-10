from models.car import car
from models.customer import customer
from datetime import datetime
import csv

class order:
    #initalizing order instance
    #vantar að tengja carID og customerID inn í orders
    def __init__(self, carID, customerSSN ,dateOfHandover, returnDate,extraInsurance):
        self.__orderID = id(self)
        self.__carID = carID
        self.__customerSSN = customerSSN
        self.__dateOfHandover = dateOfHandover
        self.__returnDate = returnDate
        self.__extrainsurance = extraInsurance
        self.__orderTotal = self.totalPrice(self.__carID)

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{} \n".format(self.__orderID,self.__dateOfHandover, self.__returnDate, self.__extrainsurance, self.__orderTotal)

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
    
    def totalPrice(self,carID):
        date_format = "%d/%m/%Y"
        total = 0
        dateReturn = datetime.strptime(self.__returnDate, date_format)
        dateHandover = datetime.strptime(self.__dateOfHandover, date_format)
        delta = dateReturn - dateHandover
        print("number of days: ")
        print (delta.days)
        pg = 0
        with open("./data/availablecars.csv", "r") as car:
            reader = csv.DictReader(car)
            for row in reader:
                
                if row['LicensePlate'] == self.__carID:
                    print(self.__carID)
                    if row['priceGroup'] == "LUXUSBILL":
                        print("luxusbill")
                        pg = 20000
                    elif row['priceGroup'] == "JEPPI":
                        print("jeppi")
                        pg = 15000
                    elif row['priceGroup'] == "FOLKSBILL":
                        print("folksbill")
                        pg = 10000
        if self.__extrainsurance == "Yes":
            print("extrains YES")
            total = delta.days * pg + 2000
        else:
            print("extrains NO")
            total = delta.days * pg

        return total

