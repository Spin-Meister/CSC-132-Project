from functools import reduce


def f(x):
    return 's' in x or 'S' in x


# family = ["Kyle","Gus","Rosie","Honey Butter", "Sarah"]
# multiples = list(filter(f,family))
# print(multiples)


def f(x):
    return x * x


# newList = list(map(f,range(1,11)))
# print(newList)

def f(x, y):
    return x * y


# fact = reduce(f,range(1,11))
# print(fact)

# list comprehension
# reduces the amount of work to create a new list
# down to one line of code
cubes = [x * x * x for x in range(10)]

# syntax for list comprehensions
# for item in iterable if condition

# built in operations for sets
# union
# | prints all unique values
# & prints all shared values


###Dictionary Introduction
offices = {"Jones": 247, "Bartholomew": 123, "Jeffery": False, "Wonka": "Chocolate Factory"}
print(offices)
del offices["Wonka"]
print("Wonka is no longer needed")

# In keyword only finds key not values
if not "Wonka" in offices:
    print("Wonka successfully terminated")

#Must use .values function
if 123 in offices.values():
    print("Bartholomew still employed")

