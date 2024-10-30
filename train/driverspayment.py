class Driverspayment:
    def __init__(self,ID,contact,account):
        self.ID = ID
        self.contact = contact
        self.account = account


    def __str__(self):
        return (f"The ID {self.ID}\n contact {self.contact}\n Accout {self.account}")
        