import os
import shutil
import sys

print(dir(__builtins__))  # List that contains all type of Error built in python

# 2. -> get info about Exception/Error
try:
    a = 1/0
except:
    print('Error ',sys.exc_info()[0], ' Happens !')