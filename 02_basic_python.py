#Basic arithmetic operations in Python

#Add two numbers
#2 + 4

print(2+4)

#Divide two numbers
print(10/5)

#careful division return float
print(type(10/5))

#statisically typed languages

#Exponential
print(2**3)

x = 5
y = x ** 2
print(y)

# string
a = "Hello World"
print(a)

#arithmrtic operations on strings
print(a*5)

#concatenation
b = "Hello python"
print(a+ " " +b) 

# #substraction
# print(a-b) # type error

# #division
# print(a/b) # type error

# index
print(a[0])
print(a[-1])
print(a[0:4])

#how many characters does our string have?
print(f'Our string has {len(a)} characters')
print('Our string has {} characters'.format(len(a)))

# have a look at logical statements
print(2==2)
print(2==3)
print(2!=3)

#check if True and 1 are in fact equivalent
print(True==1)

#True equal to 1 and False equal to 0
print(True+False+True)

#check equivalence of 2 variables
print(a==b)

print(2 == 2 and 3==3) #True
print(2 == 2 and 3==4) #False

print(2 == 2 or 3==4) #True
print(2 == 3 or 3==4) #False