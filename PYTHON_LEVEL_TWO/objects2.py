class Circle():

    pi  = 3.14

    def __init__(self, radius = 1):
        self.radius = radius


    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(4)
myc.set_radius(20)
print((myc.area()))
