class shape:
    def area(self):
        pass
class squares(shape):
    def area(self):
        return"Area of suqare"
class circles(shape):
    def area(self):
        return"area of cicles"
    
Shape=[shape(),squares(),circles()]
for s in Shape:
    print(s.area())