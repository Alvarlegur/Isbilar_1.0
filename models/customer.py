class customer:
    #initalizing customer instance
    def __init__(self, firstName, lastName, passportID, country, SSN):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__passportID = passportID
        self.__country = country
        self.__SSN = SSN

    def __str__(self):
        return "{}\t{}\t{}".format(self.__firstName, self.__lastName, self.__SSN)

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
