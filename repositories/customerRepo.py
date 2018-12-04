from models.customer import customer

class customerRepo:
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open ("./data/customers.txt", "a+") as customer_file:
            customerID = customer.get_customerID()
            firstName = customer.get_firstName()
            lastname = customer.get_lastName()
            passportID = customer.get_passportID()
            country = customer.get_country()
            SSN = customer.get_SSN()
            customer_file.write("{},{},{},{},{},{}\n".format(customerID,firstName,lastname, passportID, country,SSN))
