from models.car import car


class CarRepo():

    def __init__(self):
        self.__cars = []

    def add_car(self,car):
        with open ("./data/cars.txt","a+") as cars_file:
            licensePlate = car.get_licensePlate()
            manufacturer = car.get_manufacturer()
            typeCar = car.get_typeCar()
            manOrAuto = car.get_manOrAuto()
            fuelType = car.get_fuelType()
            priceGroup = car.get_priceGroup()
            manufYear = car.get_manufYear()
            cars_file.write("{},{},{},{},{},{},{}\n".format(licensePlate, manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear))

    def get_car(self):
        if self.__cars == []:
            with open ("./data/cars.txt", "r") as cars_file:
                for line in cars_file.readlines():
                    licensePlate,manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear = line.split(",")
                    all_cars = car(licensePlate,manufacturer, typeCar, manOrAuto, fuelType, priceGroup, manufYear)
                    self.__cars.append(all_cars)

        return self.__cars

    def delete_car(self):
        entername = str(input("Enter a car to delete: "))
        with open("./data/cars.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if not entername in i:
                    f.write(i)
            f.truncate()
        