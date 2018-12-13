from models.customer import customer
import csv
import os

class customerRepo:
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open ("./data/customers.csv", "a+") as customer_file:
            firstName = customer.get_firstName()
            lastname = customer.get_lastName()
            passportID = customer.get_passportID()
            country = customer.get_country()
            SSN = customer.get_SSN()
            customer_file.write("{},{},{},{},{}\n".format(firstName,lastname, passportID, country,SSN))


    def get_customer(self):
        if self.__customer == []:
            with open("./data/customers.csv", "r") as customers_file:
                for line in customers_file.readlines():
                    firstName,lastName,passportID, country, SSN = line.split(",")
                    all_customers = customer(firstName,lastName,passportID, country, SSN)
                    self.__customer.append(all_customers)

        return self.__customer

    def delete_customer(self):
        entername = str(input("Enter customers SSN: "))
        while entername.isalnum() != True and len(entername) != 10:
            print("Social security number has to be all numbers and with length 10\nPlease try again.")
            entername = str(input("Enter customers SSN: "))
        with open("./data/customers.csv", "r+") as customers_file_r, open("./data/temp.csv", "w+") as customers_file_w:
            reader = csv.DictReader(customers_file_r)
            writer = csv.DictWriter(customers_file_w,fieldnames= ['firstName','lastname','passportID','country','SSN'])
            writer.writeheader()
            for row in reader:
                if row['SSN'] != entername:
                    writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/temp.csv','./data/customers.csv')

    def customerIsRegistered(self,x):
        with open('./data/customers.csv', 'r') as customers_file:
            reader = csv.DictReader(customers_file)
            for row in reader:
                if row['SSN'] == x:
                    print("Customer: " + row['firstName'])
                    return True
        return False
    
    def searchCustomer(self):
        target = input("Enter a customers SSN: ")
        while target.isalnum() != True and len(target) != 10:
            print("Social security number has to be all numbers and with length 10\nPlease try again.")
            target = input("Enter customers SSN: ")
        with open('./data/customers.csv','r') as customers_file:
            reader = csv.DictReader(customers_file)
            for row in reader:
                if row['SSN'] == target:
                    print("")
                    print("\nFirst name:\t" + row['firstName'])
                    print("Last name:\t"+ row['lastname'])
                    print("PassportID:\t" + row['passportID'])
                    print("Country:\t" + row['country'])
                    print("SSN:\t\t"+ row['SSN'])
                    print("")
                    return True
        return False

    def changeCustomer(self):
        kennitala = str(input("Enter a customer SSN: "))
        with open("./data/customers.csv",'r+') as customers_file_r, open("./data/temp.csv","w+") as customers_file_w:
            reader = csv.DictReader(customers_file_r)
            writer = csv.DictWriter(customers_file_w,fieldnames= ['firstName','lastname','passportID','country','SSN'])
            writer.writeheader()
            for row in reader:

                if row['SSN'] != kennitala:
                    writer.writerow(row)
                if row['SSN'] == kennitala:
                    
                    print('1 to change first name')
                    print('2 to change last name')
                    print('3 to change passport ID')
                    print('4 to change country of origin')
                    print('5 to change SSN')
                    
                    choice = input("What would you like to change? ")
                    if choice == '1':
                        breyting = input("Enter a change of first name: ").capitalize()
                        row['firstName'] = breyting
                        writer.writerow(row)
                        os.remove('./data/customers.csv')
                        os.rename('./data/temp.csv','./data/customers.csv')
                        
                    elif choice == '2':
                        breyting = input("Enter a change of last name: ").capitalize()
                        row['lastname'] = breyting
                        writer.writerow(row)
                        os.remove('./data/customers.csv')
                        os.rename('./data/temp.csv','./data/customers.csv')
                    
                    elif choice == '3':
                        breyting = input("Enter a change of passport ID: ")
                        while len(breyting) != 8:
                            print("Enter a change of passport ID: ")
                            breyting = input("Enter a change of passport ID: ")
                        row['passportID'] = breyting
                        writer.writerow(row)
                        os.remove('./data/customers.csv')
                        os.rename('./data/temp.csv','./data/customers.csv')

                    elif choice == '4':
                        breyting = input("Enter a change of country of origin: ").capitalize()
                        row['country'] = breyting
                        writer.writerow(row)
                        os.remove('./data/customers.csv')
                        os.rename('./data/temp.csv','./data/customers.csv')

                    elif choice == '5':
                        breyting = input("Enter a change of social security number: ")
                        while len(breyting) != 10:
                            print("Try again!")
                            breyting = input("Input new social security number: ")
                        row['SSN'] = breyting
                        writer.writerow(row)
                        os.remove('./data/customers.csv')
                        os.rename('./data/temp.csv','./data/customers.csv')

                    else:
                        print("Incorrect SSN")