# enumerate()
""" The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
The enumerate() function adds a counter as the key of the enumerate object.
"""
# .items()
"""The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary,
"""


# print to the console
print("hello World!")


# loops
for i in range(0, 11): # starts at 0 goes to 10
    print(i)

for i in range(10, -1, -1): # starts at 10 counts down to 0
    print(i)

for i in range(1000): # counts all the way to 999 from 0
    print(i)


# variables
a = "Hello "
b = "World! "
c = 365
print(a + b + str(c)) # str turns number vairiable to a string

a = 15
b = 10
c = "365"
print(a + b + int(c)) # int turns string vairiable to an integer


# lists
a = [10, 20, 30, 40, 50, 365]
for num in a: # num is each index of a
    print(num) # prints each item or index

for i in range(len(a)): #i is each item in the a list to its len   or length like JS
    print(a[i])

for i in range(len(a)):
    # print(str[i] + " :: " + str(a[i]))  # prints index number and item in that index position
    print(f"{i}: {a[i]}") # prints index number and item in that index position

print(len(a))

for num in enumerate(a):
    print(num)

# # insert to front of list
a.append(4444)
print(a)

# add to the end of a list
a.pop(5)
print(a)

# insert to index of list
a.insert(0, 999)
print(a)


# # dictionary
d = {
    'Goats': 12,
    'foo': 10,
    'bar': 20,
    'baz': 30
} # creates dictionary
d['beej'] = 33 # adds to end of dictionary

for i in d: # for each itewm in d dictionary
    print(f"{i}: {d[i]}") # print the index number : key value pair

for k, v in d.items(): # k is the index of each item in d dictionary  v is set to the keys and values for each item listed in d dictionary
    print(f"{k}: {v}")


# list comprehension
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)

#   output      input        filter
#     ^           ^             ^
b = [x*2    for x in b    if x <= 5] # x is each index of b  each one *2  but only up to 5 * 2

b = [[i for i in range(x)] for x in b if x <= 5] # setting i as an index for the index of b array if the index is less than or equal to 5itterates 5 times
print(b)

c = []
for x in b:  # for each index in b
    if x <= 10: # x is less than or equal to 5
        c.append(x * 2) # append each index multiplied by 2
print(c)


# # dictionary comprehension














