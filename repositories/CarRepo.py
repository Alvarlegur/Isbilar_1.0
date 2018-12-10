from models.car import car
import csv


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
            priceGroup = car.get_priceGroup().capitalize()
            manufYear = car.get_manufYear()
            availability = car.get_availability()
            cars_file.write("{}, {}, {}, {}, {}, {}, {},{}\n".format(licensePlate, manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear,availability))


    def get_AvailCars(self):
        self.__cars = []
        with open('./data/cars.csv','r') as laust:
            reader = csv.reader(laust)
            for row in reader:
                if row[7] != "unavailable":
                    self.__cars.append(row)
        return self.__cars[1:]                   #Vantar að setja inn í model lagið þannig að bílarnir prentist út frá __str__ fallinu í car klasanum

    def get_UnavailCars(self):
        self.__cars = []
        with open('./data/cars.csv','r') as tekid:
            reader = csv.reader(tekid)
            for row in reader:
                if row[7] == "unavailable":
                    self.__cars.append(row)
        return self.__cars                      #Vantar að setja inn í model lagið þannig að bílarnir prentist út frá __str__ fallinu í car klasanum

    def delete_car(self):
        entername = str(input("Enter cars license plate: "))
        with open("./data/cars.csv", "r+") as cars_file:
            temp = cars_file.readlines()
            cars_file.seek(0)
            for line in temp:
                if not entername in line:
                    cars_file.write(line)
            cars_file.truncate()
        