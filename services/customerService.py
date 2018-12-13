from repositories.customerRepo import customerRepo

class customerService():
    def __init__(self):
        self.__customer_repo = customerRepo()

    def add_customer(self,customer):
        self.__customer_repo.add_customer(customer)

    def get_customer(self):
        return self.__customer_repo.get_customer()

    def delete_customer(self):
        return self.__customer_repo.delete_customer()

    def customerExists(self, x):
        return self.__customer_repo.customerIsRegistered(x)
    
    def changeCustomer(self):
        return self.__customer_repo.changeCustomer()

    def searchCustomer(self):
        return self.__customer_repo.searchCustomer()