def say_hello():
  print('Hello')

def not_exported_hello():
  print('Hello secured')

# This will be executed only if run the file
# When imported, it's not run
# print(globals())
if __name__ == "__main__":
  say_hello()
  not_exported_hello()

# https://www.tutorialsteacher.com/python/python-package