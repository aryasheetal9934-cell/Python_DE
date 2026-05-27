def reverse_string(str1):
    rstr1=''
    index=len(str1)
    while index>0:
        rstr1+=str1[index-1]
        index-=1
    return rstr1
print(reverse_string("sheetal"))


def reverse_string1(str):
    return str[::-1]
print(reverse_string1("sheetal"))