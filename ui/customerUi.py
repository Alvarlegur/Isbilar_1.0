from services.customerService import customerService
from models.customer import customer
from services.inputCheck import *

class customerUI():
    def __init__(self):
        self.__customerService = customerService() 

    def menu(self):
        choice = ""
        while choice != "q":
            print("---------------CUSTOMERS---------------\n")
            print("Press 1 to add customer")
            print("Press 2 to list all customers")
            print("Press 3 to delete a customer")
            print("Press 4 to change a customer")
            print("Press 5 to search for a customer")
            print("Press q to go back")
            choice = input("choose an option: ").lower()
            if choice == "1":
                firstName = input("input first name: ").capitalize()
                lastName = input("input last name: ").capitalize()
                passportID = checkPassportID()
                country = input("input country: ").capitalize()
                SSN = checkSSN()
                new_customer = customer(firstName, lastName, passportID, country, SSN)
                self.__customerService.add_customer(new_customer)

            elif choice == "2":
                customers = self.__customerService.get_customer()
                for allCustomers in customers:
                    print(allCustomers)
            
            elif choice == "3":
                customers = self.__customerService.delete_customer()
            
            elif choice == "4":
                customers = self.__customerService.changeCustomer()

            elif choice == "5":
                customers = self.__customerService.searchCustomer()
                while customers != True:
                    print("No customer found")
                    customers = self.__customerService.searchCustomer()

