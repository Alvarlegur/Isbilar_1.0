class car:
    #defining inital class instance
    def __init__(self,licensePlate, manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear):
        self.__licensePlate = licensePlate
        self.__manufacturer = manufacturer
        self.__typeCar = typeCar
        self.__manOrAuto = manOrAuto
        self.__fuelType = fuelType
        self.__priceGroup = priceGroup
        self.__manufYear = manufYear
        self.__availability = availability

    def __str__(self):
        return ("\t{}\n\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format("License Plate\tManufacturer\tType Car\tManual or Auto\tFuel Type\tPrice Group\tManufacturer Year\t",self.__licensePlate, self.__manufacturer,self.__typeCar,self.__manOrAuto,self.__fuelType,self.__priceGroup,self.__manufYear))

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

    def __repr__(self):
        return self.__str__()

    def set_licensePlate(self):
        self.__licensePlate = input("Input new license plate: ")
    
    def set_manufacturer(self):
        self.__manufacturer = input("Input new manufacturer: ")

    def set_typeCar(self):
        self.__typeCar = input("Input new car type: ")
    
    
