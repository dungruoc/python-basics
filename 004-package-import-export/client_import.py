
# from module.some_tools import say_hello, not_exported_hello

# say_hello()
# not_exported_hello()

from module import say_hello

say_hello()

# from module import not_exported_hello

# not_exported_hello()

from module import *

say_hello()
not_exported_hello()


