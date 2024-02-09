# Function

# creating a function
def funct():
    print("Welcome to Function")

# calling a function
funct()

# python function with parameters
# adding two number
def add(num1:int,num2:int):
    num3=num1+num2
    return num3

num1=5
num2=5
ans=add(num1,num2)
print(f"The addition of {num1} and {num2} is {ans}")


# python function with arguments
def name(fname,lname):
    print("Hello, My name is ", fname+" "+lname)


name("Kanak","Agrawal")


# map() function
# Return double of n
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# lamda function
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# string using map
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)