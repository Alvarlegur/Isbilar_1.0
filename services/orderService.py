from repositories.orderRepo import orderRepo

class orderService():
    def __init__(self):
        self.__order_repo = orderRepo()

    def add_order(self,order):
        if self.is_valid_order(order):
            self.__order_repo.add_order(order)

    def get_order(self):
        return self.__order_repo.get_order()

    def is_valid_order(self, order):
        return True ### verður að breyta þessu
