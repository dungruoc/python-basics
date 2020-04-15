# class Shape:
#   static_value = 10
#   # constructor
#   def __init__(self, width, height): # self === this
#     self.width = width
#     self.height = height

#   def draw(self):
#     print('shape draw (%d, %d)' % (self.width, self.height))

# shape = Shape(3, 5)
# shape.draw()

# class Circle(Shape):

#   def draw(self):
#     print('circle draw (%d, %d)' % (self.width, self.height))


# shape = Circle(3, 5)
# shape.draw()


# No private methods
# every method is overriden when redefined in child

# operator overloading

class Integer:

  def __init__(self, num):
    self.num = num

  def __str__(self):
    return 'Integer %d' % self.num
  
  def __bool__(self):
    return self.num != 0

  def __len__(self):
    return len('%d' % self.num)
  
  def __add__(self, other):
    return Integer(self.num + other.num)

  def __sub__(self, other):
    return Integer(self.num - other.num)

  def __mul__(self, other):
    return Integer(self.num * other.num)

  def __eq__(self, other):
    return self.num  == other.num

  def __ne__(self, other):
    return self.num  != other.num

  def __truediv__(self, other):
    return Integer(self.num / other.num)

  def __abs__(self):
    return Integer(abs(self.num))

  def __ge__(self, other):
    return self.num >= other.num

  def __gt__(self, other):
    return self.num > other.num

# print(Integer(3))

# print(Integer(3) < Integer(4))

# print(Integer(3) > Integer(4))

# print(Integer(3) + Integer(4))

# if Integer(0):
#   print("Error")
# else:
#   print("OK")

# if Integer(2):
#   print("OK")
# else:
#   print("Error")

# print(len(Integer(123456)))

# class MyException(Exception):
#   pass

#   def __str__(self):
#     return 'MyException'

# def throw_exc():
#   raise MyException()

# def call_exc():
#   try:
#     throw_exc()
#   except MyException as e:
#     print('caught', e)
#   except Exception as e:
#     print('unkown', e)

# call_exc()

# print(Integer(3) / Integer(0))

try:
  print(Integer(3) / Integer(0))
except ZeroDivisionError as err:
  print(err)

