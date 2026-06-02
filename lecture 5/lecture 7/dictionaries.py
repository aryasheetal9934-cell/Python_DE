# methods available in dictionaries

# from typing import Dict


# dict={"name": "sheetal", "age": "21"}
# print(dict.keys())

# print(dict.values())
# print(dict.items())
# print(dict.get("name"))

# # create a dict where keys are numbers from 1 to 5 and values are there squares

# squares={x:x**2 for x in range(1,6)}
# print(squares)


# WAP program to sort [asecnding or desecding order] a dict by values

def sort_dict_by_values(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))

colors = {"red":1, "green":5, "blue":2, "white":3}

print(colors)

print("sorted dict in ascending order:",
      sort_dict_by_values(colors))

print("sorted dict in descending order:",
      sort_dict_by_values(colors, reverse=True))


#Merging two dictinories

# d1={'a':1000,'b':2000}
# d2={'c':3000,'d':4000}

# d=d1.copy()
# d.update(d2)
# print(d)

