# For loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# for loop with break statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# for loop with continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# for loop with range

for x in range(6):
  print(x)


# nested for loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# for loop with pass statement

for x in [0, 1, 2]:
  pass