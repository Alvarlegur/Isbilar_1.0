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
<<<<<<< HEAD
<<<<<<< HEAD
                customerDict['firstName'] = input("input first name: ")
                customerDict['lastName'] = input("input last name: ")
                customerDict['passportID'] = input("input passport ID: ")
                customerDict['country'] = input("input country: ")
                customerDict['SSN'] = input("input SSN: ")
                new_customer = customer(customerDict)
=======
                firstName = input("input first name: ").capitalize()
                lastName = input("input last name: ").capitalize()
=======
                firstName = input("input first name: ")
                lastName = input("input last name: ")
>>>>>>> parent of 325f3cb... breytingar á print formatti
                passportID = input("input passport ID: ")
                country = input("input country: ")
                SSN = input("input SSN: ")
                new_customer = customer(firstName, lastName, passportID, country, SSN)
>>>>>>> 8b3091c575ff673677bcf2560290d29f91c316e5
                self.__customerService.add_customer(new_customer)

            elif choice == "2":
                customers = self.__customerService.get_customer()
                print(customers)
            
            elif choice == "3":
                customers = self.__customerService.delete_customer()
