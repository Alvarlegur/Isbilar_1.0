from services.customerService import customerService
from models.customer import customer

class customerUI():
    def __init__(self):
        self.__customerService = customerService() 

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
=======
<<<<<<< HEAD
<<<<<<< HEAD
                customerDict['firstName'] = input("input first name: ")
                customerDict['lastName'] = input("input last name: ")
                customerDict['passportID'] = input("input passport ID: ")
                customerDict['country'] = input("input country: ")
                customerDict['SSN'] = input("input SSN: ")
                new_customer = customer(customerDict)
=======
>>>>>>> 69b48a19c8494a4b3f7a2e82ac335efce736cea8
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
                self.__customerService.add_customer(new_customer)

            elif choice == "2":
                customers = self.__customerService.get_customer()
                print(customers)
            
            elif choice == "3":
                customers = self.__customerService.delete_customer()
