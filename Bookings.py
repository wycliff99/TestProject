


class Patient:

    def __init__(self, PatientName, PhoneNumber, PreferedDoc, Email, Symptoms, Date, Time, Gender):
        self.__PatientName =PatientName
        self.__PhoneNumber=PhoneNumber
        self.__PreferedDoc=PreferedDoc
        self.__Email=Email
        self.__Symptoms=Symptoms
        self.__Date=Date
        self.__Time=Time
        self.__Gender=Gender

    def get_PatientName(self):
        return self.__PatientName

    def set_frequency(self, PatientName):
        self.__PatientName = PatientName

    def get_PhoneNumber(self):
        return self.__PhoneNumber

    def set_PhoneNumber(self, PhoneNumber):
        self.__PhoneNumber=PhoneNumber

    def get_PreferedDoc(self):
        return self.__PreferedDoc

    def set_PreferedDoc(self, PreferedDoc):
        self.__PreferedDoc =PreferedDoc

    def get_Email(self):
        return self.__Email

    def set_Email(self, Email):
        self.__Email= Email

    def get_Symptoms(self):
        return self.__Symptoms

    def set_Symptoms(self, Symptoms):
        self.__Symptoms= Symptoms

    def get_Date(self):
        return self.__Date

    def set_Date(self, Date):
        self.__Date= Date

    def get_Time(self):
        return self.__Time

    def set_Time(self, Time):
        self.__Time= Time

    def get_Gender(self):
        return self.__Gender

    def set_Gender(self, Gender):
        self.__Gender= Gender

