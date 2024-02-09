import numpy as np


a = np.arange(1, 10)
print(a)


x = range(1, 10)
print(x)    # x is an iterator
print(list(x))


# further arange examples:
x = np.arange(10.4)
print(x)
x = np.arange(0.5, 10.4, 0.8)
print(x)
