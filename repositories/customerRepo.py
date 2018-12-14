from models.customer import customer
from services.inputCheck import checkSSN, checkPassportID
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
        self.__customer = []
        with open("./data/customers.csv", "r") as customers_file:
            for line in customers_file.readlines():
                firstName,lastName,passportID, country, SSN = line.split(",")
                all_customers = customer(firstName,lastName,passportID, country, SSN)
                self.__customer.append(all_customers)

        return self.__customer

    def delete_customer(self):
        entername = checkSSN()
        with open("./data/customers.csv", "r+") as customers_file_r, open("./data/temp.csv", "w+",newline="") as customers_file_w:
            reader = csv.DictReader(customers_file_r)
            writer = csv.DictWriter(customers_file_w,fieldnames= ['firstName','lastname','passportID','country','SSN'])
            writer.writeheader()
            for row in reader:
                if entername in row['SSN']:
                    if row['SSN'] != entername:
                        writer.writerow(row)
                    print("customer has been deleted!")
                else:
                    writer.writerow(row)
        os.remove('./data/customers.csv')
        os.replace('./data/temp.csv','./data/customers.csv')

    def customerIsRegistered(self,x):
        with open('./data/customers.csv', 'r') as customers_file:
            reader = csv.DictReader(customers_file)
            for row in reader:
                if row['SSN'] == x:
                    print("Customer: " + row['firstName'])
                    return True
        return False
    
    def searchCustomer(self): 
        target = checkSSN()
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
        kennitala = checkSSN()
        with open("./data/customers.csv",'r+') as customers_file_r, open("./data/temp.csv","w+",newline="") as customers_file_w:
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
                    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
                        print("Please input number from 1 to 5")
                        choice = input("What would you like to change? ")
                    if choice == '1':
                        print("Change of first name")
                        breyting = input("Enter customers first name: ").capitalize()
                        row['firstName'] = breyting
                        writer.writerow(row)
                        
                    elif choice == '2':
                        print("Change of last name")
                        breyting = input("Enter customers last name: ").capitalize()
                        row['lastname'] = breyting
                        writer.writerow(row)
                    
                    elif choice == '3':
                        print("Change of passport ID")
                        breyting = checkPassportID()
                        row['passportID'] = breyting
                        writer.writerow(row)

                    elif choice == '4':
                        print("Change of country of origin")
                        breyting = input("Enter customers country of origin: ").capitalize()
                        row['country'] = breyting
                        writer.writerow(row)

                    elif choice == '5':
                        print("Enter a change of SSN")
                        breyting = checkSSN()
                        row['SSN'] = breyting
                        writer.writerow(row)

        os.remove('./data/customers.csv')
        os.replace('./data/temp.csv','./data/customers.csv')