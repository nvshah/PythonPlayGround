import sys

try:
    a = 1/0
except:
    print('Error ',sys.exc_info()[0], ' Happens !')