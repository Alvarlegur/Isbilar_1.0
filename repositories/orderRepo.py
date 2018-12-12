from models.order import order
import csv
import os


class orderRepo():
    def __init__(self):
        self.__order = []

    def add_order(self,order):
        with open ("./data/orders.csv", "a+") as orders_file:
            orderID = order.get_orderID()
            carID = order.get_carID()
            customerSSN = order.get_customerSSN()
            dateOfHandover = order.get_dateOfHandover()
            returnDate = order.get_returnDate()
            extraInsurance = order.get_extraInsurance()
            orderTotal = order.get_orderTotal()
            cardnum = order.get_cardnum()
            orders_file.write("{},{},{},{},{},{},{},{}\n".format(orderID,carID, customerSSN, dateOfHandover, returnDate, extraInsurance, orderTotal, cardnum))

    def get_order(self):
        if self.__order == []:
            with open ("./data/orders.csv", "r") as orders_file:
                for line in orders_file.readlines():
                    orderID, carID, customerSSN, dateOfHandover, returnDate, extraInsurance, orderTotal, cardnum = line.split(",")
                    all_orders = order(carID,customerSSN,orderTotal,dateOfHandover,returnDate,extraInsurance,cardnum)
                    self.__order.append(all_orders)
                    
        return self.__order
            
    def delete_order(self):
        entername = str(input("Enter orders ID: "))
        with open("./data/orders.csv", "r+") as orders_file:
            temp = orders_file.readlines()
            orders_file.seek(0)
            for line in temp:
                if not entername in line:
                    orders_file.write(line)
            orders_file.truncate()
    
    def changeOrder(self):
        orderID = str(input("Enter a order ID: "))
        with open("./data/orders.csv",'r+') as orders_file_r, open("./data/temp.csv","w+") as orders_file_w:
            reader = csv.DictReader(orders_file_r)
            writer = csv.DictWriter(orders_file_w,fieldnames= ['orderID','carID','customerSSN','dateOfHandover','returnDate','extraInsurance','orderTotal'])
            writer.writeheader()
            for row in reader:

                if row['orderID'] != orderID:
                    writer.writerow(row)
                if row['orderID'] == orderID:
                    
                    print('1 to change car ID: ')
                    print('2 to change customer SSN: ')
                    print('3 to change date of handover: ')
                    print('4 to change return date: ')
                    print('5 to change extra insurance: ')
                    print('6 to change order total: ')
                    
                    choice = input("What would you like to change? ")
                    if choice == '1':
                        change = input("Enter a change of car ID: ")
                        row['carID'] = change
                        writer.writerow(row)
                        os.remove('./data/orders.csv')
                        os.rename('./data/temp.csv','./data/orders.csv')
                        
                    elif choice == '2':
                        change = input("Enter a change of customer SSN: ")
                        row['customerSSN'] = change
                        writer.writerow(row)
                        os.remove('./data/orders.csv')
                        os.rename('./data/temp.csv','./data/orders.csv')
                    
                    elif choice == '3':
                        change = input("Enter a change of date of handover: ")
                        row['dateOfHandover'] = change
                        writer.writerow(row)
                        os.remove('./data/orders.csv')
                        os.rename('./data/temp.csv','./data/orders.csv')

                    elif choice == '4':
                        change = input("Enter a change of return date: ")
                        row['returnDate'] = change
                        writer.writerow(row)
                        os.remove('./data/orders.csv')
                        os.rename('./data/temp.csv','./data/orders.csv')

                    elif choice == '5':
                        change = input("Enter a change of extra insurance: ")
                        row['extraInsurance'] = change
                        writer.writerow(row)
                        os.remove('./data/orders.csv')
                        os.rename('./data/temp.csv','./data/orders.csv')

                    elif choice == '6':
                        change = input("Enter a change of order total: ")
                        row['orderTotal'] = change
                        writer.writerow(row)
                        os.remove('./data/orders.csv')
                        os.rename('./data/temp.csv','./data/orders.csv')

                    else:
                        print("Incorrect car ID")
