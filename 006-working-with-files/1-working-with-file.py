# file = open('1-working-with-file.py', 'r')
# for line in file:
#   print(line)
# file.close()

# exception

# file = open('Not Found', 'r')
# for line in file:
#   print(line)
# file.close()

# try:
#   file = open('Not Found', 'r')
#   for line in file:
#     print(line)
#   file.close()
# except Exception as e:
#   print(e)
# finally:
#   file.close()


# with closure

# with open('1-working-with-file.py', 'r') as file:
#   for line in file:
#     print(line, end='')


# try:
#   with open('005-working-with-file.py-', 'r') as file:
#     for line in file:
#       print(line, end='')
# except:
#   pass

# print("this is run")

# with open('1-working-with-file.py', 'rb') as file:
#   print(file.read())

# Read Text vs Binary file
# try:
#   with open('005-working-with-file.py', 'rb') as file:
#     print(file.read())
# except:
#   pass


# try:
#   with open('005-working-with-file.py', 'rb') as file:
#     print(file.read())
# except:
#   pass

# try:
#   with open('005-working-with-file.py', 'rb') as file:
#     print(file.read().decode())
# except:
#   pass


# write

# mycontent = """\
# Xin chào! Đây là khóa Python cơ bản.
# """

# text file
# try:
#   with open('test/written-file.txt', 'w') as file:
#     file.write(mycontent)
# except:
#   pass

# bibary file
# try:
#   with open('test/written-file.txt', 'wb') as file:
#     file.write(mycontent.encode('utf-8'))
# except:
#   pass

# os and sys packages

# import os

# print(os.getcwd())

# print(os.listdir())

# for item in os.listdir():
#   print(item)
#   print(os.path.isfile(item))
#   print(os.path.abspath(item))

# myfilename = 'D:\\JavaScriptTutorials\\HNB-Training\\hnb-training-python\\006-working-with-files\\1-working-with-file.py'

# print(os.path.basename(myfilename))

# folder, file = os.path.split(myfilename)
# print(folder)
# print(file)

# abspath = os.path.join(folder, file)
# print(abspath)

import sys
print(sys.platform)
print(sys.path)