# convert list into set

a=[1,2,3,4,5]
print(type(a))
set=set(a)
print(type(set))
print(set)

# problem
num_set={1,2,3,4,5}
for value,char in enumerate(num_set): # enumerate used for itrates indvidual elements
    print(char,end=" ")

# some methods available in set 

a={"riya"}
a.add("sheetal")  # adding element to set
print(a)
 
b={1,2,3,4,5}
b.update("6","7","8","9","10") # adding multiple elements to set
print(b)

b.pop()   # remove random element from set
print(b)

b.remove("9")  #remove specific element from set
print(b)

b.discard("11") # remove specific element form set, if elememnt not prensent it will not raise error
print(b)


## WAP to remove all elemnts from set

# method 1
 
a={1,2,3,4,5}
a.clear()
print(a)

#method 2

a={1,2,3,4,5}
for i in range(len(a)):
    removed_element=a.pop()
print(removed_element)
print(a)





set1={1,2,3}
set2={3,4,5}

print(set1 | set2)  # union of set1 and set2
print(set1 & set2)  #Intersection of set1 and set2
print(set1 - set2)  #difference of set1 and set2