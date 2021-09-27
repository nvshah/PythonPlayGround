from ctypes import c_uint32 as unsigned_int32

print((11).bit_length())

# The only way to get unsigned type in python as python do not have fix bits pattern
# python provide infinte bits to represent the number
i = unsigned_int32(-100).value
si = i >> 1

print(i, si)

n1 = f"{-5 & 0b1111:04b}"
print(n1)




