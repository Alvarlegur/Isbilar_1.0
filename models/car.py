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

    def __str__(self):
        return "{},{},{}".format(self.__manufacturer, self.__typeCar, self.__priceGroup)

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

    def __repr__(self):
        return self.__str__()
