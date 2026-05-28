class User:
    def __init__(self,name):
        self.__name=name   #private attribute
    def get_name(self):
        return self.__name

user1=User("sheetal")
print(user1.get_name())  #accessing private attributes through a public method