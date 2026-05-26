def evenOdd(x):
    if(x%2==0):
        return"even"
    else:
        return"odd"
print(  evenOdd(3))



def myfunc(x,y=30):
    print("x:",x)
    print("y:",y)
myfunc(20)


def student(fname,lname):
 print(fname,lname)
student("sheetal","arya")


# positional Arguments

def nameAge(name,age):
   print(name)
   print(age)
nameAge("sheetal",21)

#Lambda

lambda_var=lambda x: x*x*x
print(lambda_var(3))


var=lambda x:x+1
print(var(2))
  

