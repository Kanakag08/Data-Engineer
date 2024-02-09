# Exception Handling
# try and expect

def funct(a):
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)


try:
    funct(3)
    funct(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


# try else except
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


# Finally
try:
    k = 5 // 0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')



# raising a exception
try:
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise