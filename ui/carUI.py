from services.carService import carService
from models.car import car



class carUI():
    
    def __init__(self):
        self.__car_service = carService()

    def menu(self):

        choice = ""
        while choice != "q":
            print("Press 1 to add a Car")
            print("Press 2 to print out cars")
            print("Press 3 to delete car")
            print("Press q to go back")

            choice = input("Choose a option: ").lower()

            if choice == "1":
                licensePlate = input("input license Plate: ")
                manufacturer = input("input manufacturer: ")
                carType = input("input Car Type: ")
                manOrAuto = input("input manual or auto: ")
                fuelType = input("input fuel type: ")
                priceGroup = input("input price group: ")
                manufYear = input("input manufacturer year: ")
                new_car = car(licensePlate,manufacturer,carType,manOrAuto,fuelType,priceGroup,manufYear)
                self.__car_service.add_car(new_car)

            elif choice == "2":
                cars = self.__car_service.get_car()
                print(cars)

            elif choice == "3":
                cars = self.__car_service.delete_car()