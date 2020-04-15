# Commments start with #

# inline codes, that are executed
print('hello world')
print("hello world")

2 + 3
print(5 * 4)


# # Python interpreter:
# # - interactive mode
# #    python
# #    >>> 
# # - run a python file
# #    python 001.py
# # - Jupyter note book

# # Variable - dynamic type binding - as simple as JS
# # not let, var, const keywords: more freestyled

myVar = 'Hello world'
print(myVar)

myVar = 1
print(myVar + 2)

myVar = 3.14

myVar1 = '1'
myVar2 = '2'
myVar1 + myVar2
int(myVar1) + int(myVar2)

# print(myVar)

# # primitives

# # number

myvar = 5
print(myvar)
print(myvar / 2)
print(myvar // 2)
print(myvar % 2)

# # stronger than usual
myvar = 5.5
print(myvar)
print(myvar / 2)
print(myvar // 2)
print(myvar % 2)

# # exp +, -, *, /

print(myvar ** 2)

# math library
import math
print(math.pow(myvar, 2))
print(math.log(myvar))


# # big numbers
# # nightmare for C/C++ or Java developer
myvar = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(myvar + 1)



# # boolean

myvar = True
print(myvar)
myvar = not myvar # !
print(myvar)
print(myvar and True)
print(myvar or True)


# # String

myString = "Hello\nWorld"
print(myString)
myString = 'Hello\nWorld'
print(myString)
myString = """This is a string
  that expands multi lines, without endline character.
  But we can avoid endline\
 with backslash
    Pay attention to the indent spaces"""
print(myString)


print('C:\some\name')  # here \n means newline!
# Raw string
print(r'C:\some\name')  # note the r before the quote

# # string operators
print (3 * 'hello')
print ('hello' + ' ' + 'world')

# # substring
string = 'hello'
string[0]
string[0:1] # slice h e l l o
string[2:4]
string[-1]
string[-3:-1]

string[::-1]


len(string)


# # string format

print ('hello %s for %i times' % ('Python', 1000))


firstvar = 'hello'
secondvar = 'world'
namevar = 'Albert'

print('{0} {1} from {name}'.format(firstvar, secondvar, name=namevar))

# # string is unmutable
# try string[0] = 'a'


# -*- coding: utf-8 -*-

myString = "Xin chào"
print(myString)


# # List

list1 = [1, 2, 3]
print(list1)

# # list operators

print(2 * list1)

# Elements in list can be anything
list2 = ['a', "hello", 3, 4, [1, 2]]

print (list1 + list2)

# # add new element to a list

list2.append(list1)

# print(list2)

# slice - the same as substring

list2[2:4]

list2[-1]

# # Modify element in list

# list2[0] = 'b'
# print(list2)

# # reference assignment, not copy
list3 = list2
list3[0] = 'new val'
print(list2)

# # Use deep copy to avoid reference copy 

import copy
list3 = copy.deepcopy(list2)
list3[2][1] = 3
list2
list3 = [item for item in list2]
list3[0] = 'new new val'
list3[4][1] = 10

# # Tuple: unmutable list

mytuple = (1, 2, 3, ('a', 'b'))
print(mytuple)

mytuple[3][0] = 'X'
mytuple[0] = 4

# tuple from list

mylist = [1, 2, 3]
mytuple = tuple(mylist)

# # list from tuple

newlist = list(mytuple)

mylist[0] = 'a'
mytuple[0] = 'a' # error


items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
filtered = list(filter(lambda x: x > 5, squared))

from functools import reduce
product = reduce((lambda x, y: x * y), filtered)

# # list multiplication

mylist = [0] * 10

# matrix: list of list
mylist = [[0, 0, 0]] * 10


# mylist[0][0] = 1 # inner list is copied by reference

# # difference ?
mylist = [[0] * 3 for i in range(10)]


# # other object
# mylist = [{'key1': 'value1', 'key2': 'value2'}] * 10
# mylist[0]['key2'] = 1
# mylist[0]['key2'] = 'new value'


# # Dictionary: Map or Js object

mydict = {
  'key1': 'value1',
  'key2': 'value2'
}

print(mydict)
print(mydict.get('key2'))
print(mydict['key2'])
# key not exist
print(mydict['key3']) # exception
print(mydict.get('key3')) # safe way

# # keys
# mydict.keys
# # unhashable type

mydict = {
  (1, 2): 1 * 2,
  (3, 4): 3 * 4
}

# print(mydict)
# print(mydict.get((1, 2)))
# print(mydict.get((3, 4)))
# print(mydict.get((2, 3)))

# # TypeError: unhashable type: 'list'
mydict = {
  [1, 2]: 1 * 2,
  [3, 4]: 3 * 4
}

# # dict from list of pair

mydict = dict([
  ('key1', 'value1'),
  ('key2', 'value2')
])

# mydict = dict([
#   ['key1', 'value1'],
#   ['key2', 'value2']
# ])

# # Delete element

mylist = [1, 2, 3]
del mylist[0]
del mylist

mydict = dict([
  ('key1', 'value1'),
  ('key2', 'value2')
])

del mydict['key1']

# print('key1' in mydict)
# print('key2' in mydict)


# # zip

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c', 'd']
mylist3 = ['a', 'b', 2, 'd', 'test']


list(zip(mylist1, mylist2, mylist3))
tuple(zip(mylist1, mylist2))

mydict = dict(zip(mylist1, mylist2))

# # Set

myset = set() # set([])
myset.add('a')
myset.add(1)
myset.add('a')
myset.add(1)

myset = set(['a', 1, 2, 'a', 'b', 1, 2])

# print('a' in myset)
# print('c' in myset)
