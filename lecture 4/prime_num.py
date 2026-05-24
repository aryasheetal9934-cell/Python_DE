nums=[2,3,5,7,11,13,19,20]

for num in nums:
     if num>1:
        for x in range(2,num):
           if num%x==0:
            print(num,"not prime")
           break

        else:
           print(num,"prime")    


