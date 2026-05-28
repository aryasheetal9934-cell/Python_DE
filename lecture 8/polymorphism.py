# class shape:
#     def area(self):
#         pass
# class squares(shape):
#     def area(self):
#         return"Area of suqare"
# class circles(shape):
#     def area(self):
#         return"area of cicles"
    
# Shape=[shape(),squares(),circles()]
# for s in Shape:
#     print(s.area())





# class DataEngineering:  # parent class
#     def course(self):
#         print("Data Engineering course")
# class Python(DataEngineering):   #child class
#     def course(self):                      #method overriding
#        print("Python course")
# class Data(DataEngineering):            #child class
#     def course(self):  
#         print("data course")

# for x in [Python(),Data()]:             ## polymorphism
#     x.course()                    #method calling








## create an runtime polymorphsim code for multiple "Animals" like "Dog0,"cat" which
## which produces "sounds like "woof"or "meow"

class Animals:
      def Sounds(self):
          pass
class Dog(Animals):
      def Sounds(self):
          return"woof"
class Cat(Animals):
       def Sounds(self):
            return"meow"
for x in [Dog(),Cat()]:
    print( x.Sounds())



#Create a function initiate_engine() that accepts objects of different classes and calls the appropriate start_engine() method to demonstrate polymorphism
#The Vehicle class should define a common method start_engine().
# Create two child classes:
# Car
# Motorcycle

class Vehicle:
    def start_engine(self):
        print("Vehicle engine starts")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine starts with key")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine starts with button")

# Polymorphism function
def initiate_engine(vehicle):
    return vehicle.start_engine()


c = Car()
m = Motorcycle()

initiate_engine(c)
initiate_engine(m)