'''
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


np.arange(12.04, 12.84, 0.08)
'''

# linespace

'''import numpy as np

# 50 values between 1 and 10:
print(np.linspace(1, 10))
# 7 values between 1 and 10:
print(np.linspace(1, 10, 7))
# excluding the endpoint:
print(np.linspace(1, 10, 7, endpoint=False))'''

import numpy as np


samples, spacing = np.linspace(1, 10, retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 20, endpoint=True, retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 20, endpoint=False, retstep=True)
print(spacing)

