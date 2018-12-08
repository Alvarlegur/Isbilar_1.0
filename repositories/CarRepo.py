from models.car import car


class CarRepo():

    def __init__(self):
        self.__cars = []

    def add_car(self,car):
        with open ("./data/cars.csv","a+") as cars_file:
            licensePlate = car.get_licensePlate()
            manufacturer = car.get_manufacturer()
            typeCar = car.get_typeCar()
            manOrAuto = car.get_manOrAuto()
            fuelType = car.get_fuelType()
            priceGroup = car.get_priceGroup()
            manufYear = car.get_manufYear()
            availability = car.get_availability()
            cars_file.write("{}, {}, {}, {}, {}, {}, {}, {}\n".format(licensePlate, manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear,availability))

    def get_car(self):
        if self.__cars == []:
            with open ("./data/cars.csv", "r") as cars_file:
                for line in cars_file.readlines():
                    licensePlate,manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear,availability = line.split(",")
                    all_cars = car(licensePlate,manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear,availability)
                    self.__cars.append(all_cars)
        return self.__cars

    def delete_car(self):
        entername = str(input("Enter cars license plate: "))
        with open("./data/cars.csv", "r+") as cars_file:
            temp = cars_file.readlines()
            cars_file.seek(0)
            for line in temp:
                if not entername in line:
                    cars_file.write(line)
            cars_file.truncate()
        