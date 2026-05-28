# pure function

def pure_func(list):
    New_list=[]
    for i in list:
        New_list.append(i*2)
    return New_list
my_list=[1,2,3,4,5]
modified_list=pure_func(my_list)
print(modified_list)


# Recursion in functional programming

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))  #o/p: 120

# functions are First-class citizens in python

def shout(text):
    return text.upper()+"!!!"
def whisper(text):
    return text.lower()+"..."
def greet(func):  # func is used as a parameter to pass the function as an arugment
    greeting=func("Helo,world")
    print(greeting)

greet(shout)  #Output: HELO,WORLD
greet(whisper) #output:hello,world


## A function is an instance of the object type
## you can store the function in a variables
## you can pass the function as an arguments to another function
## you can return a function from another function
## you can store function in data structure such as lists, dictionaries,etc

###built-in higher order functions

#map function

def addition(n):
    return n+n

number=(1,2,3,4,5)
result=map(addition,number)

print(result) 
print(list(result))
for x in result:
    print(x)

# filter function 

## the filter function is used to filter the elemnts of a sequense based on a given condition
## it takes two arguments : a function that defines the condition and iterable(like a list) to be filtered.
## the function should return true for elementa that should be included in the resuklt and false for those that should be included in the result and false for those that should be excluded.

def fun(n):
    letters={'a','e','i','o','u'}
    if n in letters:
        return True
    else:
        return False
sequences=['a','b','c','d','e','f','g']
filtered_sequences=filter(fun,sequences)

print(type(filtered_sequences))
for x in filtered_sequences:
    print(x)


## lambda function

lambda_func=lambda x:x*2
print(lambda_func(5))