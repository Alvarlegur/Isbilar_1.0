from repositories.orderRepo import orderRepo
from repositories.CarRepo import CarRepo

class orderService():
    def __init__(self):
        self.__order_repo = orderRepo()
        self.__car_repo = CarRepo()

    def add_order(self,order):
        self.__order_repo.add_order(order)

    def get_RandomAvailCar(self,carType):
        return self.__car_repo.return_randomCar(carType)

    def get_order(self):
        return self.__order_repo.get_order()

    def delete_order(self):
        return self.__order_repo.delete_order()

    def changeOrder(self):
        return self.__order_repo.changeOrder()
