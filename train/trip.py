class Trip:
    def __init__ (self,Destenation,Starting_point,duration,train_no,trip_data_time,trip_id,fee):
        self.Destenation = Destenation
        self.starting_point = Starting_point
        self.duration = duration
        self.train_no = train_no
        self.trip_data_time = trip_data_time
        self.trip_id = trip_id
        self.fee = fee



    def __str__(self):
        return (f"Train destenation{self.Destenation},\nIt's starting point{self.starting_point},
                \nThe duration,{self.duration}\nIt's Train number{self.train_no}\nThe trip_data_time{self.trip_data_time},
                \nThe Trip id{self.trip_id}\n fee,{self.fee}")