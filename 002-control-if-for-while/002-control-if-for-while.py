# mycondition = True # False
# mycondition2 = False

# if mycondition or mycondition2:
#   print('OK')
#   print('test')
# else:
#   print('KO')

# while
# counter = 0
# while counter < 10:
#   print('doing', counter)
#   counter += 1

# # continue, break, pass

# counter = 0
# while True:
#   counter += 1
#   if counter < 5:
#     continue
#   if counter == 7:
#     pass
#   else:
#     print('doing', counter)
#   if counter >= 10:
#     break 

# for loop on iteratables

# list
# for element in ['a', 2, 'c']:
#   print(element)

# # tuple
# for element in (1, 2, 3):
#   print(element)

# mydict = dict([
#   ('key1', 'value1'),
#   ('key2', 'value2')
# ])

# for key in mydict:
#   print(key)

# # # how to print values?

# for key, value in mydict.items():
#   print(key, value)

# # enumerate

# mylist = ['a', 'b', [1, 2]]

# for element in mylist:
#   print(element)

# # want index controlled ?

# myindex = 0

# for element in mylist:
#   if myindex == 1:
#     print('do something', element)
#   myindex += 1

# # simple with enumerate

# for index, element in enumerate(mylist):
#   if index == 1:
#     print('do something', element)

# print(enumerate(mylist)) # just a generator object

# # range (xrange in Python 2)

# for i in range(10):
#   print(i)

# # step
# for i in range(0, 20, 3):
#   print(i)


myset = set(['a', 1, 2, 'a', 'b', 1, 2])
for element in myset:
  print(element)


# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
# for first, second in zip(mylist1, mylist2):
#   print(first, second)
