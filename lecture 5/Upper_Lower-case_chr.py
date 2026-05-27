sentence="The quick Brown Fox jumps over a Lazy dog."
count={'upper':0, 'lower': 0}
for char in sentence:
    if char.isupper():
        count['upper']+=1
    elif char.islower():
        count['lower']+=1
print("number of upper char:",count['upper'])

print("number of upper char:",count['lower'])