import pathlib
import sys

# path = pathlib.Path.cwd() / 'general basic tricky'
# print(path)

sys.path.append('./general basic tricky')

from reduce_doubt import  f_from

f_from(10, b=30)

