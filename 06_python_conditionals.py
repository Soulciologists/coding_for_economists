#introduce package
import random

#Generate random number between 20 and 34
random_number = random.randint(20,34) # 34 is included in the random pool
print(random_number) # we get a new random integer each time we run the script

# first look at conditional statements
# Cases should be typically exhausted
if random_number < 25:
  print("The number is less than 25")
elif random_number < 30:
  print("The number less than 30")
else:
  print("The number is less than 34")

# second look at conditional statements
a = random.randint(0, 20)
b = random.randint(10, 20)

if a < 9:
  print(f'a is less than 9, a = {a}')
  if b < 19:
    print(f'b is less than 19, b = {b}')

# Equivalently, we can combine the logical conditions
if a < 9 and b < 19:
  print("a is less than 9 and b is less than 19")