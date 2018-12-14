
def checkSSN():
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

        

    