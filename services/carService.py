from repositories.CarRepo import CarRepo


class carService():
    def __init__(self):
        self.__car_repo = CarRepo()

    def add_car(self,car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)


    def get_availablecars(self):
        return self.__car_repo.get_AvailCars()
    
    def get_unavailablecars(self):
        return self.__car_repo.get_UnavailCars()
    
    def delete_car(self):
        return self.__car_repo.delete_car()

    def is_valid_car(self,car):
        return True ## breyta þessu
    