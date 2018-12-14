
def checkSSN():
    print("If the message 'customer has been deleted' comes up your have deleted customer otherwise try again!")
    entername = str(input("Enter customers SSN: "))
    while entername.isdigit() != True and len(entername) != 10:
        print("Social security number has to be all numbers and with length 10\nPlease try again.")
        entername = str(input("Enter customers SSN: "))
    return entername


def checkPassportID():
    passport = str(input("Enter customers passport ID: "))
    while len(passport) != 8:
        print("Passport ID must contain 8 letters.")
        passport = str(input("Enter a change of passport ID: "))
    return passport

def checkPriceGroup():
    priceGroup = input("Input car type: ").lower()
    if priceGroup == "s":
        priceGroup = "Sedan"
        print(priceGroup)
    elif priceGroup == "j":
        priceGroup = "Jeep"
        print(priceGroup)
    elif priceGroup == "l":
        priceGroup = "Luxury"
        print(priceGroup)
    while priceGroup != "Sedan" and priceGroup != "Jeep" and priceGroup != "Luxury":
        print("Try again")
        priceGroup = input("Please choose S, J or L for car type: ").lower()
        if priceGroup == "s":
            priceGroup = "Sedan"
        elif priceGroup == "j":
             priceGroup = "Jeep"
        elif priceGroup == "l":
            priceGroup = "Luxury"
    return priceGroup

def checkDate():
    date = input("Pick-up date (dd-mm-yyyy): ")
    while len(date) != 10 and date[2] != "-" and date[5] != "-":
        print("Please enter a valid date: ")
        date = input("Pick-up date (dd-mm-yyyy): ")
    return date