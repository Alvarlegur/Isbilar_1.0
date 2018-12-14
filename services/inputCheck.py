from datetime import datetime

def checkSSN():
    entername = str(input("Enter customers SSN: "))
    while entername.isnumeric() != True or len(entername) != 10:
        print("Social security number has to be all numbers and with length 10\nPlease try again.")
        entername = str(input("Enter customers SSN: "))
    return entername


def checkPassportID():
    passport = str(input("Enter customers passport ID: "))
    while len(passport) != 8:
        print("Passport ID must contain 8 letters.")
        passport = str(input("Enter a change of passport ID: "))
    return passport

def checkLicensePlate():
    licenseplate = str(input("Input license plate (5 letters): ")).upper()
    while len(licenseplate) != 5:
        print("Invalid license plate! Try again.")
        licenseplate = str(input("Input license plate (5 letters): ")).upper()
    return licenseplate

def checkManorAuto():
    manOrAuto = input("input manual or auto (M = Manual, A = Auto): ").lower()
    while manOrAuto != "m" and manOrAuto != "a":
        print("Try again!")
        manOrAuto = input("input manual or auto (M = Manual, A = Auto): ").lower()
    if manOrAuto == "m":
            manOrAuto = "Manual"
    elif manOrAuto == "a":
            manOrAuto = "Auto"
    return manOrAuto

def checkFuelType():
    fuelType = input("input fuel type (B = Bensin, D = Disel): ").lower()
    while fuelType != "b" and fuelType != "d":
        print("Try again!")
        fuelType = input("input fuel type (B = Bensin, D = Disel): ").lower()
    if fuelType == "b":
            fuelType = "Bensin"
    elif fuelType == "d":
            fuelType = "Disel"
    return fuelType

def checkManuYear():
    manufYear = str(input("Input manufacturer year: "))
    while manufYear.isnumeric() != True or len(manufYear) != 4:
        print("Try again!")
        manufYear = str(input("Input manufacturer year: "))
    return manufYear

def checkAvail():
    availability = input("available? (Y = Yes, N = No): ").lower()
    while availability != "y" and availability != "n":
        print("Try again!")
        availability = input("available? (Y = Yes, N = No): ").lower()
    if availability == "y":
            availability = "available"
    elif availability == "n":
            availability = "unavailable"
    return availability

def checkPriceGroup():
    priceGroup = input("Input car type: ").lower()
    while priceGroup != "s" and priceGroup != "j" and priceGroup != "l":
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
    date = input("Input date: ")
    while True:
        try:
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print("Incorrect data format, should be DD-MM-YYYY")
            date = input("Input date: ")
    return date


#def checkDatetime(date, returnDate):
    ## ddate,dmonth,dyear = date.split('-')
    ## rdate,rmonth,ryear = returnDate.split('-')
    ## if ryear < dyear:
    ##     return False
    ## elif rmonth <= dmonth and ryear >= dyear and rdate > :
    # date_format = "%d-%m-%Y"
    # x = datetime.strptime(date, date_format)
    # y = datetime.strptime(returnDate, date_format)
    # int(delta) = ((y - x) * 1)
    # if delta < 0:
    #     return False
    # return True


def checkInsurance():
    extrainsurance = input("Extra insurance 2.000isk per day (Y = Yes, N = No): ").lower()
    while extrainsurance != "y" and extrainsurance != "n":
        print("Please enter Y or N!")
        extrainsurance = input("Extra insurance (Y = Yes, N = No): ").lower()
    if extrainsurance == "y":
        extrainsurance = "Yes"
    elif extrainsurance == "n":
        extrainsurance = "No"
    return extrainsurance

def checkCardnum():
    cardnum = input("Enter a creditcard number: ")
    while cardnum.isnumeric() != True or len(cardnum) != 10:
        print("Please enter a valid creditcard number!")
        cardnum = input("Enter a creditcard number: ")
    return cardnum

def checkPaymentMethod():
    print("Credit card (C), Debit card (D), Money (M)")
    paymentMethod = input("Payment method: ").lower()
    while paymentMethod != "c" and paymentMethod != "d" and paymentMethod != "m":
        print("Try again")
        print("Please input (c) for Credit card,(d) for Debit card and (m) for Money")
        paymentMethod = input("Payment method: ").lower()
    if paymentMethod == "c":
        paymentMethod = "Credit"
    elif paymentMethod == "d":
        paymentMethod = "Debit"
    elif paymentMethod == "m":
        paymentMethod = "Money"
    return paymentMethod
