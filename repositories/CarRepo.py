from models.car import car


class CarRepo():

    def __init__(self):
        self.__cars = []

    def add_car(self,car):
        with open ("./data/cars.txt","a+") as cars_file:
            # carID = car.get_carID()
            manufacturer = car.get_manufacturer()
            typeCar = car.get_typeCar()
            manOrAuto = car.get_manOrAuto()
            fuelType = car.get_fuelType()
            priceGroup = car.get_priceGroup()
            manufYear = car.get_manufYear()
            cars_file.write("{},{},{},{},{},{}\n".format(manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear))

    def get_car(self):
        if self.__cars == []:
            with open ("./data/cars.txt", "r") as cars_file:
                for line in cars_file.readlines():
                    manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear = line.split(",")
                    all_cars = car(manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear)
                    self.__cars.append(all_cars)

        return self.__cars
