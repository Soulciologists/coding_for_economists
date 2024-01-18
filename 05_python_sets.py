#intro to data type set
#set is a collection of well defined object
myset = {1,2,3}
print(myset)

#check type
print(type(myset))

#set only contains unique values
myset = {1,2,3,3,3}
print(myset)

#check membership
print(1 in myset)

print(set('aaaaaaaaaabbbbbbbbbbcccccccc'))

#Define two sets and check out set operators
setA = {1,2,3}
listB = [3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
setB = set(listB)

print(setA, setB)