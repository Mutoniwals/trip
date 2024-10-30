class Customer:
    def __init__(self,gender,receipt,seat_no,name,ID,trip,contact):
        self.gender = gender
        self.receipt = receipt
        self.seat_no = seat_no
        self.name = name
        self.ID = ID
        self.trip = trip
        self.contact = contact

    
    def __str__(self):
        return (f"customer gender,{self.gender},\nreceipt {self.receipt},\nThe seat_no {self.seat_no}\n,
                Name {self.name}\n The Id {self.ID}\nTrip,{self.trip}\ncontact,{self.contact}")