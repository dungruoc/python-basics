# test = 'hello'

# def myfunction():
#   test = 'a'
#   print(locals())

# myfunction()

# print(globals())


# Function closure
# def myfunction(x):
#   const = 1
#   def inner_func():
#     return x + const
#   return inner_func

# test = myfunction(2)

# print(test())

# def logger(func):
#   def inner(*args, **kwargs): #1
#     print("Arguments were: %s, %s" % (args, kwargs))
#     return func(*args, **kwargs) #2
#   return inner

# @logger
# def myfunction(x, y = 1):
#   return x * y

# res = myfunction(3, y=4)
# print(res)

# Generator function

def generator_func():

  print('hello')
  yield 'world' # return
  
  print('bonjour')
  yield 'tout le monde'

gen = generator_func()

# res = next(gen)
# print(res)

# res = next(gen)
# print(res)

# res = next(gen)
# print(res)

for item in gen:
  print(item)

# Loop on N first squared number

# def squared(N):
#   return [n * n for n in range(N)]

# test = squared(1000000) # 1M elements alocated in memory

# for n in test:
#   print('testing', n)
#   if n > 10:
#     break


# def squared(N):
#     num = 0
#     while num < N:
#         yield num * num
#         num += 1

# test = squared(1000000)

# for n in test:
#   print('testing', n)
#   if n > 10:
#     break

# print(test)


