class Transport:
    def start(self):
        return"starting transport"
class car( Transport):
    def drive(self):
        return"car is moving"

mycar=car()

print(mycar.start()) # inherited method from transport class
print(mycar.drive()) # method from car class