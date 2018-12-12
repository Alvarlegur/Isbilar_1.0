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
            cars_file.write("{},{},{},{},{},{},{},{}\n".format(licensePlate,manufacturer,typeCar,manOrAuto,fuelType,priceGroup,manufYear,availability))

    def return_randomCar(self, carType):
        carID = ""
        with open('./data/cars.csv','r') as aCar, open('./data/temp.csv','w+') as updCar:
            reader = csv.DictReader(aCar)
            writer = csv.DictWriter(updCar,fieldnames= ['licensePlate','manufacturer','typeCar','manOrAuto','fuelType','priceGroup','manufYear','status'])
            writer.writeheader()
            for row in reader:
                if row['priceGroup'] == carType and row['status'] == "available":
                    carID += row['licensePlate']
                    row['status'] = 'unavailable'
                    writer.writerow(row)
                    break
                else:
                writer.writerow(row)
            for row in reader:
                if row not in updCar:
                    writer.writerow(row)
            os.remove('./data/cars.csv')
            os.rename('./data/temp.csv','./data/cars.csv')
            print("CarID: " + carID)
            return carID

    def get_AvailCars(self):
        self.__cars = []
        with open('./data/cars.csv','r') as laust:
            reader = csv.reader(laust)
            for row in reader:
                if row[7] != "unavailable":
                    availCars = car(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    self.__cars.append(availCars)
        return self.__cars                  

    def get_UnavailCars(self):
        self.__cars = []
        with open('./data/cars.csv','r') as tekid:
            reader = csv.reader(tekid)
            for row in reader:
                if row[7] != "available":
                    unavailCars = car(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    self.__cars.append(unavailCars)
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
        