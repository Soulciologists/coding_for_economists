# Let's have a look at loop syntax

# for loop operates on "iterables"

# Let's create an iterable object

mylist = [1,2, 'abc']

# Let's iterate over the object
for item in mylist:
  # loop body needs to be indented once
  print(item)

for banana in mylist:
  if banana == 1:
    print(banana)
  else:
    print('item is not equal to 1')

# looping over a range of values
for i in range(5): # range generates values on the fly
  print(i)

#Another wat to 
range_vals = [0,1,2,3,4] # stored by the computer. It consumes computer memory, not efficient
for i in range_vals:
  print(i)

# looping over a list of strings
for name in ["Alice", "Bob", "Charlie"]:
  print(name)
  #iterate through each string
  for letter in name:
    print(letter)

# Using the enumerate() function to get both index and value
print("using enumerate()")
for index, name in enumerate(["Alice", "Bob", "Charlie"]):
  print(index, name)

# Equivalent loop using indexing
mylist = ["Alice", "Bob", "Charlie"]
for index in range(len(mylist)):
  print(index, mylist[index])

#Using loop to create a list of captial letters from A-Z
alphabet = []
for i in range(65, 91):
  char = chr(i)
  alphabet.append(char)
  print(i, chr(i))

print(alphabet) 

# While loop
# While loops are used when you don't know how many times you want to loop
i = 0
while i < 10:
  # increment our counter every iteration
  print(i)
  i += 1
  print(i)

#list comprehensions
#let's have a look at a for loop creating a list of sources from 0 to 10
squares = []
for num in range(0, 11):
  squares.append(num**2)

print(squares)

#Doing the same using list comprehension
squares = [num**2 for num in range(0, 11)]
print(squares)

# using if statements in list comprehensions
even_squares = [num**2 for num in range(0, 11) if num % 2 == 0]
print(even_squares)