from repositories.customerRepo import customerRepo

class customerService():
    def __init__(self):
        self.__customer_repo = customerRepo()

    def add_customer(self,customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)

    def get_customer(self):
        return self.__customer_repo.get_customer()

    def delete_customer(self):
        return self.__customer_repo.delete_customer()

    def is_valid_customer(self,customer):
        return True
        #######verður að breyta þessu
    
    def customerExists(self, x):
        return self.__customer_repo.customerIsRegistered(x)
