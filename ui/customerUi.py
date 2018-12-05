from services.customerService import customerService
from models.customer import customer

class customerUI():
    def __init__(self):
        self.__customerService = customerService()

    def menu(self):
        choice = ""
        while choice != "q":
            print("press 1 to add customer")
            print("press 2 to list all customers")
            choice = input("choose an option").lower()
            if choice == "1":
                 firstName = input("input first name: ")
                 lastName = input("input last name: ")
                 passportID = input("input passport ID: ")
                 country = input("input country: ")
                 SSN = input("input SSN: ")
                 new_customer = customer(firstName, lastName, passportID, country, SSN)
                 self.__customerService.add_customer(new_customer)
