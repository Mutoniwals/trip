class shape:
    def __init__(self):
        self.area = 0.0

    def compute_area(self):
        return self.area


class rectangle (shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width =width 

    def compute_area(self):
        # A = L * W
        self.area = self.length * self.width

        return self.area




class Triangle(shape):
    def __init__(self,base,height):
        super().__init__()
        self.base = base
        self.height = height 

    def compute_area(self):
        # A = (1/2)b*h
        self.area = (0.5*self.base)*self.height

        return self.area


class circle (shape):
    def __init__(self,radius):
        super().__init__()
        self.radius =radius


    def compute_area(self):
        # A = pr^2
        pI =3.14
        self.area = (pI * self.area ** 2)

        return self.area    