# if
a = 77
b = 100
if b > a:
    print("b is greater than a")


# if_elif

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")



# if _elif_else

a = 100
b = 77
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# if else with OR

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


# if else with AND

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


# if else with NOT

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


# nested if loop

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


