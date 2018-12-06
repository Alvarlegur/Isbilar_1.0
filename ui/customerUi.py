from services.customerService import customerService
from models.customer import customer

class customerUI():
    def __init__(self):
        self.__customerService = customerService()
        customerDict = {} 

    def menu(self):
        choice = ""
        while choice != "q":
            print("Press 1 to add customer")
            print("Press 2 to list all customers")
            print("Press 3 to delete a customer")
            print("Press q to go back")
            choice = input("choose an option: ").lower()
            
            if choice == "1":
                customerDict['firstName'] = input("input first name: ")
                customerDict['lastName'] = input("input last name: ")
                customerDict['passportID'] = input("input passport ID: ")
                customerDict['country'] = input("input country: ")
                customerDict['SSN'] = input("input SSN: ")
                new_customer = customer(customerDict)
                self.__customerService.add_customer(new_customer)

            elif choice == "2":
                customers = self.__customerService.get_customer()
                print(customers)
            
            elif choice == "3":
                customers = self.__customerService.delete_customer()
