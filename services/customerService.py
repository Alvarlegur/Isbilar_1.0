from repositories.customerRepo import customerRepo

class customerService():
    def __init__(self):
        self.__customer_service = customerRepo()

    def add_customer(self):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)

    def is_valid_customer(self):
        pass #######verður að breyta þessu
