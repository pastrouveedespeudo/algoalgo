import importlib

import test

def a():
    with open('test.py', 'a') as file:
        file.write('aa = "5"')
    importlib.reload(test)
         
def b():
    print(test.aa)

a()
b()

