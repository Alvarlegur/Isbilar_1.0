
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