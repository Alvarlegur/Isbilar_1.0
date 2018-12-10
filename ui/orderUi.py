from services.orderService import orderService
from models.order import order
from services import carService

class orderUI():

    def __init__(self):
        self.__order_service = orderService()

    def menu(self):
        
        choice = ''
        while choice != 'q':
            print("Press 1 to add a order")
            print("Press 2 to print out all orders")
            print("Press 3 to delete order")
            print("Press q to go back")

            choice = input("Choose an option: ").lower()
            
            if choice == '1':
<<<<<<< HEAD
                print("What type of car?: ")
                priceGroup = input("(F for Folksbill 10.000kr \n J for Jeep 15.000kr \n L for Luxusbil 20.000kr)")
=======
                #orderID = input("Input orderID: ")
                carID = input("License plate number: ")
                while len(carID) != 5:
                    print("Please enter a valid license plate number!")
                    carID = input("input license Plate: ")
>>>>>>> 6863e85e848b1047de3bb12f57d44a2ebeecb0e0
                #while carService.is_available(carID) != True:
                    #print("This vehicle is not available, please try again")
                    #carID = input("License plate number: ")
                # checka hvort fastanr sé til í lausir bílar
                customerSSN = input("Customer social security number: ") 
                # checka hvort það sé búið að skrá þennan
                dateOfHandover = input("Pick-up date (dd/mm/yy): ")
                returnDate = input("Return date (dd/mm/yy): ")
                extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
                while extrainsurance != "y" and extrainsurance != "n":
                    print("Please enter Y or N!")
                    extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
                if extrainsurance == "y":
                    extrainsurance = "Yes"
                elif extrainsurance == "n":
                    extrainsurance = "No"
<<<<<<< HEAD
                new_order = order(carID, customerSSN, dateOfHandover,returnDate, extrainsurance)
=======
                #orderTotal = input("Total Prize: ")
                new_order = order(carID,customerSSN,dateOfHandover,returnDate,extrainsurance)
>>>>>>> 6863e85e848b1047de3bb12f57d44a2ebeecb0e0
                self.__order_service.add_order(new_order)

            elif choice == '2':
                orders = self.__order_service.get_order()
                print(orders)
            
            elif choice == "3":
                orders = self.__order_service.delete_order()