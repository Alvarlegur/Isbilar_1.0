class car:
    #defining inital class instance
    def __init__(self,licensePlate, manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear,availability):
        self.__licensePlate = licensePlate
        self.__manufacturer = manufacturer
        self.__typeCar = typeCar
        self.__manOrAuto = manOrAuto
        self.__fuelType = fuelType
        self.__priceGroup = priceGroup
        self.__manufYear = manufYear
        self.__availability = availability

    def __str__(self):
        return ("\t{:>10s}\t{:>10s}\t{:>10s}\t{:>10s}\t{:>10s}\t{:>10s}\t{:>10s}\t{:>10s}\n".format(self.__licensePlate, self.__manufacturer,self.__typeCar,self.__manOrAuto,self.__fuelType,self.__priceGroup,self.__manufYear, self.__availability))

    def get_licensePlate(self):
        return self.__licensePlate

    def get_manufacturer(self):
        return self.__manufacturer

    def get_typeCar(self):
        return self.__typeCar

    def get_priceGroup(self):
        return self.__priceGroup

    def get_manufYear(self):
        return self.__manufYear

    def get_manOrAuto(self):
        return self.__manOrAuto

    def get_fuelType(self):
        return self.__fuelType
    
    def get_availability(self):
        return self.__availability

    def set_availability(self):
        if self.__availability == "available":
            self.__availability = "unavailable"
        else:
            self.__availability = "available"

    def __repr__(self):
        return self.__str__()
    
