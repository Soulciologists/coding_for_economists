# Let's talk about functions

#function definition syntax
def add_one(num):
  return num + 1 # typically you find a returnn statement at the end of a function

print(add_one(5))

# Function without return statement and without arguments
def add_one_str():
  print(6)

print(add_one_str())

#Try to assign the output of a function to a variable
res = add_one(5)
res_str = add_one_str()

print(res, res_str)

# Multiple return values
def add_one_return_both(num1):
  return num1, num1 + 1

print(add_one_return_both(5))
print(type(add_one_return_both(5)))

def add_two_nums(num1, num2):
  res = num1 + num2
  return num1, num2, res

print(add_two_nums(6, 7))

#default values for function arguments
def exponentiate(num, exponent=2):
  return num ** exponent

print(exponentiate(5, 2) == exponentiate(5))

#keyword arguments: using the argument name to assign values. In this case, order doesn't matter
print(exponentiate(exponent=3, num=5))

#Functions with variable number of arguments
def add_nums(*nums):
  res = 0
  for num in nums:
    res += num
  return res

print(add_nums(1, 2, 3, 4, 5, 6))

#est's try to code up some docstrings for a function
def cast_listitems_to_str(list_of_items):
  """
  This function takes a list of items and casts them to a string
  
  paraments:
  ----------------------
  list_of_items: list

  Returns:
  ----------------------
  
  """
  list_of_strings = []
  for item in list_of_items:
    list_of_strings.append(str(item))
  return list_of_strings

print(cast_listitems_to_str(list_of_items=[1, 2, "a" , 123]))

#print(help(cast_listitems_to_str))

#scope of a variable
def test(a, b):
  c = a + b #scope of c is confined to function

c = 5 #here c has a global scope

#lambda functions (aka anonymous functions)
#reference function
def square(x):
  """
  Returns the square of x
  
  Parameters:
  -----------------------
  x: int or float or double

  Returns:
  -----------------------
  square_x: int or float or double
  """
  return x ** 2

#equivalent lambda function
square_lambda = lambda x: x ** 2
print(square(5) == square_lambda(5))
