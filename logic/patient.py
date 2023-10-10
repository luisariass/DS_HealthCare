class Patient(object):
    """
    Class used to represent a Student
    """

    def __init__(self, idn: int = 1, name: str = 'Name', surname: str = "surname", phone: int = 0000000, motiv: str = "null", date_hour: str = "00/00/00", medic: str = "NULL") -> object:
        """ Person constructor object.

        :param idn: A unique number that uniquely identifies the student in the system.
        :type idn: int
        :param name: name of student.
        :type name: str
        :param surname: last name of student.
        :type surname: str
        :returns: Student object
        :rtype: object
        """
        self.__idn = idn
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        self.__motiv = motiv
        self.__date_hour = date_hour
        self.__medic = medic

    @property
    def idn(self) -> int:
        """ Returns idn of the student.
          :returns: idn of student.
          :rtype: int
        """
        return str(self.__idn)

    @idn.setter
    def idn(self, val: int):
        """ The id of the student.
        :param id: id of student.
        :type: int
        """
        self.__idn = val

    @property
    def name(self) -> str:
        """ Returns the name of the student.
          :returns: name of student.
          :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """ The name of the student.
        :param name: name of student.
        :type: str
        """
        self.__name = name

    @property
    def surname(self) -> str:
        """ Returns the last name of the student.
          :returns: last name of student.
          :rtype: str
        """
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        """ The last name of the student.
        :param surname: last name of student.
        :type: str
        """
        self.__surname = surname

    @property
    def phone(self) -> int:
        """ Returns the phone of the student.
          :returns: phone of student.
          :rtype: int
        """
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        """ The phone of the student.
        :param phone: phone of student.
        :type: int
        """
        self.__phone = phone
    
    @property
    def motiv(self) -> str:
        """ Returns the motiv of the student.
          :returns: motiv of student.
          :rtype: str
        """
        return self.__motiv
    @motiv.setter
    def motiv(self, motiv: str):
        """ The motiv of the student.
        :param motiv: motiv of student.
        :type: str
        """
        self.__motiv = motiv
    @property
    def date_hour(self) -> str:
        """ Returns the date_hour of the student.
          :returns: date_hour of student.
          :rtype: str
        """
        return self.__date_hour
    @date_hour.setter
    def date_hour(self, date_hour: str):
        """ The date_hour of the student.
        :param date_hour: date_hour of student.
        :type: str
        """
        self.__date_hour = date_hour
    @property
    def medic(self) -> str:
        """ Returns the medic of the student.
          :returns: medic of student.
          :rtype: str
        """
        return self.__medic
    @medic.setter
    def medic(self, medic: str):
        """ The medic of the student.
        :param medic: medic of student.
        :type: str
        """
        self.__medic = medic
    
    def __str__(self):
        return dict(idn=self.idn, name=self.name, surname=self.surname,phone = self.phone, moitv = self.motiv,date_hour=self.date_hour,medic=self.medic).__str__()

if __name__ == '__main__':

    edwin = Patient(idn=23456, name="Edwin", surname="Puertas",phone=1234567,motiv="Dolor de cabeza",date_hour="12/12/12",medic="Dr. Juan")
    print(edwin)
    juan = Patient()
    print(juan)

