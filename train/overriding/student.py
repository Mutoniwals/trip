class student:
    def __init__ (self,name,reg_no,course,tuition):
        self.tuition = tuition
        self.name = name
        self.reg_no = reg_no
        self.course = course

    def __str__(self):
        return  (f"tuition{self.tuition},Name {self.name},Reg_no {self.reg_no},course {self.course}")


    def tuition_payment (self,tuition):
        return tuition    


class Localstudent (student):
    def __init__ (self,district,payment_method):
        super().__init__(self.name,self.reg_no,self.course,self.tuition)
        self.district = district
        self.payment_method = payment_method

    def tuition_payment (self,tuition):
        if self.payment_method == "bank":
            return tuition + 500

        elif self.payment_method == "mobile_money":
            return tuition + 3000
        else:
            print("stop it")

class foreignstudent(student):
    def __init__(self, name, reg_no, course, tuition,country):
        super().__init__(name, reg_no, course, tuition)
        self.country = country
        

    def tuition_payment(self, exchange_rate,amount_in_dollar):
        self.exchage_rate =exchange_rate
            
        return amount_in_dollar*self.exchage_rate     