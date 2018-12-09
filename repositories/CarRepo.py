from models.car import car
import csv


class CarRepo():

    def __init__(self):
        self.__cars = []

    def add_car(self,car):
        with open ("./data/cars.csv","a+") as cars_file:
            writer = csv.writer(cars_file)
            licensePlate = car.get_licensePlate()
            manufacturer = car.get_manufacturer()
            typeCar = car.get_typeCar()
            manOrAuto = car.get_manOrAuto()
            fuelType = car.get_fuelType()
            priceGroup = car.get_priceGroup()
            manufYear = car.get_manufYear()
            availability = car.get_availability()
            writer.writerow(["{}, {}, {}, {}, {}, {}, {}, {}".format(licensePlate, manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear,availability)])

    def availability(self):
        with open('./data/cars.csv','r+') as inp, open('./data/availablecars.csv', 'w') as out1, open('./data/unavailablecars.csv','w') as out2:
            writer1 = csv.writer(out1)
            writer2 = csv.writer(out2)
            for row in csv.reader(inp):
                if row[7] != 'unavailable':
                    writer1.writerow(row)
                else:
                    writer2.writerow(row)

    def get_AvailCars(self):
        if self.__cars == []:
            with open('./data/availablecars.csv','r') as laust:
                reader = csv.reader(laust)
                for row in reader:
                    self.__cars.append(row)
        return self.__cars

    def get_UnavailCars(self):
        if self.__cars == []:
            with open('.data/unavailablecars.csv','r') as tekid:
                reader = csv.reader(tekid)
                for row in reader:
                    self.__cars.append(row)
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
        
