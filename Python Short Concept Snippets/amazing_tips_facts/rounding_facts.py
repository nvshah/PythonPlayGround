# int() will round towards 0
# so in case of +ve it will be floor
# & in case of -ve it will be ceil

print(int(1.8))  # 1
print(int(-1.8)) # -1

# // will always return floor val
print(2 // 3) # 0
print(-2 // 3) # -1
print(int(-2/3)) # 0