from repositories.orderRepo import orderRepo

class orderService():
    def __init__(self):
        self.__order_repo = orderRepo()

    def add_order(self,order):
        if self.is_valid_order(order):
            self.__order_repo.add_customer(order)

    def is_valid_order(self, order):
        pass ### verður að breyta þessu
