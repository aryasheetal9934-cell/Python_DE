# create an greeter class which greets users as good morning , good eveing ,good morning by the usernane

from datetime import datetime

class Greeter:
    def __init__(self,username):
       self.username=username
    def greet(self):
        current_hour=datetime.now().hour
        if 5<=current_hour<12:
            greeting="Good morning"
        elif 12<=current_hour<18:
            greeting="Good Evening"
        else:
            greeting="Good ninght"
        return f"{greeting},{self.username}!"
    
greeter= Greeter("sheetal")
print(greeter.greet())

# create a class for vechicles which stores information like vehicles_name, vehicles type, top-speed,model etc add few objects to it.

class vehical:
    def __init__(self,name,model,year,top_speed):
        self.name=name
        self.model=model
        self.year=year
        self.top_speed=top_speed

vehical1=vehical("BMW","X5",2020,250)
vehical2=vehical("Audi","Q7",2021,240)
vehical3=vehical("Mercedes","GLE",2019,230)

print(f"Vehical Name: {vehical1.name},Model: {vehical1.model},year:{vehical1.year},top_speed{vehical1.top_speed}")
print(f"Vehical Name: {vehical2.name},Model: {vehical2.model},year:{vehical2.year},top_speed{vehical2.top_speed}")
print(f"Vehical Name: {vehical3.name},Model: {vehical3.model},year:{vehical3.year},top_speed{vehical3.top_speed}")

# WAP to create a temperature class that stores a temperature in celsius. and add two methods to_fahrehnite(),to_kelvin which returns value of temperature in fahrenhnite and kelvin

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def to_fahrenheit(self):
        return(self.celsius*9/5)+32
    def to_kelvin(self):
        return self.celsius+273.1
    
t=Temperature(100)

print("celsius:",t.celsius)
print("Fahrenhiet:",t.to_fahrenheit())
print("kelvin:",t.to_kelvin())
