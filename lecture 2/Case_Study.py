# A person Requries at least 80% of marks to be qualified for test for physical assesment 
# condition if  he's a sports person then he requires 75% of marks to be qualified for test for physical assesment
# so firsst declare the global vaiable which store the marks 
# create a function which will check whether the person is a sports person or not and then check the marks and print the result

marks=85 #global variable
def calculate_quota(total_marks):
    global sports #accessing the global variable
    sports=True #local variable
    if sports==True:
        return "sports quata is applicalbe. and your new qualifying marks are 75"
    else:
        return "sports quota is not applicable"
    
print(f'your marks are {marks},your status is {calculate_quota(marks) },and your sports quota is {sports}')
