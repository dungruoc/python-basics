# def myfunction():
#   print('hello')

# print(myfunction())

# myF = myfunction
# myF()

# print(myfunction) # nothing ?

# def my_returned_function():
#   return 1

# # print(myfunction())
# print(my_returned_function())

# a = my_returned_function() + 1
# print(a)

# def my_returned_function():
#   if False:
#     return 1

# # no error but the return value is None
# print(my_returned_function())

# #variable scope

# myvar = 1

# def myfunction():
#   myvar = 2
#   mylocalvar = 1

# myfunction()

# print(myvar)
# print(mylocalvar)

# def myfunction():
#   global myvar
#   myvar = 2

# myfunction()

# print(myvar)

# # function with input

# def myfunction(argument):
#   print(argument)
#   return argument

# mylist = myfunction([1, 2, 3])

# def myfunction(argument):
#   argument[0] = 5
#   return argument

# mylist2 = myfunction(mylist)
# print(mylist) # mylist was modified

# # multiple output

def myfunction(x, y):
  return x + y, x*y, (x*x + y*y) ** 0.5

# print(myfunction(3, 4))

# result = myfunction(3, 4)
# print(result[0])
# print(result[1])
# print(result[2])

# sumXy, prodXy, distZero = myfunction(3, 4)


# keyword argument

# print(myfunction(x=3, y=4))
# print(myfunction(y=4, x=3))

# default paramenters

def myfunction(x=2, y=3):
  return x + y, x*y, (x*x + y*y) ** 0.5

# print(myfunction())

# print(myfunction(y=5)) # this is not possible with Java, C as the previous agument cannot take default

# # any arguments ?
# def myfunction(*arguments, **keywords):
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# myfunction("first argument", "second",
#            "third argument",
#            firstkey="keyword argument 1",
#            secondtkey="keyword argument2")

# # unpack argument list

# mylist = (3, 4) # [3, 4]
# mylist = [3]

# print(myfunction(mylist[0], mylist[1]))

# print(myfunction(*mylist))

# mydict = {'y': 4}

# print(myfunction(**mydict))

# first-class function
# function can be assigned as variable
# myfunc = myfunction
# print(myfunc(**mydict))

# # functional programming

def add(*arguments, **keywords):
  total = 0
  for arg in arguments:
    total += arg
  for kw in keywords:
    total += keywords[kw]
  return total

# print(add(10, x=5, y=5))

# def my_add10(*arguments, **keywords):
#   return add(10, *arguments, **keywords)

# print(my_add10(x=5, y=5))


# # lambda

# my_add10 = lambda x: add(10, x)

# print(my_add10(x=5))

mylist = list(zip((1, 3, 2), ('c', 'a', 'b')))
# print(sorted(mylist))
print(sorted(mylist, key=lambda x: x[1]))

# # Weakness: Python lambda can be only 1 line expression