from services.carService import carService
from models.car import car



class carUI():
    
    def __init__(self):
        self.__car_service = carService()

    def menu(self):

        choice = ""
        while choice != "q":
            print("----------------CARS---------------\n")
            print("Press 1 to add a Car")
            print("Press 2 to print out available cars")
            print("Press 3 to print out unavailable cars")
            print("Press 4 to delete car")
            print("Press 5 to print out pricelist")
            print("Press q to go back")

            choice = input("Choose a option: ").lower()

            if choice == "1":
                licensePlate = input("input license Plate (5 letters): ").upper()
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
                priceGroup = input("input price group (S = Sedan, J = Jeep, L = Luxury): ").lower()
                while priceGroup != "s" and priceGroup != "j" and priceGroup != "l":
                    print("Try again!")
                    priceGroup = input("input price group (S = Sedan, J = Jeep, L = Luxury): ").lower()
                if priceGroup == "s":
                    priceGroup = "Sedan"
                elif priceGroup == "j":
                    priceGroup = "Jeep"
                elif priceGroup == "l":
                    priceGroup = "Luxury"
                manufYear = input("input manufacturer year: ")
                while len(manufYear) != 4:
                    print("Try again!")
                    manufYear = input("input manufacturer year: ")
                availability = input("available? (Y = Yes, N = No): ").lower()
                while availability != "y" and availability != "n":
                    print("Try again!")
                    availability = input("available? (Y = Yes, N = No").lower()
                if availability == "y":
                    availability = "available"
                elif availability == "n":
                    availability = "unavailable"
                new_car = car(licensePlate,manufacturer,carType,manOrAuto,fuelType,priceGroup,manufYear,availability)
                self.__car_service.add_car(new_car)

            elif choice == "2":
                cars = self.__car_service.get_availablecars()
                for availablecars in cars:
                    print(availablecars)

            elif choice == "3":
                cars2 = self.__car_service.get_unavailablecars()
                for unavailablecars in cars2:
                    print(unavailablecars)

            elif choice == "4":
                cars = self.__car_service.delete_car()
            
            elif choice == "5":
                print("\nSedan:   10.000isk per day\nJeep:    15.000isk per day\nLuxury:  20.000isk per day\n")

            
            elif choice != "q":
                print("Please try again!")