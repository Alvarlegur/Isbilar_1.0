# def checkSSN():
#     entername = str(input("Enter customers SSN: "))
#     while entername.isalnum() != True and len(entername) != 10:
#         print("Social security number has to be all numbers and with length 10\nPlease try again.")
#         entername = str(input("Enter customers SSN: "))

def checkSSN():
    
    entername = str(input("Enter customers SSN: "))
    while entername.isdigit() == False and len(entername) != 10:
        print("Social security number has to be all numbers and with length 10\nPlease try again.")
        entername = input("Enter customers SSN: ")
    print("Customer has been deleted!")
    return entername

    