# number Function
# int,float,complex

x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Random Number
import random
print(random.randrange(1, 10))