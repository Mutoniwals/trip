class Driver:
    def __init__ (self,permit,gender,name,ID,contact,birthyear,trian_no):
        self.__permit = permit
        self.__gender = gender
        self.__name = name
        self.__ID = ID
        self.__contact = contact
        self.__birthyear = birthyear
        self.__trian_no = trian_no
    
    def __str__(self):
        return f'''Drivers permit,{self.permit}\n Gender,{self.gender}\n
        His Name:{self.name}\n The Id {self.ID}\n The contact {self.contact}\n His birth_year {self.birthyear}'''

