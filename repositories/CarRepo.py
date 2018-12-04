from models.car import car


class CarRepo():

    def __init__(self):
        self.__car = []

    def add_car(self,car):
        with open ("./data/cars.txt","a+") as cars_file:
            carID = car.get_carID()
            manufacturer = car.get_manufacturer()
            typeCar = car.get_typeCar()
            manOrAuto = car.get_manOrAuto()
            fuelType = car.get_fuelType()
            priceGroup = car.get_priceGroup()
            manufYear = car.get_manufYear()
            cars_file.write("{},{},{},{},{},{},{}\n".format(carID,manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear))
