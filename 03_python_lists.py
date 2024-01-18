#in this file we look at list, tuple, dictionary and set

#list
mylist = [1,2,3,4,5]
print(mylist)

print(type(mylist))

#grab first object of the list
print(mylist[0])

#how many object in our list?
print(f'mylist has {len(mylist)} objects.')

#list is flexible since it can include differnt type of data
mixedlist = [1, "two", 3.0, [4, "four"], 5]
print(mixedlist)

#we can add an object to a list
mixedlist.append(6)
print(mixedlist)

#remove an object from a list
mixedlist.pop() # without argument, it removes the last item
print(mixedlist)
mixedlist.pop(0)
print(mixedlist)

print(mixedlist.count(1))
