# HTML, JSON, XML, CSV

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# f = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
# htmlContent = f.read().decode('utf-8')
# # print(htmlContent)

# # with open('test/wiki-python-language.html', 'wb') as file:
# #   file.write(htmlContent.encode('utf-8'))

# from html.parser import HTMLParser

# parser = HTMLParser()
# parser.feed(htmlContent)

# parsed_html = BeautifulSoup(htmlContent)

# print(parsed_html.prettify())

# test_api = urlopen('http://120.72.106.56:9000/v1/documents')
# get_content = test_api.read().decode('utf-8')

# print(get_content)

# import json

# json_parsed = json.loads(get_content)

# print(json_parsed)

# firstname = json_parsed['data'][0]['filename']
# print(firstname)

# firstname = 'file001.txt'
# test_api = urlopen('http://120.72.106.56:9000/v1/documents/%s' % firstname)
# get_content = test_api.read().decode('utf-8')

# print(get_content)

# myObj = {
#   'key1': 1,
#   'key2': ['a', 2],
#   'key3': ('test', [1])
# }

# import pickle

# picklestring = pickle.dumps(myObj, protocol=0)
# print(picklestring)

# newObj = pickle.loads(picklestring)
# print(newObj)

# class ComplexClass:
#   def __init__(self):
#     self.text = 'hello'
#     self.list1 = ['a', 2]
#     self.tuple1 = ('test', [1])

#   def show(self):
#     print(self.text, self.list1, self.tuple1)

# myObj = ComplexClass()
# myObj.show()

# picklestring = pickle.dumps(myObj, protocol=0)
# print(picklestring)

# with open('test/pickle-object.pkl', 'wb') as file:
#   file.write(picklestring)

# with open('test/pickle-object.pkl', 'rb') as file:
#   picklestring = file.read()

# newObj = pickle.loads(picklestring)
# newObj.show() # but this need ComplexClass defined an loaded before

mystring = """{
  'key1': 1,
  'key2': ['a', 2],
  'key3': ('test', [1])
}
"""

test = eval(mystring)
print(test)

print(eval("2 + 1"))