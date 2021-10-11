# #! python = 3.10
#
# # 1
# a = "sdsd"
# match x:
#     case "sdsd":
#         print("It is sdsd")
#
#     case "hell":
#         print("it is hell")
#
#     case _:
#         print('Default Case')
#
# # 2
# coord = (1, 0)
# match coord:
#     case(0, 0):
#         print('0, 0')
#     case(0, y):
#         print('0', y)
#     case(x, 0):
#         print(x, '0')
#     case(x, y) if x == y:
#         # Guard
#         print('x same y')
#     case(_, _):
#         print('Any Pair')
#     case _:
#         print('Not a Pair')
#
# # 3
# lst = []
# match lst:
#     case [_]:
#         print('one elelemnt')
#     case [_,_]:
#         print('Two Element')
#     case [x,y,z];
#         print('3 elements : ',x,y,z)
#     case [x,y,z,_,*a]:
#         print('four or more elements', a)
#     case [x,y,z,*a]:
#         print('three or more elements', x,y,z,a)
#     case _:
#         print(None)
#
