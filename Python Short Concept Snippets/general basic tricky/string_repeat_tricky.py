s = "123"

s2 = 0 * s  #''
s3 = -1 * s #''

print(s2, s3)

print(s[-1:9]) #3

#bytes obj
b = b'foo\xddbar'

#Not escaping \ in byte string
b = rb'foo\xddbar'

#str.encode() is used to encode for utf8
b = bytes('foo.bar', 'utf8')