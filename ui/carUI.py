from services.carService import carService
from models.car import car



class carUI():
    
    def __init__(self):
        self.__car_service = carService()

    def menu(self):

        choice = ""
        while choice != "q":
            print("Press 1 to add a Car")
            print("Press 2 to print out available cars")
            print("Press 3 to print out unavailable cars")
            print("Press 4 to delete car")
            print("Press q to go back")

            choice = input("Choose a option: ").lower()

            if choice == "1":
                licensePlate = input("input license Plate (5 letters): ").upper()
                while len(licensePlate) != 5:
                    print("Try again!")
                    licensePlate = input("input license Plate: ")
                manufacturer = input("input manufacturer: ").upper()
                carType = input("input Car Type: ").upper()
                manOrAuto = input("input manual or auto (M = Manual, A = Auto): ").upper()
                while manOrAuto != "M" and manOrAuto != "A":
                    print("Try again!")
                    manOrAuto = input("input manual or auto (M = Manual, A = Auto): ").upper()
                if manOrAuto == "M":
                        manOrAuto = "MANUAL"
                elif manOrAuto == "A":
                        manOrAuto = "AUTO"
                fuelType = input("input fuel type (B = Bensin, D = Disel): ").upper()
                while fuelType != "B" and fuelType != "D":
                    print("Try again!")
                    fuelType = input("input fuel type (B = Bensin, D = Disel): ").upper()
                if fuelType == "B":
                    fuelType = "BENSIN"
                elif fuelType == "D":
                    fuelType = "DISEL"
                priceGroup = input("input price group (F = Folksbill, J = Jeppi, L = Luxusbill): ").upper()
                while priceGroup != "F" and priceGroup != "J" and priceGroup != "L":
                    print("Try again!")
                    priceGroup = input("input price group (F = Folksbill, J = Jeppi, L = Luxusbill): ").upper()
                if priceGroup == "F":
                    priceGroup = "FOLKSBILL"
                elif priceGroup == "J":
                    priceGroup = "JEPPI"
                elif priceGroup == "L":
                    priceGroup = "LUXUSBILL"
                manufYear = input("input manufacturer year: ")
                while len(manufYear) != 4:
                    print("Try again!")
                    manufYear = input("input manufacturer year: ")
                availability = input("available? (Y = Yes, N = No): ").upper()
                while availability != "Y" and availability != "N":
                    print("Try again!")
                    availability = input("available? (Y = Yes, N = No").upper()
                if availability == "Y":
                    availability = "AVAILABLE"
                elif availability == "N":
                    availability = "UNAVAILABLE"
                new_car = car(licensePlate,manufacturer,carType,manOrAuto,fuelType,priceGroup,manufYear,availability)
                self.__car_service.add_car(new_car)

            elif choice == "2":
                cars = self.__car_service.get_availablecars()
                print(cars)

            elif choice == "3":
                cars2 = self.__car_service.get_unavailablecars()
                print(cars2)

            elif choice == "4":
                cars = self.__car_service.delete_car()
            
            elif choice != "1" or choice != "2" or choice != "3" or choice != "q":
                print("Please try again!")