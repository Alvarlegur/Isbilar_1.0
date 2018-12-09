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
                licensePlate = input("input license Plate (5 letters): ")
                while len(licensePlate) != 5:
                    print("Try again!")
                    licensePlate = input("input license Plate: ")
                manufacturer = input("input manufacturer: ").capitalize()
                carType = input("input Car Type: ").capitalize()
                manOrAuto = input("input manual or auto (M = Manual, A = Auto): ").lower()
                while manOrAuto != "m" and manOrAuto != "a":
                    print("Try again!")
                    manOrAuto = input("input manual or auto (M = Manual, A = Auto): ").lower()
                if manOrAuto == "m":
                        manOrAuto = "Manual"
                elif manOrAuto == "a":
                        manOrAuto = "Auto"
                fuelType = input("input fuel type (B = Bensin, D = Disel): ").lower()
                while fuelType != "b" and fuelType != "d":
                    print("Try again!")
                    fuelType = input("input fuel type (B = Bensin, D = Disel): ").lower()
                if fuelType == "b":
                    fuelType = "Bensin"
                elif fuelType == "d":
                    fuelType = "Disel"
                priceGroup = input("input price group (F = Folksbill, J = Jeppi, L = Luxusbill): ").lower()
                while priceGroup != "f" and priceGroup != "j" and priceGroup != "l":
                    print("Try again!")
                    priceGroup = input("input price group (F = Folksbill, J = Jeppi, L = Luxusbill): ").lower()
                if priceGroup == "f":
                    priceGroup = "Folksbill"
                elif priceGroup == "j":
                    priceGroup = "Jeppi"
                elif priceGroup == "l":
                    priceGroup = "Luxusbill"
                manufYear = input("input manufacturer year: ")
                availability = input("available (Y/N)? ")
                new_car = car(licensePlate,manufacturer,carType,manOrAuto,fuelType,priceGroup,manufYear,availability)
                self.__car_service.add_car(new_car)

            elif choice == "2":
                self.__car_service.get_availability
                cars = self.__car_service.get_availablecars
                print(cars)

            elif choice == "3":
                self.__car_service.get_availability
                cars = self.__car_service.get_unavailablecars
                print(cars)

            elif choice == "4":
                cars = self.__car_service.delete_car()
            
            elif choice != "1" or choice != "2" or choice != "3" or choice != "q":
                print("Please try again!")