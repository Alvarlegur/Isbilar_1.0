from models.car import car
from datetime import datetime
import csv
import os


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
        with open('./data/cars.csv','r') as aCar, open('./data/temp.csv','w+',newline="") as updCar:
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
        os.replace('./data/temp.csv','./data/cars.csv')
        return carID
            

    def get_AvailCars(self):
        self.__cars = []
        with open('./data/cars.csv','r') as laust:
            reader = csv.reader(laust)
            for row in reader:
                if row[7] == "available":
                    availCars = car(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    self.__cars.append(availCars)
        return self.__cars

    def get_UnavailCars(self):
        self.__cars = []
        with open('./data/cars.csv','r') as tekid:
            reader = csv.reader(tekid)
            for row in reader:
                if row[7] == "unavailable":
                    unavailCars = car(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    self.__cars.append(unavailCars)
        return self.__cars

<<<<<<< HEAD
#Fall sem átti að checka á dagsetningu fyrir daginn í dag og skoða hvort 
#að það séu einhverjar pantanir þar sem dagsetning dagsins í dag
# er á bilinu á milli dateOfHandover og returnDate þá breytir fallið status
#á bílnum og setur hann sem unavailable.
    # def check_status(self):
    #     with open ('./data/cars.csv','r') as carsReader, open('./data/orders.csv','r') as orderReader, open('./data/temp.csv', 'w+',newline="") as carWriter:
    #         car_reader = csv.DictReader(carsReader)
    #         car_writer = csv.DictWriter(carWriter, fieldnames=['licensePlate','manufacturer','typeCar','manOrAuto','fuelType','priceGroup','manufYear','status'])
    #         order_reader = csv.DictReader(orderReader)
    #         today = datetime.today().strftime('%d-%m-%Y')
    #         car_writer.writeheader()
    #         carList = []
    #         # for x in order_reader:
    #         #     carList.append(x['carID'])
    #         # for row in car_reader:
    #         #     row['status'] = 'available'
    #         #     if row['licensePlate'] in carList:
    #         #         row['status'] = 'unavailable'
    #         # for row2 in order_reader:
    #         #     if row2
    #     os.remove('./data/cars.csv')
    #     os.rename('./data/temp.csv','./data/cars.csv')
            # for row in car_reader:
            #     for row2 in order_reader:
            #         if row2['carID'] == row['licensePlate']:
            #             if row2['dateOfHandover'] <= today and row2['returnDate'] >= today:
            #                 row['status'] = 'unavailable'
            #                 car_writer.writerow(row)
            #         else:
            #             row['status'] = 'available'
            #             car_writer.writerow(row)
        #     for row in car_reader:
        #         for row2 in order_reader:
        #             if row['licensePlate'] == row2['carID']:
        #                 if row2['dateOfHandover'] <= today and row2['returnDate'] >= today:
        #                     row['status'] = 'unavailable'
        #                     car_writer.writerow(row)
     
            # for row in car_reader:
            #     for row2 in order_reader:
            #         if row['licensePlate'] == row2['carID']:
            #             if row2['dateOfHandover'] <= today and row2['returnDate'] >= today:
            #                 row['status'] = 'unavailable'
            #                 car_writer.writerow(row)
            #         else:
            #             row['status'] = 'available'
            #             car_writer.writerow(row)
                        
            # for row in car_reader:
            #     if row['status'] != 'unavailable':
            #         for row2 in order_reader:
            #             if row2['carID'] == row['licensePlate']:
            #                 if row2['dateOfHandover'] <= today and row2['returnDate'] >= today:
            #                     row['status'] = 'unavailable'
            #                     car_writer.writerow(row)
            #                     break
            #                 else:
            #                     row['status'] = 'available'
            #                     car_writer.writerow(row)
            #     else:
            #         row['status'] = 'available'
            #         car_writer.writerow(row)
            # for row in car_reader:
            #     for row2 in order_reader:
            #         if row['licensePlate'] == row2['carID']:
            #             if row2['dateOfHandover'] <= today and today <= row2['returnDate']:
            #                 row['status'] = 'unavailable'
            #                 car_writer.writerow(row)
            #                 break
            #             else:
            #                 row['status'] = 'available'
            #                 car_writer.writerow(row)
            #         else:
            #             car_writer.writerow(row)
            # for row in order_reader:
            #     if row['dateOfHandover'] <= today and today <= row['returnDate']:
            #         for row2 in car_reader:
            #             if row['carID'] == row2['licensePlate']:
            #                 row2['status'] = 'unavailable'
            #                 car_writer.writerow(row2)
            #                 print("skrifa unavailable" + row2['licensePlate'])
            #                 break
            #     else:
            #         for row2 in car_reader:
            #             if row['carID'] == row2['licensePlate']:
            #                 row2['status'] = 'available'
            #                 car_writer.writerow(row2)
            #                 print("skrifa available" + row2['licensePlate'])



    def delete_car(self):
        entername = str(input("Enter cars license plate: ")).upper()
        #Check á constraints is_valid_licenseplate()
        with open("./data/cars.csv", "r+") as cars_file_r, open("./data/temp.csv", "w+") as cars_file_w:
=======
    #def check_status(self):
    #    with open ('./data/cars.csv','r') as carsReader, open('./data/orders.csv','r') as orderReader, open('./data/temp.csv', 'w+',newline="") as carWriter:
    #       car_reader = csv.DictReader(carsReader)
    #        car_writer = csv.DictWriter(carWriter, fieldnames=['licensePlate','manufacturer','typeCar','manOrAuto','fuelType','priceGroup','manufYear','status'])
    #        order_reader = csv.DictReader(orderReader)
    #        today = datetime.today().strftime('%d-%m-%Y')
    #        for row in order_reader:
    #            if row['dateOfHandover'] <= today and row['returnDate'] >= today:
    #                carToChange = row['carID']
    #                for row2 in car_reader:
    #                    if carToChange == row2['carID']:
    #                        row2['status'] = 'unavailable'
    #                        car_writer.writerow(row2)
    #            else:
    #                car_writer.writerow(row)
    #    os.remove('./data/cars.csv')
    #    os.replace('./data/temp.csv','./data/cars.csv')

    def delete_car(self):
        entername = str(input("Enter cars license plate: "))
        with open("./data/cars.csv", "r+") as cars_file_r, open("./data/temp.csv", "w+",newline="") as cars_file_w:
>>>>>>> e6a32647929b61017b5697eab4502c87a17b41b1
            reader = csv.DictReader(cars_file_r)
            writer = csv.DictWriter(cars_file_w,fieldnames= ['licensePlate','manufacturer','typeCar','manOrAuto','fuelType','priceGroup','manufYear','status'])
            writer.writeheader()
            for row in reader:
                if row['licensePlate'] != entername:
                    writer.writerow(row)
        os.remove('./data/cars.csv')
        os.replace('./data/temp.csv','./data/cars.csv')
