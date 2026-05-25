list=[2,3,5,7,11,13,19,20]

for num in list:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
         print(num)

