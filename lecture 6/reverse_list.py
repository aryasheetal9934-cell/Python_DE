# method 1
li=[10,20,30,40,50]
li.reverse()
print(li)

#method 2

a=[10,20,30,40,50]
rev=list(reversed(a))
print(rev)

#method 3

b=[10,20,30,40,50]
rever=b[::-1]
print(rever)

## using loops

a=[10,20,30,40,50]
i,j=0,len(a)-1
while i<j:
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1
print(a)
