from services.carService import carService
from models.car import car
from services.inputCheck import *



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
                licensePlate = checkLicensePlate()
                manufacturer = input("input manufacturer: ").capitalize()
                carType = input("input Car Type: ").capitalize()
                manOrAuto = checkManorAuto()
                fuelType = checkFuelType()
                print("(S)edan - (J)eep - (L)uxury")
                priceGroup = checkPriceGroup()
                manufYear = checkManuYear()
                availability = checkAvail()
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