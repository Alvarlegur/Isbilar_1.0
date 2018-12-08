

class customer():
    #initalizing customer instance
    def __init__(self, firstName, lastName, passportID, country, SSN):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__passportID = passportID
        self.__country = country
        self.__SSN = SSN

    def __str__(self):
        return "\t{:>5s}\n\t{:>5s}\t\t{:>5s}\t{:>5s}\n".format("First name\tLast name\tSSN",self.__firstName, self.__lastName, self.__SSN)

    def __repr__(self):
        return self.__str__()

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_passportID(self):
        return self.__passportID

    def get_country(self):
        return self.__country

    def get_SSN(self):
        return self.__SSN
